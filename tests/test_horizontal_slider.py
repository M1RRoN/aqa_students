from pages.horizontal_slider import Slider


def test_slider(driver):
    slider = Slider(driver)
    driver.get(slider.URL)
    slider.scroll_slider(4)
    assert "2" == driver.get_text(slider.SLIDER_RANGE_LOC)
