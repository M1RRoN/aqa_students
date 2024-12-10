from config.driver import SingletonDriver


class BasePage:
    def __init__(self):
        self.driver = SingletonDriver.get_driver()
