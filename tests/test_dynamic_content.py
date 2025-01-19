import pytest

from browser.browser_factory import BrowserName
from config.config_reader import ConfigReader
from pages.dynamic_content import DynamicContentPage
from pages.main_page import MainPage


@pytest.mark.parametrize("driver", [browser for browser in BrowserName], indirect=True)
def test_dynamic_content(driver):
    dc = DynamicContentPage(driver)
    main_page = MainPage(driver)
    driver.get(ConfigReader().get("herokuapp_url"))
    main_page.go_to_dynamic_content_page()
    dc.wait_for_open()
    src_list = dc.refresh_page_while_not_find_identical_images()

    assert len(set(src_list)) < 3, "Не удалось найти два одинаковых изображения"
