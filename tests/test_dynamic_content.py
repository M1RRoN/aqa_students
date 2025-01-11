import pytest

from pages.dynamic_content import DynamicContent


@pytest.mark.parametrize("driver", ["chrome"], indirect=True)
def test_dynamic_content(driver):
    dc = DynamicContent(driver)
    driver.get(dc.URL)
    src_list = driver.all_elements(dc.URL, "img", "src")[1:3]

    while len(set(src_list)) == 3:
        driver.refresh()
        src_list = driver.all_elements(dc.URL, "img", "src")

    assert len(set(src_list)) < 3, "Не удалось найти два одинаковых изображения"
