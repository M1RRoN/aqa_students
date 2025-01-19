from browser.browser import logger
from elements.web_element import WebElement
from pages.base_page import BasePage


class InfiniteScrollPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='content']//h3[contains(text(), 'Infinite Scroll')]"

    PARAGRAPH_LOC = "//*[@id='content']//div[contains(@class, 'jscroll-added')]"

    def __init__(self, driver, age):
        super().__init__(driver)
        self.name = "infinite_scroll"

        self.scroll = WebElement(driver, self.UNIQUE_ELEMENT_LOC, "Infinite scroll page -> scroll")
        self.paragraph = WebElement(driver, self.PARAGRAPH_LOC, "Infinite scroll page -> paragraph")

    def scroll_to_paragraph(self, age):
        paragraphs = self.paragraph.presence_of_all_elements_located()

        while len(paragraphs) < age:
            last_paragraph = paragraphs[-1]
            self.paragraph.scroll_into_view(last_paragraph)
            paragraphs = self.paragraph.presence_of_all_elements_located()

        logger.info(f"Scrolled to {len(paragraphs)} paragraphs!")
        return paragraphs
