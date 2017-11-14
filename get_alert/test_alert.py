from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.common.by import By

import time

frame_locator = "//iframe[@src='alert/input-alert.html']"
menu_with_sub_locator = "//a[@href='#example-1-tab-2']"
drag_locator = "//button[contains(.,'Click the button to demonstrate the Input box.')]"


def switch_to_frame(driver, wait):
    frame = wait.until(expected.element_to_be_clickable((By.XPATH, frame_locator)))
    driver.switch_to.frame(frame)


def move(driver, wait):
    wait.until(expected.element_to_be_clickable((By.XPATH, "// a[ @ href = '#example-1-tab-2']"))).click()
    switch_to_frame(driver, wait)
    wait.until(expected.element_to_be_clickable((By.XPATH, drag_locator))).click()
    #driver.switch_to.default_content()
    alert = driver.switch_to_alert()
    alert.send_keys("friend")
    driver.switch_to.alert.accept()
    text = wait.until(expected.element_to_be_clickable((By.ID, "demo"))).text
    return text
