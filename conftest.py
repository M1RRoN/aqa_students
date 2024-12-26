import pytest
from selenium import webdriver

from browser.browser import Browser


@pytest.fixture(scope="function")
def driver():
    web_driver = webdriver.Chrome()
    browser = Browser(driver=web_driver)
    yield browser
    browser.quit()
