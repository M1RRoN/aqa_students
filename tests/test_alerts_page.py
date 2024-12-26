import time

from selenium.webdriver.common.by import By

from pages.js_alerts import Alerts


def test_accept_alert(driver):
    driver.get(url="https://the-internet.herokuapp.com/javascript_alerts")
    alert = Alerts(driver)
    alert.unique_element.click((By.XPATH, alert.UNIQUE_ELEMENT_LOC))
    alert_text = driver.switch_to_alert().text
    assert "I am a JS Alert" == alert_text
    alert.accept_alert()
    text = driver.get_text(alert.RESULT_LOC)
    assert "You successfully clicked an alert" == text

    alert.confirm.click((By.XPATH, alert.JS_CONFIRM_LOC))
    alert_text = driver.switch_to_alert().text
    assert "I am a JS Confirm" == alert_text
    alert.accept_alert()
    text = driver.get_text(alert.RESULT_LOC)
    assert "You clicked: Ok" == text

    alert.prompt.click((By.XPATH, alert.JS_PROMPT_LOC))
    alert_text = driver.switch_to_alert().text
    assert "I am a JS prompt" == alert_text
    driver.alert_send_keys("done")
    text = driver.get_text(alert.RESULT_LOC)
    assert "You entered: done" == text


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
    assert "You successfully clicked an alert" == text

    driver.find_element(By.XPATH, alert.JS_CONFIRM_LOC)
    driver.execute_script("""
                document.querySelectorAll('button').forEach(function(button) {
                    if (button.textContent.includes("Click for JS Confirm")) {
                        button.click();
                    }
                });
            """)
    time.sleep(2)
    driver.switch_to_alert()
    driver.execute_script(script="window.confirm = function() { return true; }")
    alert.accept_alert()
    alert.wait_for_open(alert.RESULT_LOC)
    text = driver.get_text(alert.RESULT_LOC)
    assert "You clicked: Ok" == text

    driver.find_element(By.XPATH, alert.JS_PROMPT_LOC)
    driver.execute_script(script="window.prompt = function(message, defaultValue) { return 'done'; }")
    text = driver.get_text(alert.RESULT_LOC)
    assert "You entered: done" == text
