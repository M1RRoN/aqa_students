import pytest

from browser.browser import Browser
from browser.browser_factory import BrowserFactory
from config.config_reader import ConfigReader


@pytest.fixture
def url():
    config_reader = ConfigReader()
    return config_reader.get


@pytest.fixture(scope="function")
def driver(request):
    browser_name = request.param
    web_driver = BrowserFactory().get_browser(browser_name=browser_name)
    browser = Browser(driver=web_driver)
    yield browser
    browser.quit()
