from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.config_reader import ConfigReader


class BasePage:
    UNIQUE_ELEMENT_LOC = None
    timeout = ConfigReader().get("timeout")

    def __init__(self, browser):
        self.browser = browser

        self.page_name = None
        self.unique_element = None

    def wait_for_open(self):
        WebDriverWait(self.browser.driver, self.timeout).until(
            EC.presence_of_element_located(self.unique_element.locator)
        )
