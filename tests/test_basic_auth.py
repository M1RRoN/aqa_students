import pytest
from selenium.webdriver.common.by import By

from config.config_reader import ConfigReader
from pages.basic_auth import BasicAuthPage


@pytest.mark.parametrize("driver", ["chrome"], indirect=True)
def test_basic_auth(driver):
    driver.get(url=ConfigReader().get("herokuapp_url"))
    alert = BasicAuthPage(driver)
    alert.goto(By.XPATH, alert.button.locator)
    alert.login("admin", "admin")
    elem_text = driver.find_element(By.XPATH, alert.RESULT_LOC).text

    assert "Congratulations! You must have the proper credentials." == elem_text
