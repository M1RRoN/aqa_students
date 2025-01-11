import requests
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import logging

from selenium.webdriver.support.wait import WebDriverWait

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class Browser:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get(self, url):
        logger.info("Open page")
        self.driver.get(url)
        WebDriverWait(self.driver, 10).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

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
        logger.info("Getting current URL")
        return self.driver.current_url

    def switch_to_alert(self):
        logger.info(f"Switching to alert")
        return self.driver.switch_to.alert

    def alert_send_keys(self, *args):
        alert = self.switch_to_alert()
        logger.info(f"Sending keys in alert: {args}")
        for arg in args:
            alert.send_keys(arg)
        alert.accept()

    def wait_for_alert(self, timeout=10):
        logger.info(f"Waiting for alert to appear with timeout {timeout} seconds")
        try:
            WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
            logger.info("Alert is present")
        except Exception as e:
            logger.error(f"Alert did not appear: {e}")

    def find_element(self, by, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((by, locator))
            )
            return element
        except NoSuchElementException:
            print(f"Element with locator: {locator} not found.")
            return None

    def alert_accept(self):
        logger.info("Accept alert")
        try:
            self.wait_for_alert()
            alert = self.switch_to_alert()
            alert.accept()
            logger.info("Alert successfuly accept")
        except Exception as e:
            logger.error(f"Alert did not accept: {e}")

    def get_text(self, locator, timeout=10):
        logger.info(f"Get element text")
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((By.XPATH, locator))
            )
            return element.text
        except Exception as e:
            logger.error(f"Alert did not accept: {e}")

    def execute_script(self, script: str, *args):
        try:
            logging.info(f"Executing script: {script} with arguments: {args}")

            return self.driver.execute_script(script, *args)
        except Exception as e:
            logging.error(f"Error executing script: {e}")
            raise

    def execute(self, command, params):
        return self.driver.execute(command, params)

    def back(self):
        self.driver.back()

    def switch_to_frame(self, frame_loc):
        logger.info("Switch to frame")
        frame = self.driver.find_element(By.XPATH, frame_loc)
        self.driver.switch_to.frame(frame)

    def all_elements(self, url, tag, attribute):
        logger.info("Send request")
        response = requests.get(url)
        attributes = []

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            logger.info("Find tags")
            images = soup.find_all(tag)
            for img in images:
                attributes.append(img.get(attribute))
            return attributes
        else:
            logger.error(f"Error: {response.status_code}")

    def page_source(self):
        logger.info("Get HTML")
        return self.execute_script("return document.documentElement.outerHTML")

    def find_elements_with_explicit_wait(self, locator, timeout=10):
        logger.info("Find all elements")
        try:
            elements = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located(locator)
            )
            return elements
        except Exception as e:
            logger.error(f"Ошибка при поиске элементов: {e}")
            return []
