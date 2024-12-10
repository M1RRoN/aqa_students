import json
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class ConfigReader:
    def __init__(self, config_path=None):
        if config_path is None:
            base_dir = Path(__file__).resolve().parent.parent
            config_path = base_dir / "config" / "config.json"
        self._config = self._load_config(config_path)

    def _load_config(self, config_path):
        try:
            with open(config_path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            raise Exception(f"Config file '{config_path}' not found")

    def get(self, key, default=None):
        return self._config.get(key, default)


class SingletonDriver:
    _driver = None
    _config = ConfigReader()

    @classmethod
    def get_driver(cls):
        if cls._driver is None:
            chrome_options = Options()
            options_from_config = cls._config.get("chrome_options", [])
            for option in options_from_config:
                chrome_options.add_argument(option)
            cls._driver = webdriver.Chrome(options=chrome_options)
        return cls._driver

    @classmethod
    def quit_driver(cls):
        if cls._driver:
            cls._driver.quit()
            cls._driver = None
