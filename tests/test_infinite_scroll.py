import random

from config.config_reader import ConfigReader
from pages.infinite_scroll import InfiniteScrollPage
from pages.main_page import MainPage


def test_infinite_scroll(chrome_driver):
    main_page = MainPage(chrome_driver)
    age = random.randint(18, 30)
    scroll = InfiniteScrollPage(chrome_driver, age)
    chrome_driver.get(ConfigReader().get("herokuapp_url"))
    main_page.go_to_infinite_scroll_page()

    paragraphs = scroll.scroll_to_paragraph(age)

    assert len(paragraphs) == age, f"Expected {age}, Actual {len(paragraphs)}"
