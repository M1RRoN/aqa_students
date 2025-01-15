from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from elements.base_element import BaseElement
import os

class Input(BaseElement):
    def send_keys(self, keys: str, locator: tuple):
        self.logger.info(f"Attempting to send keys to element: {self.description}")
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located(locator)
            )
            element.send_keys(keys)
            self.logger.info(f"Successfully sent keys to element: {self.description}")
        except Exception as e:
            self.logger.error(f"Error sending keys to element {self.description}: {e}")
            raise
