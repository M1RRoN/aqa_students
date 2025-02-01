import pytest

from browser.browser_factory import BrowserName
from config.config_reader import ConfigReader
from pages.demoqa_iframes import IframesPage
from pages.main_page import MainPage


# @pytest.mark.parametrize("driver", [browser for browser in BrowserName], indirect=True)
# def test_iframes(driver):
#     main_page = MainPage(driver)
#     iframe_page = IframesPage(driver)
#     driver.get(url=ConfigReader().get("demoqa_url"))
#     main_page.go_to_alerts_frame_windows_page()
#     iframe_page.go_to_nested_frames()
#
#     iframe_page.switch_to_parent_frame()
#     text = iframe_page.get_text_frame()
#     expected_text = "Parent frame"
#     assert expected_text == text, f"Expected: {expected_text} Actual: {text}"
#
#     iframe_page.switch_to_child_frame()
#     text = iframe_page.get_text_frame()
#     expected_text = "Child Iframe"
#     assert expected_text == text, f"Expected: {expected_text} Actual: {text}"
