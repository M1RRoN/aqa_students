from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import logging

from selenium.webdriver.support.wait import WebDriverWait

from config.config_reader import ConfigReader
from logger_config import setup_logger

setup_logger()


class Browser:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.timeout = ConfigReader().get("timeout")

    def __getattr__(self, name):
        if hasattr(self.driver, name):
            return getattr(self.driver, name)
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")

    def get(self, url):
        self.logger.info(f"Open page {url}")
        self.driver.get(url)
        WebDriverWait(self.driver, self.timeout).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

    def refresh(self):
        self.logger.info("Refresh current page")
        self.driver.refresh()

    def close(self):
        self.logger.info("Close current window")
        self.driver.close()

    def quit(self):
        self.logger.info("Quit browser session")
        self.driver.quit()

    def get_cookie(self, name):
        self.logger.info(f"Getting cookie {name}")
        self.driver.get_cookie(name)

    def add_cookie(self, cookie_dict):
        self.logger.info(f"Adding cookie: {cookie_dict}")
        self.driver.add_cookie(cookie_dict)

    def get_current_url(self):
        current_url = self.driver.current_url
        self.logger.info(f"Current URL: {current_url}")
        return current_url

    def switch_to_alert(self):
        self.logger.info(f"Switching to alert")
        WebDriverWait(self.driver, self.timeout).until(EC.alert_is_present())
        return self.driver.switch_to.alert

    def alert_send_keys(self, keys):
        alert = self.switch_to_alert()
        self.logger.info(f"Sending keys in alert: {keys}")
        alert.send_keys(keys)
        alert.accept()

    def wait_alert(self):
        self.logger.info(f"Waiting for alert to appear with timeout {self.timeout} seconds")
        try:
            WebDriverWait(self.driver, self.timeout).until(EC.alert_is_present())
        except Exception as e:
            self.logger.error(f"Alert did not appear: {e}")
            raise

    def alert_accept(self):
        self.logger.info("Accept alert")
        try:
            self.wait_alert()
            alert = self.switch_to_alert()
            alert.accept()
            self.logger.info("Alert successfuly accept")
        except Exception as e:
            self.logger.error(f"Alert did not accept: {e}")

    def execute_script(self, script: str, *args):
        try:
            self.logger.info(f"Executing script: {script} with arguments: {args}")

            return self.driver.execute_script(script, *args)
        except Exception as e:
            logging.error(f"Error executing script: {e}")
            raise

    def back(self):
        self.logger.info("Return to previous page")
        self.driver.back()

    def switch_to_frame(self, frame_element):
        self.logger.info("Switch to frame")
        frame = self.driver.find_element(By.XPATH, frame_element.locator)
        self.driver.switch_to.frame(frame)

    def get_page_source(self):
        self.logger.info("Get HTML source of the page")
        return self.driver.page_source

    def refresh_page(self):
        self.driver.refresh()
