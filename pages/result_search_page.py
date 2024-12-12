from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class ResultSearch(BasePage):
    SEARCH_INPUT_IN_SEARCH_PAGE = (By.ID, "term")
    SEARCH_RESULT_CONTAINER = (By.ID, "search_result_container")
    SORTING = (By.ID, "sort_by_trigger")
    SORT_PRICE_DESC = (By.ID, "Price_DESC")
    SEARCH_RESULTS_XPATH = (By.XPATH, "//*[@id='search_resultsRows']//a[position() <= {quantity}]")

    def input_text(self):
        element = WebDriverWait(self.driver, self.wait).until(
            EC.visibility_of_element_located(self.SEARCH_INPUT_IN_SEARCH_PAGE))
        return element.get_attribute("value")

    def sort_results_price_desc(self):
        WebDriverWait(self.driver, self.wait).until(EC.element_to_be_clickable(self.SORTING)).click()
        WebDriverWait(self.driver, self.wait).until(EC.element_to_be_clickable(self.SORT_PRICE_DESC))

    def get_n_games(self, quantity):
        formatted_xpath = (self.SEARCH_RESULTS_XPATH[0], self.SEARCH_RESULTS_XPATH[1].format(quantity=quantity))
        list_games = (WebDriverWait(self.driver, self.wait)
                      .until(EC.presence_of_all_elements_located(formatted_xpath)))
        return list_games

    def wait_visibility_container(self):
        return WebDriverWait(self.driver, self.wait).until(
            EC.visibility_of_element_located(self.SEARCH_RESULT_CONTAINER))
