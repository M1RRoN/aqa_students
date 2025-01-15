import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.config_reader import ConfigReader


class BasePage:
    UNIQUE_ELEMENT_LOC = None

    JAVASCRIPT_ALERTS_LOC = "//a[@href='/javascript_alerts']"

    def __init__(self, browser):
        self.driver = browser
        self.timeout = ConfigReader().get("timeout")
        self.logger = logging.getLogger(__name__)

        self.button = None
        self.page_name = None
        self.unique_element = None

    def wait_for_open(self, locator):
        WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located((By.XPATH, locator))
        )

    def goto(self, by, locator):
        self.button.click((by, locator))
