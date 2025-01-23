from browser.browser import logger
from elements.web_element import WebElement
from pages.base_page import BasePage


class InfiniteScrollPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='content']//h3[contains(text(), 'Infinite Scroll')]"

    PARAGRAPH_LOC = "//*[@id='content']//div[contains(@class, 'jscroll-added')]"

    def __init__(self, browser, age):
        super().__init__(browser)
        self.name = "infinite_scroll"

        self.scroll = WebElement(browser, self.UNIQUE_ELEMENT_LOC, "Infinite scroll page -> scroll")
        self.paragraph = WebElement(browser, self.PARAGRAPH_LOC, "Infinite scroll page -> paragraph")

    def scroll_to_paragraph(self, age):
        paragraphs = self.browser.presence_of_all_elements_located(self.paragraph.locator)

        while len(paragraphs) < age:
            self.paragraph.scroll_into_view(True)
            paragraphs = self.browser.presence_of_all_elements_located(self.paragraph.locator)

        logger.info(f"Scrolled to {len(paragraphs)} paragraphs!")
        return paragraphs
