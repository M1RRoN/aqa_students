from selenium.webdriver.common.by import By

from elements.button import Button
from pages.base_page import BasePage


class AlertsPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='content']//button[@onclick='jsAlert()']"

    JS_ALERTS_LOC = "//*[@id='content']//button[@onclick='jsAlert()']"
    JS_CONFIRM_LOC = "//*[@id='content']//button[@onclick='jsConfirm()']"
    JS_PROMPT_LOC = "//*[@id='content']//button[@onclick='jsPrompt()']"
    RESULT_LOC = "//*[@id='result']"
    BUTTON_JAVASCRIPT_ALERTS_LOC = "//*[@id='content']//a[contains(text(), 'JavaScript Alerts')]"

    def __init__(self, driver):
        super().__init__(driver)
        self.name = "js_alerts"

        self.unique_element = Button(self.driver, locator=self.UNIQUE_ELEMENT_LOC,
                                     description="JS alerts page -> Alerts button")
        self.alert = Button(self.driver, locator=self.JS_ALERTS_LOC,
                                     description="JS alerts page -> Alerts button")
        self.confirm = Button(self.driver, locator=self.JS_CONFIRM_LOC,
                              description="JS alerts page -> Confirm button")
        self.prompt = Button(self.driver, locator=self.JS_PROMPT_LOC,
                             description="JS alerts page -> Prompt button")
        self.button = Button(self.driver, "Main page -> JavaScript Alerts page", self.BUTTON_JAVASCRIPT_ALERTS_LOC)

    def accept_alert(self):
        self.driver.wait_alert()
        alert = self.driver.switch_to_alert()
        alert.accept()

    def click_on_js_button(self):
        self.alert.click((By.XPATH, self.JS_ALERTS_LOC))
