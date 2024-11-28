import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://store.steampowered.com/"

LOGIN_BUTTON = (By.XPATH, "//*[@id='global_actions']//a[contains(@class, 'global_action_link')]")
MAIN_PAGE_SEARCH = (By.XPATH, "//*[@id='store_nav_search_term']")
LOGIN_BUTTON_IN_LOGIN_PAGE = (By.XPATH, "//div[@data-featuretarget='login']//button[@type='submit']")
ERROR_IN_LOGIN_PAGE = (By.XPATH, "//*[@id='responsive_page_template_content']/div[3]/div[1]/div/div/div/div[2]/div/form/div[5]")
LOGIN_FIELD_IN_LOGIN_PAGE = (By.XPATH, "//*[@id='responsive_page_template_content']/div[3]/div[1]/div/div/div/div[2]/div/form/div[1]/input")
PASSWORD_FIELD_IN_LOGIN_PAGE = (By.XPATH, "//input[@type='password']")

WAIT = 10


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    yield driver
    driver.quit()


def test_main_page(driver):
    elem = driver.find_element(*MAIN_PAGE_SEARCH)
    assert elem is not None, "Ошибка: элемент не найден на странице"
    assert driver.execute_script("return document.readyState") == "complete", "Страница не загрузилась полностью"


def test_click_login_button(driver):
    driver.find_element(*LOGIN_BUTTON).click()
    text_login_page = WebDriverWait(driver, WAIT).until(
        EC.presence_of_element_located(LOGIN_BUTTON_IN_LOGIN_PAGE)
    ).text
    assert text_login_page == "Войти", "Ошибка: кнопка не найдена"
    assert driver.execute_script("return document.readyState") == "complete", "Страница не загрузилась полностью"


def test_input_random_creds_in_login_page(driver):
    driver.find_element(*LOGIN_BUTTON).click()
    WebDriverWait(driver, WAIT).until(
        EC.presence_of_element_located(LOGIN_FIELD_IN_LOGIN_PAGE)
    ).send_keys("account_name")
    driver.find_element(*PASSWORD_FIELD_IN_LOGIN_PAGE).send_keys("random_password")
    driver.find_element(*LOGIN_BUTTON_IN_LOGIN_PAGE).click()
    error = WebDriverWait(driver, WAIT).until(
        EC.text_to_be_present_in_element(ERROR_IN_LOGIN_PAGE,
                                         "Пожалуйста, проверьте свой пароль и имя аккаунта")
    )
    error_text = driver.find_element(*ERROR_IN_LOGIN_PAGE).text
    assert error_text == "Пожалуйста, проверьте свой пароль и имя аккаунта и попробуйте снова.", "Ошибка: текст ошибки не найден"
