from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from browser.browser import logger
from selenium.webdriver.support import expected_conditions as EC


class BaseElement:
    def __init__(self, driver, timeout: int, description: str, locator: str):
        self.driver = driver
        self.timeout = timeout
        self.description = description
        self.locator = locator

    def click(self, locator: tuple[str, str]):
        try:
            logger.info(f"Waiting for element {self.description} to be clickable")
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable(locator)
            )
            logger.info(f"Clicking on element {self.description}")
            element.click()
        except Exception as e:
            logger.error(f"Failed to click on element {self.description}: {e}")
            raise

    def get_text(self, locator):
        element = WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located((By.XPATH, locator))
        )
        return element.text

    def get_attribute(self):
        pass

    def is_enables(self):
        pass

    def wait_alert(self):
        logger.info(f"Waiting for alert to appear with timeout {self.timeout} seconds")
        try:
            alert = WebDriverWait(self.driver, self.timeout).until(EC.alert_is_present())
            logger.info("Alert is present")
            return alert
        except Exception as e:
            logger.error(f"Alert did not appear: {e}")
            raise

    def right_click(self):
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.XPATH, self.locator))
            )
            actions = ActionChains(self.driver)
            actions.context_click(element).perform()
        except Exception as e:
            print(f"Ошибка при выполнении right_click: {e}")
