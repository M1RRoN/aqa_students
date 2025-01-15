import pytest
from selenium.webdriver.common.by import By

from config.config_reader import ConfigReader
from pages.infinite_scroll import InfiniteScrollPage


@pytest.mark.parametrize("driver", ["chrome"], indirect=True)
def test_infinite_scroll(driver):
    scroll = InfiniteScrollPage(driver, 30)
    driver.get(ConfigReader().get("herokuapp_url"))
    scroll.goto(By.XPATH, scroll.BUTTON_INFINITE_SCROLL_LOC)
    paragraphs = scroll.scroll_to_paragraph()

    assert len(paragraphs) == scroll.age, f"Expected {scroll.age}, Actual {len(paragraphs)}"
