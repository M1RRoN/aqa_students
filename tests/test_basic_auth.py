from pages.basic_auth import BasicAuth


def test_basic_auth(driver):
    driver.get(url="https://admin:admin@the-internet.herokuapp.com/basic_auth")
    alert = BasicAuth(driver)
    alert.login("admin", "admin")
    elem_text = driver.find_element(alert.RESULT_LOC).text

    assert "Congratulations! You must have the proper credentials." == elem_text
