import pytest
from selenium.webdriver.common.by import By

from config.config_reader import ConfigReader
from pages.demoqa_iframes import IframesPage


@pytest.mark.parametrize("driver", ["chrome"], indirect=True)
def test_iframes(driver):
    iframe = IframesPage(driver)
    driver.get(url=ConfigReader().get("demoqa_url"))
    iframe.goto(By.XPATH, iframe.ALERTS_FRAME_WINDOWS_LOC)
    iframe.goto(By.XPATH, iframe.MENU_NESTED_FRAMES_LOC)

    driver.switch_to_frame(iframe.parent_frame)
    text = iframe.get_text_frame(iframe.parent_frame)
    assert text == "Parent frame"

    driver.switch_to_frame(iframe.child_frame)
    text = iframe.get_text_frame(iframe.child_frame)
    assert  text == "Child Iframe"
