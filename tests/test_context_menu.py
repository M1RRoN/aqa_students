import pytest

from browser.browser_factory import BrowserName
from config.config_reader import ConfigReader
from pages.context_menu import ContextMenuPage
from pages.main_page import MainPage


@pytest.mark.parametrize("driver", [browser for browser in BrowserName], indirect=True)
def test_context_menu(driver):
    main_page = MainPage(driver)
    menu = ContextMenuPage(driver)
    driver.get(url=ConfigReader().get("herokuapp_url"))
    main_page.go_to_context_menu_page()

    menu.click_on_hot_spot()
    alert_text = menu.get_alert_text_after_right_click()
    menu.accept_alert_after_right_click()
    expected_text = "You selected a context menu"

    assert expected_text == alert_text, f"Expected alert text: '{expected_text}', but got: '{alert_text}'"
