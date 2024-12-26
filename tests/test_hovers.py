from pages.hovers import Hovers


def test_hovers(driver):
    hover = Hovers(driver)
    driver.get(hover.URL)
    for id in range(1, 4):
        hover.view_profile(id)
        current_url = driver.get_current_url()
        assert hover.PROFILE_URL.format(id=id) == current_url
        driver.back()
