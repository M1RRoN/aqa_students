import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = 'https://store.steampowered.com/'
LOGIN_PAGE_URL = "https://store.steampowered.com/login"


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_main_page(driver):
    driver.get(BASE_URL)
    title = driver.title
    assert title == 'Добро пожаловать в Steam'


def test_click_login_button(driver):
    driver.get(BASE_URL)
    driver.find_element(By.XPATH, '//div[@id="global_actions"]//a[contains(@class, "global_action_link")]').click()
    text_login_page = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[text()='Войти, используя имя аккаунта']"))
    ).text
    assert text_login_page == "Войти, используя имя аккаунта".upper()


def test_input_random_creds_in_login_page(driver):
    driver.implicitly_wait(10)
    driver.get(LOGIN_PAGE_URL)
    driver.find_element(By.XPATH, "//input[@type='text'][contains(@class, '_2GBW')]").send_keys("account_name")
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys("random_password")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.XPATH, "//div[contains(@class, '_1W_6HX')]"),
                                         "Пожалуйста, проверьте свой пароль и имя аккаунта")
    )
    error = driver.find_element(By.XPATH, "//div[contains(@class, '_1W_6HX')]").text
    assert error == "Пожалуйста, проверьте свой пароль и имя аккаунта и попробуйте снова."
