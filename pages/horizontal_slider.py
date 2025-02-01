from custom_elements.slider import Slider
from pages.base_page import BasePage


class HorizontalSliderPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='content']//input[@type='range']"

    SLIDER_LOC = "//*[@id='content']//input[@type='range']"
    SLIDER_RANGE_LOC = "//*[@id='range']"
    BUTTON_HORIZONTAL_SLIDER_LOC = "//*[@id='content']//a[contains(text(), 'Horizontal Slider')]"

    def __init__(self, browser):
        super().__init__(browser)
        self.name = "horizontal_slider"

        self.slider = Slider(browser, self.SLIDER_LOC, "Slider")
        self.slider_range = Slider(browser, self.SLIDER_RANGE_LOC, "Slider range")


    def scroll_slider_to_value(self, target_value):
        self.slider.scroll_slider(target_value)

    def get_slider_value(self):
        slider = self.slider_range.visibility_of_element_located()
        return float(slider.text)

    def get_slider_attributes(self):
        attr = self.slider.get_slider_attributes()
        return attr
