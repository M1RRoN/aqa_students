import pytest

from browser.browser_factory import BrowserName
from config.config_reader import ConfigReader
from pages.hovers import HoversPage
from pages.main_page import MainPage


@pytest.mark.parametrize("driver", [browser for browser in BrowserName], indirect=True)
def test_hovers(driver):
    main_page = MainPage(driver)
    hover_page = HoversPage(driver)
    driver.get(ConfigReader().get("herokuapp_url"))
    profile_url = ConfigReader().get("profile_url")
    main_page.go_to_hovers_page()

    profile_elements = hover_page.get_all_profiles()
    profile_count = profile_elements.count()

    for id in range(1, profile_count + 1):
        hover_page.view_profile(id)
        current_url = driver.get_current_url()
        expected_url = profile_url.format(id=id)
        assert profile_url.format(id=id) == current_url, f"Expected: {expected_url} Actual: {current_url}"
        driver.back()
