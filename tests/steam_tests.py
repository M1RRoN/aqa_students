import pytest
from faker import Faker

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://store.steampowered.com/"

LOGIN_BUTTON = (By.XPATH, "//*[@id='global_actions']//a[contains(@class, 'global_action_link')]")
MAIN_PAGE_SEARCH = (By.ID, "store_nav_search_term")
LOGIN_BUTTON_IN_LOGIN_PAGE = (By.XPATH, "//div[@data-featuretarget='login']//button[@type='submit']")
ERROR_IN_LOGIN_PAGE = (
    By.XPATH, "//a[contains(@href, 'HelpWithLogin')]//preceding-sibling::*[1]")
LOGIN_FIELD_IN_LOGIN_PAGE = (
    By.XPATH, "//a[contains(@href, 'HelpWithLogin')]//preceding-sibling::*[5]//input")
PASSWORD_FIELD_IN_LOGIN_PAGE = (By.XPATH, "//input[@type='password']")
SUBMIT_BUTTON_NOT_DISABLED_LOCATOR = (By.XPATH, "//div[@data-featuretarget='login']//button[@type='submit' and not(@disabled)]")

WAIT = 10

fake = Faker()


@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--disable-popup-blocking")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(BASE_URL)
    yield driver
    driver.quit()


def test_input_random_creds_in_login_page(driver):
    WebDriverWait(driver, WAIT).until(
        EC.element_to_be_clickable(LOGIN_BUTTON)
    ).click()

    WebDriverWait(driver, WAIT).until(
        EC.visibility_of_element_located(LOGIN_FIELD_IN_LOGIN_PAGE)
    ).send_keys(fake.email())

    WebDriverWait(driver, WAIT).until(
        EC.visibility_of_element_located(PASSWORD_FIELD_IN_LOGIN_PAGE)
    ).send_keys(fake.password())

    WebDriverWait(driver, WAIT).until(
        EC.element_to_be_clickable(LOGIN_BUTTON_IN_LOGIN_PAGE)
    ).click()

    WebDriverWait(driver, WAIT).until(
        EC.presence_of_element_located(SUBMIT_BUTTON_NOT_DISABLED_LOCATOR)
    )

    error = WebDriverWait(driver, WAIT).until(
        EC.presence_of_element_located(ERROR_IN_LOGIN_PAGE)
    ).text
    assert error == "Пожалуйста, проверьте свой пароль и имя аккаунта и попробуйте снова.", "Ошибка: текст ошибки не совпадает"
    assert driver.execute_script("return document.readyState") == "complete", "Страница не загрузилась полностью"
