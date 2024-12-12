from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from config.config_reader import ConfigReader


class SingletonDriver:
    _driver = None
    _config = ConfigReader()

    @classmethod
    def get_driver(cls, lang=None, base_url=None):
        if cls._driver is None:
            chrome_options = Options()
            if lang:
                chrome_options.add_argument(f"--lang={lang}")
            options_from_config = cls._config.get("chrome_options")
            for option in options_from_config:
                chrome_options.add_argument(option)
            cls._driver = webdriver.Chrome(options=chrome_options)
        return cls._driver

    @classmethod
    def quit_driver(cls):
        if cls._driver:
            cls._driver.quit()
            cls._driver = None
