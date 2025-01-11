import os

from elements.input import Input
from pages.base_page import BasePage


class Upload(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='file-upload']"

    URL = "https://the-internet.herokuapp.com/upload"
    BUTTON_UPLOAD = "//*[@id='file-submit']"
    UPLOADED_FILES = "//*[@id='uploaded-files']"
    DRAG_AND_DROP = "//*[@id='drag-drop-upload']"
    HIDDEN_INPUT = "//input[contains(@class, 'dz-hidden-input')]"

    FILE_PATH = os.path.normpath(
        os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "..", "test_files", "SteamSetup.exe"
        )
    )

    def __init__(self, driver):
        super().__init__(driver)
        self.name = "upload"

        self.upload = Input(driver, 10, "Upload file page -> upload", self.UNIQUE_ELEMENT_LOC)
