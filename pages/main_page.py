from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class MainPage(BasePage):
    SEARCH_INPUT = (By.ID, "store_nav_search_term")
    SEARCH_BUTTON = (By.XPATH, "//a[@id='store_search_link']//img")
    HTML = (By.XPATH, f"//html")
    SET_LANGUAGE_BUTTON = (By.ID, "language_pulldown")

    def __init__(self, wait, base_url):
        super().__init__()
        self.wait = wait
        self.base_url = base_url

    def open_main_page(self):
        self.driver.get(self.base_url)

    def search_on_main_page(self, game_name):
        WebDriverWait(self.driver, self.wait).until(EC.visibility_of_element_located(self.SEARCH_INPUT)).send_keys(game_name)
        WebDriverWait(self.driver, self.wait).until(EC.element_to_be_clickable(self.SEARCH_BUTTON)).click()

    def get_language(self):
        html_lang = WebDriverWait(self.driver, self.wait).until(EC.visibility_of_element_located(self.HTML)).get_attribute("lang")
        return html_lang

    def click_on_language_button(self):
        WebDriverWait(self.driver, self.wait).until(EC.element_to_be_clickable(self.SET_LANGUAGE_BUTTON)).click()

    def set_new_language(self, lang_enum_value):
        language_xpath = (By.XPATH, f"//div[@id='language_dropdown']//a[contains(@onclick, 'ChangeLanguage') and contains(@onclick, '{lang_enum_value}')][1]")
        WebDriverWait(self.driver, self.wait).until(EC.element_to_be_clickable(language_xpath))

    def wait_for_open(self):
        assert self.driver.execute_script("return document.readyState") == "complete", \
            (f"Страница не загрузилась полностью. "
             f"Получено: {self.driver.execute_script('return document.readyState')}, ожидаемо: 'complete'")
