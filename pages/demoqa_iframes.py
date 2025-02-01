from browser.browser import logger
from elements.button import Button
from elements.web_element import WebElement
from pages.base_page import BasePage


class IframesPage(BasePage):
    UNIQUE_ELEMENT_LOC = "frame1Wrapper"

    MENU_FRAMES_LOC = "//*[@id='item-2']//span[contains(@class, 'text') and contains(text(), 'Frames')]"
    MENU_NESTED_FRAMES_LOC = "//*[@id='item-3']//span[contains(@class, 'text') and contains(text(), 'Nested Frames')]"
    PARENT_FRAME_LOC = "frame1"
    CHILD_FRAME_LOC = "//iframe[@srcdoc='<p>Child Iframe</p>']"
    ALERTS_FRAME_WINDOWS_LOC = "//h5[contains(text(), 'Alerts, Frame & Windows')]"
    FRAME_BODY = "//body"

    def __init__(self, browser):
        super().__init__(browser)
        self.name = "iframes"
        self.button_nested_frames = Button(browser, self.MENU_NESTED_FRAMES_LOC,
                                           "Alerts, Frame & Windows page -> Nested Frames page")
        self.parent_frame = WebElement(browser, self.PARENT_FRAME_LOC, "Parent frame")
        self.child_frame = WebElement(browser, self.CHILD_FRAME_LOC, "Child_frame")

        self.unique_element = WebElement(browser, self.UNIQUE_ELEMENT_LOC,
                                         "iframes page -> iframe")
        self.frame_body = WebElement(browser, self.FRAME_BODY, "Frame body")

    def get_text_frame(self):
        logger.info("Get frame text")
        text = self.frame_body.get_text()
        return text

    def go_to_nested_frames(self):
        self.button_nested_frames.click()

    def switch_to_parent_frame(self):
        self.browser.switch_to_frame(self.parent_frame)

    def switch_to_child_frame(self):
        self.browser.switch_to_frame(self.child_frame)
