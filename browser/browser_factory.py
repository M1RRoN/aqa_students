from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


class BrowserFactory:
    @staticmethod
    def get_browser(browser_name: str, headless: bool = False):
        browser_name = browser_name.lower()

        if browser_name == "chrome":
            options = ChromeOptions()
            if headless:
                options.add_argument("--headless")
            return webdriver.Chrome(service=ChromeService(), options=options)

        elif browser_name == "firefox":
            options = FirefoxOptions()
            if headless:
                options.add_argument("--headless")
            return webdriver.Firefox(service=FirefoxService("C:\FirefoxDriver\geckodriver.exe"), options=options)

        elif browser_name == "edge":
            options = EdgeOptions()
            if headless:
                options.add_argument("--headless")
            return webdriver.Edge(service=EdgeService("C:\EdgeDriver\msedgedriver.exe"), options=options)
