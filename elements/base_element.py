import logging

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.config_reader import ConfigReader


class BaseElement:
    timeout = ConfigReader().get("timeout")

    def __init__(self, browser, locator, description: str):
        self.browser = browser
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
            element = WebDriverWait(self.browser.driver, self.timeout).until(
                EC.visibility_of_element_located(self.locator)
            )
            return element
        except TimeoutException:
            self.logger.error(f"Timeout while waiting for element with locator: {self.locator}")

    def presence_of_element_located(self):
        try:
            elements = WebDriverWait(self.browser.driver, self.timeout).until(
                EC.presence_of_element_located(self.locator)
            )
            return elements
        except NoSuchElementException:
            self.logger.info(f"Element with locator: {self.locator} not found.")

    def element_to_be_clickable(self):
        try:
            elements = WebDriverWait(self.browser.driver, self.timeout).until(
                EC.element_to_be_clickable(self.locator)
            )
            return elements
        except NoSuchElementException:
            self.logger.info(f"Element with locator: {self.locator} not found.")

    def click(self):
        try:
            self.logger.info(f"Waiting for button '{self.description}' to be clickable")
            element = self.element_to_be_clickable()
            self.logger.info(f"Clicking on button '{self.description}'")
            element.click()
        except TimeoutException:
            self.logger.error(f"Timeout while waiting for button '{self.description}' to be clickable")
            raise

    def get_text(self):
        element = WebDriverWait(self.browser.driver, self.timeout).until(
            EC.presence_of_element_located(self.locator)
        )
        return element.text

    def get_attribute(self, attribute):
        element = WebDriverWait(self.browser.driver, self.timeout).until(
            EC.visibility_of_element_located(self.locator)
        )
        return element.get_attribute(attribute)

    def right_click(self):
        self.logger.info(f"Attempting to right-click on element: {self.description}")
        try:
            element = WebDriverWait(self.browser.driver, self.timeout).until(
                EC.visibility_of_element_located(self.locator)
            )
            actions = ActionChains(self.browser.driver)
            actions.move_to_element(element)
            actions.context_click(element).perform()
        except TimeoutException:
            self.logger.error(f"Timeout while waiting for button '{self.description}' to be clickable")
            raise

    def scroll_into_view_to_last_element(self, align_to_top):
        elements = self.browser.presence_of_all_elements_located(self.locator)
        last_element = elements[-1]
        align = "true" if align_to_top else "false"
        self.browser.driver.execute_script(f"arguments[0].scrollIntoView({align});", last_element)
