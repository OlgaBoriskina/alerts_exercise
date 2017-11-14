from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.common.by import By

frame_locator = "//iframe[@src='alert/input-alert.html']"
input_alert_locator = "// a[ @ href = '#example-1-tab-2']"
result_text_locator = "demo"
button_for_alert = "//button[contains(.,'Click the button to demonstrate the Input box.')]"
text_for_alert = "friend"


def switch_to_frame(driver, wait):
    frame = wait.until(expected.element_to_be_clickable((By.XPATH, frame_locator)))
    driver.switch_to.frame(frame)


def test_step(driver, wait):
    wait.until(expected.element_to_be_clickable((By.XPATH, input_alert_locator))).click()
    switch_to_frame(driver, wait)
    wait.until(expected.element_to_be_clickable((By.XPATH, button_for_alert))).click()
    alert = driver.switch_to_alert()
    alert.send_keys(text_for_alert)
    driver.switch_to.alert.accept()
    result_text = wait.until(expected.element_to_be_clickable((By.ID, result_text_locator))).text
    return result_text
