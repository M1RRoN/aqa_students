from enum import Enum

import pytest

from config.driver import SingletonDriver, ConfigReader
from pages.main_page import MainPage


class Language(Enum):
    ENGLISH = "en"
    RUSSIAN = "ru"


@pytest.fixture(scope="session")
def wait():
    config = ConfigReader()
    return config.get("wait")

@pytest.fixture(scope="session")
def base_url():
    config = ConfigReader()
    return config.get("base_url")

@pytest.fixture(scope="session")
def driver(request, wait, base_url):
    lang = request.param

    driver = SingletonDriver.get_driver()
    driver.get(base_url)
    main = MainPage(wait, base_url)

    if lang:
        lang_enum = None
        for language in Language:
            if language.value == lang:
                lang_enum = language
                break

        if lang_enum is None:
            raise ValueError(f"Language '{lang}' not found in enum.")

        html_lang = main.get_language()
        if html_lang != lang_enum.value:
            main.click_on_language_button()
            main.set_new_language(lang_enum.value)

    yield driver
    SingletonDriver.quit_driver()
