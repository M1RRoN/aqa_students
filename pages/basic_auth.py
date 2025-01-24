import pyautogui

from elements.button import Button
from elements.label import Label
from pages.base_page import BasePage


class BasicAuthPage(BasePage):
    UNIQUE_LOC = "//*[@id='content']//h3[contains(text(), 'Basic Auth')]"

    BUTTON_BASIC_AUTH_LOC = "//*[@id='content']//a[contains(text(), 'Basic Auth')]"
    RESULT_LOC = "//*[@id='content']//p"

    def __init__(self, browser):
        super().__init__(browser)
        self.name = "basic_auth"
        self.button = Button(browser, self.BUTTON_BASIC_AUTH_LOC, "Main page -> Basic Auth page")
        self.result_after_auth = Label(self.browser, locator=self.RESULT_LOC, description="Alert result")

    def get_result_text(self):
        text = self.result_after_auth.get_text()
        return text

    def write_login_and_password_in_form(self, username, password):
        pyautogui.write(username)
        pyautogui.press("tab")

        pyautogui.write(password)
        pyautogui.press("enter")
