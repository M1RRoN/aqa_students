from elements.button import Button
from elements.web_element import WebElement
from pages.base_page import BasePage


class ContextMenuPage(BasePage):
    UNIQUE_ELEMENT_LOC = "hot-spot"

    HOT_SPOT_LOC = "hot-spot"
    BUTTON_CONTEXT_MENU_LOC = "//*[@id='content']//a[contains(text(), 'Context Menu')]"

    def __init__(self, driver):
        super().__init__(driver)
        self.name = "context_menu"

        self.hot_spot = WebElement(driver, self.HOT_SPOT_LOC, "hot-spot for alert")

    def accept_alert_after_right_click(self):
        self.browser.alert_accept()

    def get_alert_text_after_right_click(self):
        text = self.browser.get_alert_text()
        return text

    def click_on_hot_spot(self):
        self.hot_spot.right_click()
