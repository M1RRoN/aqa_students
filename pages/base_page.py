from config.config_reader import ConfigReader


class BasePage:
    UNIQUE_ELEMENT_LOC = None
    TIMEOUT = ConfigReader().get("timeout")

    def __init__(self, browser):
        self.browser = browser

        self.page_name = None
        self.unique_element = None

    def wait_for_open(self):
        self.unique_element.presence_of_element_located()
