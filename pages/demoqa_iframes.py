from selenium.webdriver.common.by import By

from elements.button import Button
from elements.web_element import WebElement
from pages.base_page import BasePage


class IframesPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='frame1Wrapper']"

    MENU_FRAMES_LOC = "//*[@id='item-2']//span[contains(@class, 'text') and contains(text(), 'Frames')]"
    MENU_NESTED_FRAMES_LOC = "//*[@id='item-3']//span[contains(@class, 'text') and contains(text(), 'Nested Frames')]"
    PARENT_FRAME_LOC = "//*[@id='frame1']"
    CHILD_FRAME_LOC = "//iframe[@srcdoc='<p>Child Iframe</p>']"
    ALERTS_FRAME_WINDOWS_LOC = "//h5[contains(text(), 'Alerts, Frame & Windows')]"
    FRAME_BODY ="//body"

    def __init__(self, driver):
        super().__init__(driver)
        self.name = "iframes"
        self.button = Button(driver, "Main page -> Alerts, Frame & Windows page", self.ALERTS_FRAME_WINDOWS_LOC)
        self.button_nested_frames = Button(driver, "Alerts, Frame & Windows page -> Nested Frames page",
                                           self.MENU_NESTED_FRAMES_LOC)
        self.parent_frame = WebElement(driver, "Parent frame", self.PARENT_FRAME_LOC)
        self.child_frame = WebElement(driver, "Child_frame", self.CHILD_FRAME_LOC)

        self.unique_element = WebElement(self.driver, locator=self.UNIQUE_ELEMENT_LOC,
                                         description="iframes page -> iframe")

    def get_text_frame(self, frame):
        self.logger.info("Get frame text")
        text = frame.get_text(By.XPATH, self.FRAME_BODY)
        return text
