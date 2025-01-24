import pytest

from browser.browser_factory import BrowserName
from config.config_reader import ConfigReader
from pages.js_alerts import AlertsPage
from pages.main_page import MainPage
from browser.scripts import CLICK_ON_ALERT, SEND_KEYS_IN_PROMPT


@pytest.mark.parametrize("driver", [browser for browser in BrowserName], indirect=True)
def test_accept_alert(driver, get_config):
    main_page = MainPage(driver)
    alert_page = AlertsPage(driver)
    driver.get(ConfigReader().get("herokuapp_url"))
    main_page.go_to_js_alerts_page()
    alert_page.wait_for_open()
    alert_page.click_on_js_button()
    alert_text = driver.get_alert_text()
    expected_alert_text = "I am a JS Alert"
    assert expected_alert_text == alert_text, f"Expected alert text: '{expected_alert_text}', but got: '{alert_text}'"
    driver.alert_accept()
    text = alert_page.get_result_text()
    expected_text = "You successfully clicked an alert"
    assert expected_text == text, f"Expected result text: '{expected_text}', but got: '{text}'"

    alert_page.click_on_confirm_button()
    driver.switch_to_alert()
    alert_text = driver.get_alert_text()
    expected_alert_text = "I am a JS Confirm"
    assert "I am a JS Confirm" == alert_text, f"Expected alert text: '{expected_alert_text}', but got: '{alert_text}'"
    driver.alert_accept()
    text = alert_page.get_result_text()
    expected_text = "You clicked: Ok"
    assert expected_text == text, f"Expected result text: '{expected_text}', but got: '{text}'"

    alert_page.click_on_prompt_button()
    driver.switch_to_alert()
    alert_text = driver.get_alert_text()
    expected_alert_text = "I am a JS prompt"
    assert "I am a JS prompt" == alert_text, f"Expected alert text: '{expected_alert_text}', but got: '{alert_text}'"
    driver.alert_send_keys("done")
    driver.alert_accept()
    text = alert_page.get_result_text()
    expected_text = "You entered: done"
    assert expected_text == text, f"Expected result text: '{expected_text}', but got: '{text}'"


@pytest.mark.parametrize("driver", [browser for browser in BrowserName], indirect=True)
def test_alerts_and_js(driver):
    main_page = MainPage(driver)
    alert_page = AlertsPage(driver)
    driver.get(ConfigReader().get("herokuapp_url"))
    main_page.go_to_js_alerts_page()
    alert_page.wait_for_open()
    driver.execute_script(CLICK_ON_ALERT, keys="Click for JS Alert")
    driver.alert_accept()
    alert_page.wait_for_open()
    text = alert_page.get_result_text()
    expected_text = "You successfully clicked an alert"
    assert expected_text == text, f"Expected result text: '{expected_text}', but got: '{text}'"

    alert_page.confirm.element_to_be_clickable()
    driver.execute_script(CLICK_ON_ALERT, keys="Click for JS Confirm")
    driver.alert_accept()
    alert_page.wait_for_open()
    text = alert_page.get_result_text()
    expected_text = "You clicked: Ok"
    assert expected_text == text, f"Expected result text: '{expected_text}', but got: '{text}'"

    driver.execute_script(SEND_KEYS_IN_PROMPT, keys="done")
    driver.execute_script(CLICK_ON_ALERT, keys="Click for JS Prompt")
    text = alert_page.get_result_text()
    expected_text = "You entered: done"
    assert expected_text == text, f"Expected result text: '{expected_text}', but got: '{text}'"
