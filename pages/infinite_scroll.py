from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from elements.web_element import WebElement
from pages.base_page import BasePage


class InfiniteScroll(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='content']//h3[contains(text(), 'Infinite Scroll')]"

    URL = "https://the-internet.herokuapp.com/infinite_scroll"

    def __init__(self, driver, age):
        super().__init__(driver)
        self.name = "infinite_scroll"

        self.scroll = WebElement(driver, 10, "Infinite scroll page -> scroll", self.UNIQUE_ELEMENT_LOC)
        self.age = age

    def scroll_on_page(self):
        ActionChains(self.driver).scroll_by_amount(0, 500).perform()

    def find_paragraphs(self):
        paragraphs = self.driver.find_elements_with_explicit_wait(
            (By.XPATH, "//*[@id='content']//div[contains(@class, 'jscroll-added')]"))
        return paragraphs
