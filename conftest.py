import pytest

from config.driver import SingletonDriver
from config.config_reader import ConfigReader
from config.language_enum import Language
from pages.main_page import MainPage


@pytest.fixture(scope="session")
def wait():
    config = ConfigReader()
    return config.get("wait")


@pytest.fixture(scope="session")
def base_url():
    config = ConfigReader()
    return config.get("base_url")


@pytest.fixture(scope="function")
def driver(request, wait, base_url):
    lang = request.param
    driver = SingletonDriver.get_driver(lang=lang)
    driver.get(base_url)
    yield driver
    SingletonDriver.quit_driver()

@pytest.fixture(scope="function")
def set_lang(request, wait, base_url, driver):
    lang = request.param
    driver.get(base_url)
    main = MainPage()

    if lang:
        lang_enum = None
        for language in Language:
            if language == lang:
                lang_enum = language
                break

        if lang:
            try:
                lang_enum = Language(lang)
            except ValueError:
                raise ValueError(f"Language '{lang}' not found in enum.")

        html_lang = main.get_language()
        if html_lang != lang_enum.value:
            main.click_on_language_button()
            main.set_new_language(lang_enum.value)
