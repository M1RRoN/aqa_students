from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class ResultSearch(BasePage):
    SEARCH_INPUT_IN_SEARCH_PAGE = (By.ID, "term")
    SEARCH_RESULT_CONTAINER = (By.ID, "search_result_container")
    SORTING = (By.ID, "sort_by_trigger")
    SORT_PRICE_DESC = (By.ID, "Price_DESC")

    def __init__(self, wait, base_url):
        super().__init__()
        self.wait = wait
        self.base_url = base_url

    def text_input(self):
        element = WebDriverWait(self.driver, self.wait).until(EC.visibility_of_element_located(self.SEARCH_INPUT_IN_SEARCH_PAGE))
        return element.get_attribute("value")

    def sorted_results_price_desc(self):
        WebDriverWait(self.driver, self.wait).until(EC.element_to_be_clickable(self.SORTING)).click()
        WebDriverWait(self.driver, self.wait).until(EC.element_to_be_clickable(self.SORT_PRICE_DESC))

    def get_n_games(self, quantity):
        list_games = (WebDriverWait(self.driver, self.wait)
                      .until(EC.presence_of_all_elements_located((By.XPATH, f"//div[@id='search_resultsRows']//a[position() <= {quantity}]"))))
        return list_games[:quantity]

    def wait_for_open(self):
        assert self.driver.execute_script("return document.readyState") == "complete", \
            (f"Страница не загрузилась полностью. "
             f"Получено: {self.driver.execute_script('return document.readyState')}, ожидаемо: 'complete'")

    def visibility_container(self):
        return WebDriverWait(self.driver, self.wait).until(EC.visibility_of_element_located(self.SEARCH_RESULT_CONTAINER))
