from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from elements.button import Button
from elements.web_element import WebElement
from pages.base_page import BasePage


class HoversPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='content']//h3[contains(text(), 'Hovers')]"

    PROFILE_LOC = "//*[@id='content']//div[contains(@class, 'figure')][{id}]"
    FIRST_PROFILE_LOC = "//*[@id='content']//div[contains(@class, 'figure')][1]"
    PROFILE_LINK = "//*[@id='content']//div[contains(@class, 'figcaption')]//a[contains(@href, '/users/{id}')]"
    BUTTON_HOVERS_PAGE_LOC = "//*[@id='content']//a[contains(text(), 'Hovers')]"

    def __init__(self, driver):
        super().__init__(driver)
        self.name = "hovers"

        self.unique_element = WebElement(self.driver, "Hovers page -> Profile", self.UNIQUE_ELEMENT_LOC,)
        self.button = Button(self.driver, "Button Hovers", self.BUTTON_HOVERS_PAGE_LOC)

    def view_profile(self, id: int):
        avatar = self.driver.find_element(By.XPATH, self.PROFILE_LOC.format(id=id))
        actions = ActionChains(self.driver)
        actions.move_to_element(avatar).perform()
        hover_link = self.driver.find_element(By.XPATH, self.PROFILE_LINK.format(id=id))
        hover_link.click()
