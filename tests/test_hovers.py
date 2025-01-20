from config.config_reader import ConfigReader
from pages.hovers import HoversPage
from pages.main_page import MainPage


def test_hovers(chrome_driver):
    main_page = MainPage(chrome_driver)
    hover_page = HoversPage(chrome_driver)
    chrome_driver.get(ConfigReader().get("herokuapp_url"))
    profile_url = ConfigReader().get("profile_url")
    main_page.go_to_hovers_page()

    profile_elements = hover_page.get_all_profiles()
    print(profile_elements)
    profile_count = len(profile_elements)

    for id in range(1, profile_count + 1):
        hover_page.view_profile(id)
        current_url = chrome_driver.get_current_url()
        expected_url = profile_url.format(id=id)
        assert profile_url.format(id=id) == current_url, (f"Profile URL does not match the current one."
                                                          f" Expected: {expected_url} Actual: {current_url}")
        chrome_driver.return_from_profile_to_hover_page()
