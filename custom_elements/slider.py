from dataclasses import dataclass

from selenium.webdriver import ActionChains, Keys

from elements.base_element import BaseElement


@dataclass
class SliderAttributes:
    min_value: float
    max_value: float
    step: float


class Slider(BaseElement):
    def scroll_slider(self, move_offset):
        slider = self.presence_of_element_located()
        actions = ActionChains(self.driver)
        slider.send_keys(Keys.NULL)
        for _ in range(move_offset * 2):
            actions.send_keys(Keys.ARROW_RIGHT).perform()

    def get_slider_attributes(self):
        slider = self.visibility_of_element_located()
        min_value = float(slider.get_attribute("min"))
        max_value = float(slider.get_attribute("max"))
        step = float(slider.get_attribute("step"))
        return SliderAttributes(min_value=min_value, max_value=max_value, step=step)
