import pytest

from config.driver import SingletonDriver
from config.config_reader import ConfigReader
from config.language_enum import Language
from pages.main_page import MainPage


@pytest.fixture(scope="session")
def base_url():
    config = ConfigReader()
    return config.get("base_url")


@pytest.fixture(scope="function")
def driver(request, base_url):
    lang = request.param
    driver = SingletonDriver.get_driver(lang=lang)
    driver.get(base_url)
    yield driver
    SingletonDriver.quit_driver()

@pytest.fixture(scope="function")
def set_lang(request, base_url, driver):
    lang = request.param
    driver.get(base_url)
    main = MainPage()
    lang_enum = Language(lang)
    html_lang = main.get_language()
    if html_lang != lang_enum:
        main.click_on_language_button()
        main.set_new_language(lang_enum)
