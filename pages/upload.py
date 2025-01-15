import os

from elements.input import Input
from pages.base_page import BasePage


class UploadPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='file-upload']"

    BUTTON_SELECT_FILE_LOC = "//*[@id='file-upload']"
    BUTTON_UPLOAD_LOC = "//*[@id='file-submit']"
    UPLOADED_FILES_LOC = "//*[@id='uploaded-files']"
    DRAG_AND_DROP_LOC = "//*[@id='drag-drop-upload']"
    HIDDEN_INPUT_LOC = "//input[contains(@class, 'dz-hidden-input')]"
    BUTTON_FILE_UPLOAD_LOC = "//*[@id='content']//a[contains(text(), 'File Upload')]"


    def __init__(self, driver):
        super().__init__(driver)
        self.name = "upload"

        self.upload_file = Input(driver, "Upload file page -> upload", self.BUTTON_SELECT_FILE_LOC)

    def upload_file(self, file_path):
        normalized_path = os.path.normpath(file_path)
        self.logger.info(f"Uploading file: {normalized_path}")
