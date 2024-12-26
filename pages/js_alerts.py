from elements.button import Button
from pages.base_page import BasePage


class Alerts(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='content']//button[@onclick='jsAlert()']"

    JS_CONFIRM_LOC = "//*[@id='content']//button[@onclick='jsConfirm()']"
    JS_PROMPT_LOC = "//*[@id='content']//button[@onclick='jsPrompt()']"
    RESULT_LOC = "//*[@id='result']"

    TIMEOUT = 10

    def __init__(self, driver):
        super().__init__(driver)
        self.name = "js_alerts"

        self.unique_element = Button(self.driver, timeout=self.TIMEOUT, locator=self.UNIQUE_ELEMENT_LOC,
                                     description="JS alerts page -> Alerts button")
        self.confirm = Button(self.driver, timeout=self.TIMEOUT, locator=self.JS_CONFIRM_LOC,
                              description="JS alerts page -> Confirm button")
        self.prompt = Button(self.driver, timeout=self.TIMEOUT, locator=self.JS_PROMPT_LOC,
                             description="JS alerts page -> Prompt button")

    def accept_alert(self):
        self.driver.wait_for_alert()
        alert = self.driver.switch_to_alert()
        alert.accept()
