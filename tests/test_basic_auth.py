import pytest

from browser.browser_factory import BrowserName
from config.config_reader import ConfigReader
from pages.basic_auth import BasicAuthPage
from pages.main_page import MainPage


@pytest.mark.parametrize("driver", [browser for browser in BrowserName], indirect=True)
@pytest.mark.parametrize("username, password", [("admin", "admin")])
def test_basic_auth(driver, username, password):
    driver.get(url=ConfigReader().get("herokuapp_url"))
    main_page = MainPage(driver)
    auth = BasicAuthPage(driver)
    main_page.go_to_basic_auth_page()
    auth.write_login_and_password_in_form(username, password)
    result_text = auth.get_result_text()
    expected_alert_text = "Congratulations! You must have the proper credentials."

    assert expected_alert_text == result_text, f"Expected alert text: '{expected_alert_text}', but got: '{result_text}'"
