import random

import pytest
from selenium.webdriver.common.by import By

from config.config_reader import ConfigReader
from pages.horizontal_slider import HorizontalSliderPage


@pytest.mark.parametrize("driver", ["chrome"], indirect=True)
def test_slider(driver):
    slider = HorizontalSliderPage(driver)
    driver.get(ConfigReader().get("herokuapp_url"))
    slider.goto(By.XPATH, slider.BUTTON_HORIZONTAL_SLIDER_LOC)

    min_value, max_value, step = slider.get_slider_attributes()
    target_value = round(random.uniform(min_value, max_value))
    slider.scroll_slider_to_value(target_value)
    current_value = slider.get_slider_value()

    assert current_value == target_value
