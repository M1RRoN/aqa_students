from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.language_enum import Language
from pages.base_page import BasePage


class MainPage(BasePage):
    SEARCH_INPUT = (By.ID, "store_nav_search_term")
    SEARCH_BUTTON = (By.XPATH, "//*[@id='store_search_link']//img")
    HTML = (By.XPATH, f"//html")
    SET_LANGUAGE_BUTTON = (By.ID, "language_pulldown")
    CHOOSE_LANGUAGE_BUTTON = (By.XPATH, "//div[@id='language_dropdown']//a[contains(@onclick, 'ChangeLanguage')"
                                        " and contains(@onclick, 'Language.{lang_enum}')][1]")

    def search_on_main_page(self, game_name):
        WebDriverWait(self.driver, self.wait).until(EC.visibility_of_element_located(self.SEARCH_INPUT)).send_keys(
            game_name)
        WebDriverWait(self.driver, self.wait).until(EC.element_to_be_clickable(self.SEARCH_BUTTON)).click()

    def get_language(self):
        html_lang = WebDriverWait(self.driver, self.wait).until(
            EC.visibility_of_element_located(self.HTML)).get_attribute("lang")
        return Language(html_lang)

    def click_on_language_button(self):
        WebDriverWait(self.driver, self.wait).until(EC.element_to_be_clickable(self.SET_LANGUAGE_BUTTON)).click()

    def set_new_language(self, lang_enum: Language):
        format_xpath = (self.CHOOSE_LANGUAGE_BUTTON[0], self.CHOOSE_LANGUAGE_BUTTON[1].format(lang_enum=lang_enum))
        WebDriverWait(self.driver, self.wait).until(EC.element_to_be_clickable(format_xpath))
