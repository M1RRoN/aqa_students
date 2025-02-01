import random

import pytest

from browser.browser_factory import BrowserName
from config.config_reader import ConfigReader
from pages.infinite_scroll import InfiniteScrollPage
from pages.main_page import MainPage


# @pytest.mark.parametrize("driver", [browser for browser in BrowserName], indirect=True)
# def test_infinite_scroll(driver):
#     main_page = MainPage(driver)
#     age = random.randint(18, 30)
#     scroll = InfiniteScrollPage(driver)
#     driver.get(ConfigReader().get("herokuapp_url"))
#     main_page.go_to_infinite_scroll_page()
#
#     paragraphs = scroll.scroll_to_paragraph(age)
#
#     assert paragraphs == age, f"Expected {age}, Actual {len(paragraphs)}"
