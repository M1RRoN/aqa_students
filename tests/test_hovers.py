import pytest
from selenium.webdriver.common.by import By

from config.config_reader import ConfigReader
from pages.hovers import HoversPage


@pytest.mark.parametrize("driver", ["chrome"], indirect=True)
def test_hovers(driver):
    hover = HoversPage(driver)
    driver.get(ConfigReader().get("herokuapp_url"))
    profile_url = ConfigReader().get("profile_url")
    hover.goto(By.XPATH, hover.BUTTON_HOVERS_PAGE_LOC)
    for id in range(1, 4):
        hover.view_profile(id)
        current_url = driver.get_current_url()
        assert profile_url.format(id=id) == current_url, "Profile URL does not match the current one"
        driver.back()
