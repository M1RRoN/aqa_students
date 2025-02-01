from browser.browser import logger
from elements.multi_web_element import MultiWebElement
from elements.web_element import WebElement
from pages.base_page import BasePage


class InfiniteScrollPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='content']//h3[contains(text(), 'Infinite Scroll')]"

    PARAGRAPH_LOC = "//*[@id='content']//div[contains(@class, 'jscroll-added')]"

    def __init__(self, browser):
        super().__init__(browser)
        self.name = "infinite_scroll"

        self.scroll = WebElement(browser, self.UNIQUE_ELEMENT_LOC, "Infinite scroll page -> scroll")
        self.paragraph = WebElement(browser, self.PARAGRAPH_LOC, "Infinite scroll page -> paragraph")

    def scroll_to_paragraph(self, age):
        """
        Вроде бы особых изменений не было, но теперь что-то очень медленно скроллить начало, примерно раз в 10-15 секунд,
        до этого было почти моментально на весm тест секунд 10,
        пробовал явное ожидание поменьше поставить, без изменений, может есть идеи почему так происходит?
        """
        lambda_xpath_locator = lambda x: f"({self.paragraph.locator[1]})[{x}]"
        paragraphs_multi = MultiWebElement(
            driver=self.browser,
            lambda_xpath_locator=lambda_xpath_locator,
            description="Paragraph elements"
        )
        paragraphs_count = paragraphs_multi.count()

        while paragraphs_count < age:
            last_paragraph = paragraphs_multi[paragraphs_count - 1]
            last_paragraph.scroll_into_view(align_to_top=True)

            paragraphs_count = paragraphs_multi.count()

        logger.info(f"Scrolled to {paragraphs_count} paragraphs!")
        return paragraphs_count
