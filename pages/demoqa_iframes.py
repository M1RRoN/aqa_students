from browser.browser import logger
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
    FRAME_BODY = "//body"

    def __init__(self, driver):
        super().__init__(driver)
        self.name = "iframes"
        self.button_nested_frames = Button(driver, self.MENU_NESTED_FRAMES_LOC,
                                           "Alerts, Frame & Windows page -> Nested Frames page")
        self.parent_frame = WebElement(driver, self.PARENT_FRAME_LOC, "Parent frame")
        self.child_frame = WebElement(driver, self.CHILD_FRAME_LOC, "Child_frame")

        self.unique_element = WebElement(self.driver, self.UNIQUE_ELEMENT_LOC,
                                         "iframes page -> iframe")
        self.frame_body = WebElement(driver, self.FRAME_BODY, "Frame body")

    def get_text_frame(self):
        logger.info("Get frame text")
        text = self.frame_body.get_text()
        return text

    def go_to_nested_frames(self):
        self.button_nested_frames.click()

    def switch_to_parent_frame(self):
        self.driver.switch_to_frame(self.parent_frame)

    def switch_to_child_frame(self):
        self.driver.switch_to_frame(self.child_frame)
