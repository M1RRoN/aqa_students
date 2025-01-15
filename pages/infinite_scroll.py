from selenium.webdriver.common.by import By

from elements.button import Button
from elements.web_element import WebElement
from pages.base_page import BasePage


class InfiniteScrollPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='content']//h3[contains(text(), 'Infinite Scroll')]"

    BUTTON_INFINITE_SCROLL_LOC = "//*[@id='content']//a[contains(text(), 'Infinite Scroll')]"
    PARAGRAPH_LOC = "//*[@id='content']//div[contains(@class, 'jscroll-added')]"

    def __init__(self, driver, age):
        super().__init__(driver)
        self.name = "infinite_scroll"

        self.scroll = WebElement(driver, "Infinite scroll page -> scroll", self.UNIQUE_ELEMENT_LOC)
        self.button = Button(self.driver, "Main page -> Infinite Scroll page", self.BUTTON_INFINITE_SCROLL_LOC)
        self.age = age

    def scroll_to_paragraph(self):
        paragraphs = self.driver.find_elements(By.XPATH, self.PARAGRAPH_LOC)

        while len(paragraphs) < self.age:
            self.logger.info(f"Current paragraph count: {len(paragraphs)}. Target: {self.age}")
            last_paragraph = paragraphs[-1]
            self.driver.execute_script("arguments[0].scrollIntoView(true);", last_paragraph)
            paragraphs = self.driver.find_elements(By.XPATH, self.PARAGRAPH_LOC)

        self.logger.info(f"Scrolled to {len(paragraphs)} paragraphs!")
        return paragraphs
