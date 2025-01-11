from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    UNIQUE_ELEMENT_LOC = None

    JAVASCRIPT_ALERTS_LOC = "//a[@href='/javascript_alerts']"

    def __init__(self, browser):
        self.driver = browser

        self.page_name = None
        self.unique_element = None

    def wait_for_open(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, locator))
        )
