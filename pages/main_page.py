from selenium.webdriver.common.by import By

from pages.base_page import BasePage, BASE_URL

SEARCH_INPUT = (By.ID, "store_nav_search_term")
SEARCH_BUTTON = (By.XPATH, "//a[@id='store_search_link']//img")
WAIT = 10

class MainPage(BasePage):
    def open_main_page(self):
        self.driver.get(BASE_URL)

    def search_on_main_page(self, game_name):
        search_name = self.send_keys(SEARCH_INPUT, game_name, WAIT)
        search_button = self.find_clickable_element(SEARCH_BUTTON, WAIT).click()