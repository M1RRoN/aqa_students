from enum import StrEnum

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from config.config_reader import ConfigReader


class BrowserName(StrEnum):
    CHROME = "chrome"
    # FIREFOX = "firefox"
    # EDGE = "edge"


class BrowserFactory:
    @staticmethod
    def get_browser(browser_name: BrowserName):
        headless = ConfigReader().get("headless")

        def apply_headless(options):
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')

            if headless:
                options.add_argument("--headless")

        if browser_name == BrowserName.CHROME:
            options = ChromeOptions()
            apply_headless(options)
            chrome_driver_path = "/usr/bin/chromedriver"
            return webdriver.Chrome(service=ChromeService(executable_path=chrome_driver_path), options=options)

        # elif browser_name == BrowserName.FIREFOX:
        #     options = FirefoxOptions()
        #     apply_headless(options)
        #     return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
        #
        # elif browser_name == BrowserName.EDGE:
        #     options = EdgeOptions()
        #     apply_headless(options)
        #     return webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
