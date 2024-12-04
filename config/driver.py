import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BASE_URL
from pages.main_page import WAIT


class SingletonDriver:
    _driver = None

    @classmethod
    def get_driver(cls):
        if cls._driver is None:
            chrome_options = Options()
            chrome_options.add_argument("--disable-popup-blocking")
            cls._driver = webdriver.Chrome(options=chrome_options)
            cls._driver.get(BASE_URL)
        return cls._driver

    @classmethod
    def quit_driver(cls):
        if cls._driver:
            cls._driver.quit()
            cls._driver = None


@pytest.fixture(scope="session")
def driver(request):
    lang = request.param
    driver = SingletonDriver.get_driver()

    driver.get(f"{BASE_URL}")
    if lang:
        html_lang = driver.find_element(By.TAG_NAME, "html").get_attribute("lang")
        if html_lang != lang:
            WebDriverWait(driver, WAIT).until(
                EC.element_to_be_clickable((By.ID, "language_pulldown"))
            ).click()
            WebDriverWait(driver, WAIT).until(
                EC.element_to_be_clickable(
                    (By.XPATH,
                     f"//div[@id='language_dropdown']//a[contains(@onclick, 'ChangeLanguage') and contains(@onclick, '{lang}')][1]")
                )
            ).click()

    yield driver
    SingletonDriver.quit_driver()
