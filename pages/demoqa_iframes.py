from selenium.webdriver.common.by import By

from browser.browser import logger
from elements.web_element import WebElement
from pages.base_page import BasePage


class Iframes(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='frame1Wrapper']"

    MENU_FRAMES = "//*[@id='item-2']//span[contains(@class, 'text') and contains(text(), 'Frames')]"
    MENU_NESTED_FRAMES = "//*[@id='item-3']//span[contains(@class, 'text') and contains(text(), 'Nested Frames')]"
    PARENT_FRAME_LOC = "//*[@id='frame1']"
    CHILD_FRAME_LOC = "//iframe[@srcdoc='<p>Child Iframe</p>']"
    ALERTS_FRAME_WINDOWS_LOC = "//h5[contains(text(), 'Alerts, Frame & Windows')]"

    URL = "https://demoqa.com"

    TIMEOUT = 10

    def __init__(self, driver):
        super().__init__(driver)
        self.name = "iframes"

        self.unique_element = WebElement(self.driver, timeout=self.TIMEOUT, locator=self.UNIQUE_ELEMENT_LOC,
                                         description="iframes page -> iframe")

    def get_text_frame(self, locator):
        logger.info("Get frame text")
        text = self.driver.find_element(By.XPATH, locator).text
        return text
