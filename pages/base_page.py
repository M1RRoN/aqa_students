from selenium.common import TimeoutException

from config.config_reader import ConfigReader
from config.driver import SingletonDriver


class BasePage:
    def __init__(self):
        self.driver = SingletonDriver.get_driver()
        self.wait = ConfigReader().get("wait")

    def wait_for_open(self):
        ready_state = self.driver.execute_script("return document.readyState")
        if ready_state != "complete":
            raise TimeoutException(
                f"Страница не загрузилась полностью. Получено: {ready_state}, ожидаемо: 'complete'."
            )
