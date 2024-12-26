from selenium.webdriver.common.by import By

from pages.demoqa_iframes import Iframes


def test_iframes(driver):
    iframe = Iframes(driver)
    driver.get(iframe.URL)
    driver.find_element(By.XPATH, iframe.ALERTS_FRAME_WINDOWS_LOC).click()
    driver.find_element(By.XPATH, iframe.MENU_NESTED_FRAMES).click()

    driver.switch_to_frame(iframe.PARENT_FRAME_LOC)
    text = iframe.get_text_frame("//body")
    assert text == "Parent frame"

    driver.switch_to_frame(iframe.CHILD_FRAME_LOC)
    text = iframe.get_text_frame("//body")
    assert  text == "Child Iframe"
