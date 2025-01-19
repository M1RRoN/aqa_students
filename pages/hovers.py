from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from elements.web_element import WebElement
from pages.base_page import BasePage


class HoversPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='content']//h3[contains(text(), 'Hovers')]"

    PROFILE_LOC = "//*[@id='content']//div[contains(@class, 'figure')][{id}]"
    ALL_PROFILE_LOC = "//*[@id='content']//div[contains(@class, 'figure')]"
    FIRST_PROFILE_LOC = "//*[@id='content']//div[contains(@class, 'figure')][1]"
    PROFILE_LINK_LOC = "//*[@id='content']//div[contains(@class, 'figcaption')]//a[contains(@href, '/users/{id}')]"
    BUTTON_HOVERS_PAGE_LOC = "//*[@id='content']//a[contains(text(), 'Hovers')]"

    def __init__(self, driver):
        super().__init__(driver)
        self.name = "hovers"

        self.unique_element = WebElement(self.driver, self.UNIQUE_ELEMENT_LOC, "Hovers page -> Unique element")
        self.profile = WebElement(driver, self.ALL_PROFILE_LOC, "Hovers page -> Profile")
        self.profile_link = WebElement(driver, self.PROFILE_LINK_LOC, "Hovers page -> Profile link")

    def view_profile(self, id: int):
        original_locator = self.profile.locator
        original_profile_link_locator = self.profile_link.locator
        try:
            self.profile.locator = (By.XPATH, self.PROFILE_LOC.format(id=id))
            self.profile_link.locator = (By.XPATH, self.PROFILE_LINK_LOC.format(id=id))
            avatar = self.profile.presence_of_element_located()
            actions = ActionChains(self.driver)
            actions.move_to_element(avatar).perform()
            hover_link = self.profile_link.element_to_be_clickable()
            hover_link.click()
        finally:
            self.profile.locator = original_locator
            self.profile_link.locator = original_profile_link_locator

    def return_from_profile_to_hover_page(self):
        self.driver.back()

    def get_current_url(self):
        url = self.driver.get_current_url()
        return url

    def get_all_profiles(self):
        original_locator = self.profile.locator
        try:
            self.profile.locator = (By.XPATH, self.ALL_PROFILE_LOC)

            return self.profile.presence_of_all_elements_located()
        finally:
            self.profile.locator = original_locator
