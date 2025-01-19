import logging

from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.config_reader import ConfigReader


class BaseElement:
    def __init__(self, driver, locator, description: str):
        self.driver = driver
        self.timeout = ConfigReader().get("timeout")
        self.description = description
        self.logger = logging.getLogger(__name__)
        if isinstance(locator, str):
            if "/" in locator:
                self.locator = (By.XPATH, locator)
            else:
                self.locator = (By.ID, locator)
        else:
            self.locator = locator

    def visibility_of_element_located(self):
        try:
            elements = WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located(self.locator)
            )
            return elements
        except NoSuchElementException:
            self.logger.info(f"Element with locator: {self.locator} not found.")

    def presence_of_element_located(self):
        try:
            elements = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located(self.locator)
            )
            return elements
        except NoSuchElementException:
            self.logger.info(f"Element with locator: {self.locator} not found.")

    def presence_of_all_elements_located(self):
        try:
            elements = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_all_elements_located(self.locator)
            )
            return elements
        except NoSuchElementException:
            self.logger.info(f"Element with locator: {self.locator} not found.")

    def element_to_be_clickable(self):
        try:
            elements = WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable(self.locator)
            )
            return elements
        except NoSuchElementException:
            self.logger.info(f"Element with locator: {self.locator} not found.")

    def click(self):
        try:
            self.logger.info(f"Waiting for button '{self.description}' to be clickable")
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable(self.locator)
            )
            self.logger.info(f"Clicking on button '{self.description}'")
            element.click()
        except Exception as e:
            self.logger.error(f"Failed to click on button '{self.description}': {e}")
            raise

    def get_text(self):
        element = WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(self.locator)
        )
        return element.text

    def get_attribute(self, attribute):
        element = WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(self.locator)
        )
        return element.get_attribute(attribute)

    def right_click(self):
        self.logger.info(f"Attempting to right-click on element: {self.description}")
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located(self.locator)
            )
            actions = ActionChains(self.driver)
            actions.move_to_element(element)
            actions.context_click(element).perform()
        except Exception as e:
            self.logger.error(f"Error during right-click on element {self.description}: {e}")
            raise

    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
