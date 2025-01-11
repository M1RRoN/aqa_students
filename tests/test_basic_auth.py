import pytest
from selenium.webdriver.common.by import By

from pages.basic_auth import BasicAuth


@pytest.mark.parametrize("driver", ["chrome"], indirect=True)
def test_basic_auth(driver):
    driver.get(url="https://admin:admin@the-internet.herokuapp.com/basic_auth")
    alert = BasicAuth(driver)
    alert.login("admin", "admin")
    elem_text = driver.find_element(By.XPATH, alert.RESULT_LOC).text

    assert "Congratulations! You must have the proper credentials." == elem_text
