import time

import pytest

from pages.infinite_scroll import InfiniteScroll


@pytest.mark.parametrize("driver", ["chrome"], indirect=True)
def test_infinite_scroll(driver):
    scroll = InfiniteScroll(driver, 30)
    driver.get(scroll.URL)
    paragraphs = scroll.find_paragraphs()

    while len(paragraphs) < scroll.age:
        scroll.scroll_on_page()
        time.sleep(1)
        paragraphs = scroll.find_paragraphs()

    assert len(paragraphs) == scroll.age, f"Ожидалось {scroll.age}, а найдено {len(paragraphs)}"
