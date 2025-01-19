from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from elements.base_element import BaseElement

class Input(BaseElement):
    def send_keys(self, keys: str):
        self.logger.info(f"Attempting to send keys to element: {self.description}")
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located(self.locator)
            )
            element.send_keys(keys)
            self.logger.info(f"Successfully sent keys to element: {self.description}")
        except Exception as e:
            self.logger.error(f"Error sending keys to element {self.description}: {e}")
            raise
