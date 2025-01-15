import pytest
from selenium.webdriver.common.by import By

from config.config_reader import ConfigReader
from pages.dynamic_content import DynamicContentPage


@pytest.mark.parametrize("driver", ["chrome"], indirect=True)
def test_dynamic_content(driver):
    dc = DynamicContentPage(driver)
    driver.get(ConfigReader().get("herokuapp_url"))
    dc.goto(By.XPATH, dc.BUTTON_DYNAMIC_CONTENT_LOC)
    current_url = driver.get_current_url()
    src_list = driver.all_elements(current_url, "img", "src")[1:3]

    while len(set(src_list)) == 3:
        driver.refresh()
        src_list = driver.all_elements(current_url, "img", "src")

    assert len(set(src_list)) < 3, "Не удалось найти два одинаковых изображения"
