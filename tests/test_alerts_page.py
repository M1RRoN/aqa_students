import time

import pytest
from selenium.webdriver.common.by import By

from config.config_reader import ConfigReader
from elements.base_element import BaseElement
from pages.js_alerts import AlertsPage
from scripts import click_on_alert, send_keys_in_confirm


@pytest.mark.parametrize("driver", ["chrome", "firefox", "edge"], indirect=True)
def test_accept_alert(driver, url):
    elem = BaseElement(driver, "alert page", "//a[@href='/javascript_alerts']")
    alert = AlertsPage(driver)
    driver.get(ConfigReader().get("herokuapp_url"))
    alert.goto(By.XPATH, alert.BUTTON_JAVASCRIPT_ALERTS_LOC)
    alert.click_on_js_button()
    alert_text = driver.switch_to_alert().text
    expected_alert_text = "I am a JS Alert"
    assert expected_alert_text == alert_text, f"Expected alert text: '{expected_alert_text}', but got: '{alert_text}'"
    alert.accept_alert()
    text = elem.get_text(By.XPATH, alert.RESULT_LOC)
    expected_text = "You successfully clicked an alert"
    assert expected_text == text, f"Expected result text: '{expected_text}', but got: '{text}'"

    alert.confirm.click((By.XPATH, alert.JS_CONFIRM_LOC))
    alert_text = driver.switch_to_alert().text
    expected_alert_text = "I am a JS Confirm"
    assert "I am a JS Confirm" == alert_text, f"Expected alert text: '{expected_alert_text}', but got: '{alert_text}'"
    alert.accept_alert()
    text = elem.get_text(By.XPATH, alert.RESULT_LOC)
    expected_text = "You clicked: Ok"
    assert expected_text == text, f"Expected result text: '{expected_text}', but got: '{text}'"

    alert.prompt.click((By.XPATH, alert.JS_PROMPT_LOC))
    alert_text = driver.switch_to_alert().text
    expected_alert_text = "I am a JS prompt"
    assert "I am a JS prompt" == alert_text, f"Expected alert text: '{expected_alert_text}', but got: '{alert_text}'"
    driver.alert_send_keys("done")
    text = elem.get_text(By.XPATH, alert.RESULT_LOC)
    expected_text = "You entered: done"
    assert expected_text == text, f"Expected result text: '{expected_text}', but got: '{text}'"


@pytest.mark.parametrize("driver", ["chrome"], indirect=True)
def test_alerts_and_js(driver):
    driver.get(ConfigReader().get("herokuapp_url"))
    alert = AlertsPage(driver)
    alert.goto(By.XPATH, alert.BUTTON_JAVASCRIPT_ALERTS_LOC)
    click_on_alert(driver, "Click for JS Alert")
    alert.accept_alert()
    alert.wait_for_open(alert.RESULT_LOC)
    text = alert.button.get_text(By.XPATH, alert.RESULT_LOC)
    assert "You successfully clicked an alert" == text, "Текст не совпадает"

    driver.find_element(By.XPATH, alert.JS_CONFIRM_LOC)
    click_on_alert(driver, "Click for JS Confirm")
    driver.switch_to_alert()
    alert.accept_alert()
    alert.wait_for_open(alert.RESULT_LOC)
    text = alert.button.get_text(By.XPATH, alert.RESULT_LOC)
    assert "You clicked: Ok" == text, "Текст не совпадает"

    send_keys_in_confirm(driver, "done")
    click_on_alert(driver, "Click for JS Prompt")
    text = driver.find_element(By.XPATH, alert.RESULT_LOC).text
    assert "You entered: done" == text, "Текст не совпадает"
