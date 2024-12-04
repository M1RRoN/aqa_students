from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://store.steampowered.com/"

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, timeout):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def find_visibility_element(self, locator, timeout):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def find_clickable_element(self, locator, timeout):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def send_keys(self, locator, text, timeout):
       element = self.find_visibility_element(locator, timeout)
       element.send_keys(text)

    def find_elements(self, locator, timeout):
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )
        return self.driver.find_elements(*locator)
