from selenium.webdriver.common.by import By

from pages.base_page import BasePage

SEARCH_INPUT_IN_SEARCH_PAGE = (By.ID, "term")
SEARCH_RESULT_CONTAINER = (By.ID, "search_result_container")
SORTING = (By.ID, "sort_by_trigger")
SORT_PRICE_DESC = (By.ID, "Price_DESC")
WAIT = 10


class ResultSearch(BasePage):
    def text_input(self):
        element = self.find_visibility_element(SEARCH_INPUT_IN_SEARCH_PAGE, WAIT)
        return element.get_attribute("value")

    def sorted_results_price_desc(self):
        self.find_clickable_element(SORTING, WAIT).click()
        self.find_clickable_element(SORT_PRICE_DESC, WAIT)

    def get_n_games(self, quantity):
        list_games = self.find_elements((By.XPATH, f"//div[@id='search_resultsRows']//a[position() <= {quantity}]"), WAIT)
        return list_games[:quantity]
