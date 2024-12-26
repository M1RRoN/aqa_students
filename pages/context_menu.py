from elements.web_element import WebElement
from pages.base_page import BasePage


class ContextMenu(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='hot-spot']"

    URL = "https://the-internet.herokuapp.com/context_menu"

    def __init__(self, driver):
        super().__init__(driver)
        self.name = "context_menu"

        self.wb = WebElement(driver, 10, "hot-spot for alert", self.UNIQUE_ELEMENT_LOC)
