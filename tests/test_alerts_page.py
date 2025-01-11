import time

import pytest
from selenium.webdriver.common.by import By

from pages.js_alerts import Alerts


@pytest.mark.parametrize("driver", ["chrome", "firefox", "edge"], indirect=True)
def test_accept_alert(driver, get_url):
    # driver.get(url="https://the-internet.herokuapp.com/javascript_alerts")
    driver.get(url=get_url("herokuapp_url"))
    driver.find_element(By.XPATH, "//a[@href='/javascript_alerts']").click()
    alert = Alerts(driver)
    alert.unique_element.click((By.XPATH, alert.UNIQUE_ELEMENT_LOC))
    alert_text = driver.switch_to_alert().text
    assert "I am a JS Alert" == alert_text, "Текст алерта не совпадает"
    alert.accept_alert()
    text = driver.get_text(alert.RESULT_LOC)
    assert "You successfully clicked an alert" == text, "Текст не совпадает"

    alert.confirm.click((By.XPATH, alert.JS_CONFIRM_LOC))
    alert_text = driver.switch_to_alert().text
    assert "I am a JS Confirm" == alert_text, "Текст алерта не совпадает"
    alert.accept_alert()
    text = driver.get_text(alert.RESULT_LOC)
    assert "You clicked: Ok" == text, "Текст не совпадает"

    alert.prompt.click((By.XPATH, alert.JS_PROMPT_LOC))
    alert_text = driver.switch_to_alert().text
    assert "I am a JS prompt" == alert_text, "Текст алерта не совпадает"
    driver.alert_send_keys("done")
    text = driver.get_text(alert.RESULT_LOC)
    assert "You entered: done" == text, "Текст не совпадает"


@pytest.mark.parametrize("driver", ["chrome"], indirect=True)
def test_alerts_and_js(driver):
    driver.get(url="https://the-internet.herokuapp.com/javascript_alerts")
    alert = Alerts(driver)
    driver.execute_script("""
            document.querySelectorAll('button').forEach(function(button) {
                if (button.textContent.includes("Click for JS Alert")) {
                    button.click();
                }
            });
        """)
    alert.accept_alert()
    alert.wait_for_open(alert.RESULT_LOC)
    text = driver.get_text(alert.RESULT_LOC)
    assert "You successfully clicked an alert" == text, "Текст не совпадает"

    driver.find_element(By.XPATH, alert.JS_CONFIRM_LOC)
    time.sleep(2)
    driver.execute_script("""
                document.querySelectorAll('button').forEach(function(button) {
                    if (button.textContent.includes("Click for JS Confirm")) {
                        button.click();
                    }
                });
            """)
    time.sleep(2)
    driver.switch_to_alert()
    alert.accept_alert()
    alert.wait_for_open(alert.RESULT_LOC)
    text = driver.get_text(alert.RESULT_LOC)
    assert "You clicked: Ok" == text, "Текст не совпадает"

    driver.execute_script("""
        window.prompt = function(message, defaultValue) { return 'done'; };
    """)
    driver.execute_script("""
        document.querySelectorAll('button').forEach(function(button) {
            if (button.textContent.includes("Click for JS Prompt")) {
                button.click();
            }
        });
    """)
    text = driver.find_element(By.XPATH, alert.RESULT_LOC).text
    assert "You entered: done" == text, "Текст не совпадает"
