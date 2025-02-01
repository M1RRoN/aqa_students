import random

import pytest

from browser.browser_factory import BrowserName
from config.config_reader import ConfigReader
from pages.horizontal_slider import HorizontalSliderPage
from pages.main_page import MainPage


@pytest.mark.parametrize("driver", [browser for browser in BrowserName], indirect=True)
def test_slider(driver):
    main_page = MainPage(driver)
    slider = HorizontalSliderPage(driver)
    driver.get(ConfigReader().get("herokuapp_url"))
    main_page.go_to_horizontal_slider_page()

    slider_attributes = slider.get_slider_attributes()
    target_value = round(random.uniform(slider_attributes.min_value, slider_attributes.max_value))
    slider.scroll_slider_to_value(target_value)
    current_value = slider.get_slider_value()

    assert current_value == target_value, f"Expected: {current_value} Actual: {target_value}"
