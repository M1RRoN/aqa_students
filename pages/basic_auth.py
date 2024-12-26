from pages.base_page import BasePage


class BasicAuth(BasePage):
    UNIQUE_LOC = None

    LOGIN_URL = "https://admin:admin@the-internet.herokuapp.com/basic_auth"
    RESULT_LOC = "//*[@id='content']"

    def __init__(self, driver):
        super().__init__(driver)
        self.name = "basic_auth"

    def login(self, login: str, password: str):
        self.driver.get(url=f"https://{login}:{password}@the-internet.herokuapp.com/basic_auth")
