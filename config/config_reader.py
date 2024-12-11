import json


class ConfigReader:
    CONFIG_PATH = "config/config.json"

    def __init__(self, config_path=None):
        self.config_path = config_path or self.CONFIG_PATH

    def get(self, key):
        with open(self.config_path, "r") as file:
            config = json.load(file)
        return config.get(key)
