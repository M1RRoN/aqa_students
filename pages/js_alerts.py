from elements.button import Button
from elements.label import Label
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
        self.button = Button(self.driver, locator=self.BUTTON_JAVASCRIPT_ALERTS_LOC,
                             description="Main page -> JavaScript Alerts page")
        self.result = Label(self.driver, locator=self.RESULT_LOC, description="Alert result")

    def switch_and_accept_alert(self):
        self.driver.wait_alert()
        alert = self.driver.switch_to_alert()
        alert.accept()

    def click_on_js_button(self):
        self.alert.click()

    def click_on_confirm_button(self):
        self.confirm.click()

    def click_on_prompt_button(self):
        self.prompt.click()

    def get_alert_text_on_page(self):
        text = self.driver.get_alert_text()
        return text

    def get_result_text(self):
        text = self.result.get_text()
        return text

    def send_keys_in_alert_and_accept(self):
        self.driver.alert_send_keys("done")

    def switch_to_alert(self):
        self.driver.switch_to_alert()
