from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from elements.base_element import BaseElement

class Input(BaseElement):
    def send_keys(self, keys: str):
        self.logger.info(f"Send keys to element: {self.description}")
        try:
            element = WebDriverWait(self.browser.driver, self.timeout).until(
                EC.visibility_of_element_located(self.locator)
            )
            element.send_keys(keys)
        except Exception as e:
            self.logger.error(f"Error sending keys to element {self.description}: {e}")
            raise

    def send_keys_into_hidden_input(self, keys: str):
        """
        Джаваскриптом не получилось, пробовал типа такого arguments[0].value = arguments[1];
        Но как я прочитал, браузеры такое поведение блокируют из за безопасности, по другому как просто это сделать не нашел
        """
        self.logger.info(f"Send keys to element: {self.description}")
        try:
            element = WebDriverWait(self.browser.driver, self.timeout).until(
                EC.presence_of_element_located(self.locator)
            )
            element.send_keys(keys)
        except Exception as e:
            self.logger.error(f"Error sending keys to element {self.description}: {e}")
            raise
    #
    # def send_keys_into_hidden_input(self, keys: str):
    #     self.logger.info(f"Send keys to hidden element: {self.description}")
    #     try:
    #         element = WebDriverWait(self.browser.driver, self.timeout).until(
    #             EC.presence_of_element_located(self.locator)
    #         )
    #         self.browser.driver.execute_script(
    #             "arguments[0].value = arguments[1];", element, keys
    #         )
    #         self.logger.info(f"Keys '{keys}' successfully sent to hidden input: {self.description}")
    #     except Exception as e:
    #         self.logger.error(f"Error sending keys to hidden input {self.description}: {e}")
    #         raise

