from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from elements.web_element import WebElement
from pages.base_page import BasePage


class Slider(BasePage):
    UNIQUE_ELEMENT_LOC = "//input"

    SLIDER_RANGE_LOC = "//*[@id='range']"
    URL = "https://the-internet.herokuapp.com/horizontal_slider"

    def __init__(self, driver):
        super().__init__(driver)
        self.name = "horizontal_slider"

        self.slider = WebElement(driver, 10, "Slider", self.UNIQUE_ELEMENT_LOC)

    def scroll_slider(self, move_offset):
        slider = self.driver.find_element(By.XPATH, self.UNIQUE_ELEMENT_LOC)
        actions = ActionChains(self.driver)
        slider.send_keys(Keys.NULL)
        for _ in range(move_offset):
            actions.send_keys(Keys.ARROW_RIGHT).perform()
