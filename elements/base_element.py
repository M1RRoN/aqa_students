import logging

from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.config_reader import ConfigReader


class BaseElement:
    def __init__(self, driver, description: str, locator: str):
        self.driver = driver
        self.timeout = ConfigReader().get("timeout")
        self.description = description
        self.locator = locator
        self.logger = logging.getLogger(__name__)

    def find_element(self, by, locator):
        try:
            element = WebDriverWait(self.driver.driver, self.timeout).until(
                EC.presence_of_element_located((by, locator))
            )
            return element
        except NoSuchElementException:
            print(f"Element with locator: {locator} not found.")
            return None

    def find_elements_with_explicit_wait(self, locator):
        self.logger.info("Find all elements")
        try:
            elements = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_all_elements_located(locator)
            )
            return elements
        except Exception as e:
            self.logger.error(f"Error while searching for elements: {e}")
            return []

    def click(self, locator: tuple[str, str]):
        try:
            self.logger.info(f"Waiting for element {self.description} to be clickable")
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable(locator)
            )
            self.logger.info(f"Clicking on element {self.description}")
            element.click()
        except Exception as e:
            self.logger.error(f"Failed to click on element {self.description}: {e}")
            raise

    def get_text(self, by, locator):
        element = WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located((by, locator))
        )
        return element.text

    def get_attribute(self):
        raise NotImplementedError("This method must be implemented in a subclass or later.")

    def is_enabled(self):
        raise NotImplementedError("This method must be implemented in a subclass or later.")

    def right_click(self):
        self.logger.info(f"Attempting to right-click on element: {self.description}")
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located((By.XPATH, self.locator))
            )
            actions = ActionChains(self.driver)
            actions.context_click(element).perform()
        except Exception as e:
            self.logger.error(f"Error during right-click on element {self.description}: {e}")
            raise

    def get_all_elements(self, driver, url, tag, attribute):
        self.logger.info("Open page using driver")
        driver.get(url)

        self.logger.info(f"Find all {tag} tags")
        elements = driver.find_elements(By.TAG_NAME, tag)

        attributes = []
        for element in elements:
            attr_value = element.get_attribute(attribute)
            if attr_value:
                attributes.append(attr_value)

        return attributes
