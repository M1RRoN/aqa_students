import pytest

from elements.web_element import WebElement
from pages.context_menu import ContextMenu


@pytest.mark.parametrize("driver", ["chrome"], indirect=True)
def test_context_menu(driver):
    menu = ContextMenu(driver)
    wb = WebElement(driver, 10, "hot-spot for alert", menu.UNIQUE_ELEMENT_LOC)
    driver.get(menu.URL)
    wb.right_click()
    driver.alert_accept()
