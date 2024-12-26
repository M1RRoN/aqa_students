from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from elements.web_element import WebElement
from pages.base_page import BasePage


class Hovers(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='content']//h3[contains(text(), 'Hovers')]"

    PROFILE_LOC = "//*[@id='content']//div[contains(@class, 'figure')][{id}]"
    FIRST_PROFILE_LOC = "//*[@id='content']//div[contains(@class, 'figure')][1]"
    PROFILE_LINK = "//*[@id='content']//div[contains(@class, 'figcaption')]//a[contains(@href, '/users/{id}')]"
    URL = "https://the-internet.herokuapp.com/hovers"
    PROFILE_URL = "https://the-internet.herokuapp.com/users/{id}"

    TIMEOUT = 10

    def __init__(self, driver):
        super().__init__(driver)
        self.name = "hovers"

        self.unique_element = WebElement(self.driver, timeout=self.TIMEOUT, locator=self.FIRST_PROFILE_LOC,
                                     description="Hovers page -> Profile")

    def view_profile(self, id: int):
        avatar = self.driver.find_element(By.XPATH, self.PROFILE_LOC.format(id=id))
        actions = ActionChains(self.driver)
        actions.move_to_element(avatar).perform()
        hover_link = self.driver.find_element(By.XPATH, self.PROFILE_LINK.format(id=id))
        hover_link.click()
