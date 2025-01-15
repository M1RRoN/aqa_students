from elements.button import Button
from elements.web_element import WebElement
from pages.base_page import BasePage


class ContextMenuPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='hot-spot']"

    BUTTON_CONTEXT_MENU_LOC = "//*[@id='content']//a[contains(text(), 'Context Menu')]"

    def __init__(self, driver):
        super().__init__(driver)
        self.name = "context_menu"
        self.button = Button(driver, "Main page -> Context Menu page", self.BUTTON_CONTEXT_MENU_LOC)

        self.hot_spot = WebElement(driver, "hot-spot for alert", self.UNIQUE_ELEMENT_LOC)
