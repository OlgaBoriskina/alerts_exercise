from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

import get_alert.alert as alert
import authorization.authorization as authorization
import unittest

base_url = "http://way2automation.com/way2auto_jquery"
keyword = "friend"

class Test (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("chromedriver.exe")
        self.driver.get(base_url)
        self.wait = WebDriverWait(self.driver, 10)
        authorization.authorize(self.wait)
        self.driver.refresh()
        self.driver.get(base_url + "/alert.php")

    def test_get_alert(self):
        test_result = alert.test_step(self.driver, self.wait)
        assert (keyword in test_result)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()