from selenium.webdriver.common.by import By

from elements.button import Button
from custom_elements.slider import Slider
from pages.base_page import BasePage


class HorizontalSliderPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='content']//input[@type='range']"

    SLIDER_LOC = "//*[@id='content']//input[@type='range']"
    SLIDER_RANGE_LOC = "//*[@id='range']"
    BUTTON_HORIZONTAL_SLIDER_LOC = "//*[@id='content']//a[contains(text(), 'Horizontal Slider')]"

    def __init__(self, driver):
        super().__init__(driver)
        self.name = "horizontal_slider"

        self.slider = Slider(driver, self.SLIDER_LOC, "Slider")

    def scroll_slider_to_value(self, target_value):
        self.slider.scroll_slider(target_value)

    def get_slider_value(self):
        slider = self.driver.find_element(By.XPATH, self.SLIDER_RANGE_LOC)
        return float(slider.text)

    def get_slider_attributes(self):
        attr = self.slider.get_slider_attributes()
        return attr
