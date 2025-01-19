from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
import logging

from selenium.webdriver.support.wait import WebDriverWait

from config.config_reader import ConfigReader
from elements.web_element import WebElement
from logger_config import setup_logger

setup_logger()
logger = logging.getLogger(__name__)


class Browser:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.timeout = ConfigReader().get("timeout")

    def __getattr__(self, name):
        if hasattr(self.driver, name):
            return getattr(self.driver, name)
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")

    @property
    def selenium_driver(self):
        return self.driver

    def get(self, url):
        return self.selenium_driver.get(url)

    def refresh(self):
        logger.info("Refresh current page")
        self.driver.refresh()

    def close(self):
        logger.info("Close current window")
        self.driver.close()

    def quit(self):
        logger.info("Quit browser session")
        self.driver.quit()

    def get_cookie(self, name):
        logger.info(f"Getting cookie {name}")
        self.driver.get_cookie(name)

    def add_cookie(self, cookie_dict):
        logger.info(f"Adding cookie: {cookie_dict}")
        self.driver.add_cookie(cookie_dict)

    def get_current_url(self):
        current_url = self.driver.current_url
        logger.info(f"Current URL: {current_url}")
        return current_url

    def switch_to_alert(self):
        logger.info(f"Switching to alert")
        self.wait_alert()
        return self.driver.switch_to.alert

    def alert_send_keys(self, keys):
        alert = self.switch_to_alert()
        logger.info(f"Sending keys in alert: {keys}")
        alert.send_keys(keys)
        alert.accept()

    def wait_alert(self):
        logger.info(f"Waiting for alert to appear with timeout {self.timeout} seconds")
        try:
            WebDriverWait(self.driver, self.timeout).until(EC.alert_is_present())
        except Exception as e:
            logger.error(f"Alert did not appear: {e}")
            raise

    def alert_accept(self):
        logger.info("Accept alert")

        self.wait_alert()
        alert = self.switch_to_alert()
        alert.accept()
        logger.info("Alert successfuly accept")


    def execute_script(self, script: str, *args):
        try:
            logger.info(f"Executing script: {script} with arguments: {args}")

            return self.driver.execute_script(script, *args)
        except Exception as e:
            logging.error(f"Error executing script: {e}")
            raise

    def back(self):
        logger.info("Return to previous page")
        self.driver.back()

    def switch_to_frame(self, frame_element: WebElement):
        logger.info("Switch to frame")
        frame = frame_element.presence_of_element_located()
        self.driver.switch_to.frame(frame)

    def get_element_content(self, web_element):
        logger.info("Get innerHTML of the specified element")
        return web_element.get_attribute("innerHTML")

    def refresh_page(self):
        logger.info("Refresh current page")
        self.driver.refresh()

    def get_alert_text(self):
        alert = self.switch_to_alert()
        text = alert.text
        return text
