import pytest
from selenium.webdriver.common.by import By

from config.config_reader import ConfigReader
from pages.context_menu import ContextMenuPage


@pytest.mark.parametrize("driver", ["chrome"], indirect=True)
def test_context_menu(driver):
    menu = ContextMenuPage(driver)
    driver.get(url=ConfigReader().get("demoqa_url"))
    menu.goto(By.XPATH, menu.BUTTON_CONTEXT_MENU_LOC)

    menu.hot_spot.right_click()
    driver.alert_accept()
