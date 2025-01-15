from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from elements.button import Button
from pages.base_page import BasePage


class BasicAuthPage(BasePage):
    UNIQUE_LOC = "//*[@id='content']//h3[contains(text(), 'Basic Auth')]"

    BUTTON_BASIC_AUTH_LOC = "//*[@id='content']//a[contains(text(), 'Basic Auth')]"
    RESULT_LOC = "//*[@id='content']//p"

    def __init__(self, driver):
        super().__init__(driver)
        self.name = "basic_auth"
        self.button = Button(driver, "Main page -> Basic Auth page", self.BUTTON_BASIC_AUTH_LOC)

    def login(self, username: str, password: str):
        """

        этот код не работает, селениум не видит алерт, архитектуру оставлю, но решение кажется здесь толька авторизация через урл

        """
        self.logger.info("Waiting for login alert to appear")
        WebDriverWait(self.driver, self.timeout).until(EC.alert_is_present())
        alert = self.driver.switch_to_alert()

        self.logger.info("Login alert appeared, sending credentials using ActionChains")

        alert.send_keys(f"{username}{Keys.TAB}{password}")
        alert.accept()
        self.logger.info("Credentials sent, accepting alert")
        self.driver.alert_accept()
