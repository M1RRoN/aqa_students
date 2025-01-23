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
            raise

    def presence_of_element_located(self):
        try:
            elements = WebDriverWait(self.browser.driver, self.timeout).until(
                EC.presence_of_element_located(self.locator)
            )
            return elements
        except TimeoutException:
            self.logger.error(f"Timeout while waiting for element with locator: {self.locator}")
            raise

    def element_to_be_clickable(self):
        try:
            elements = WebDriverWait(self.browser.driver, self.timeout).until(
                EC.element_to_be_clickable(self.locator)
            )
            return elements
        except TimeoutException:
            self.logger.error(f"Timeout while waiting for element with locator: {self.locator}")
            raise

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
        element = self.visibility_of_element_located()
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

    def scroll_into_view(self, align_to_top):
        elements = self.browser.presence_of_all_elements_located(self.locator)
        last_element = elements[-1]
        align = str(align_to_top).lower()
        self.browser.driver.execute_script(f"arguments[0].scrollIntoView({align});", last_element)

    def is_exists(self) -> bool:
        print(self.locator)
        for i in list(self.locator):
            print(i)
            elements = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located(i)
            )
            if elements:
                return True
            else:
                return False

    def get_elements_by_locator(self):
        return self.browser.presence_of_all_elements_located(self.locator)
