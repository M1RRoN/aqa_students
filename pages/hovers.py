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

    def __init__(self, browser):
        super().__init__(browser)
        self.name = "hovers"

        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT_LOC, "Hovers page -> Unique element")
        self.profile = WebElement(browser, self.ALL_PROFILE_LOC, "Hovers page -> Profile")
        self.profile_link = WebElement(browser, self.PROFILE_LINK_LOC, "Hovers page -> Profile link")

    def view_profile(self, id: int):
        profile_locator = self.format_locator(self.PROFILE_LOC, id=id)
        profile_link_locator = self.format_locator(self.PROFILE_LINK_LOC, id=id)

        profile = WebElement(self.browser, profile_locator, f"Hovers page -> Profile {id}")
        profile_link = WebElement(self.browser, profile_link_locator, f"Hovers page -> Profile link {id}")

        avatar = profile.presence_of_element_located()
        actions = ActionChains(self.browser.driver)
        actions.move_to_element(avatar).perform()
        hover_link = profile_link.element_to_be_clickable()
        hover_link.click()

    def get_all_profiles(self):
        profiles = self.browser.presence_of_all_elements_located(self.profile.locator)
        return profiles

    def format_locator(self, locator_template, **kwargs):
        formatted_locator = locator_template.format(**kwargs)
        return By.XPATH, formatted_locator
