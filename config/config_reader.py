import json


class ConfigReader:
    CONFIG_PATH = "config/config.json"

    def __init__(self, config_path=CONFIG_PATH):
        self.config_path = config_path
        self.config_data = None

    def _load_config(self):
        with open(self.config_path, "r") as file:
            self.config_data = json.load(file)

    def get(self, key):
        if self.config_data is None:
            self._load_config()
        return self.config_data.get(key)
