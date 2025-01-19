import os

from browser.browser import logger
from elements.button import Button
from elements.input import Input
from elements.web_element import WebElement
from pages.base_page import BasePage


class UploadPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='file-upload']"

    BUTTON_SELECT_FILE_LOC = "//*[@id='file-upload']"
    BUTTON_UPLOAD_LOC = "//*[@id='file-submit']"
    UPLOADED_FILES_LOC = "//*[@id='uploaded-files']"
    RESULT_TEXT_AFTER_UPLOAD = "//h3"

    DRAG_AND_DROP_LOC = "//*[@id='drag-drop-upload']"
    HIDDEN_INPUT_LOC = "//input[contains(@class, 'dz-hidden-input')]"
    RESULT_FILE_NAME_AFTER_DRAG_AND_DROP_LOC = "(//div[contains(@class, 'dz-filename')]//span)[1]"
    SUCCESS_MARK_LOC = "(//div[contains(@class, 'dz-success-mark')]//span)[2]"

    def __init__(self, driver):
        super().__init__(driver)
        self.name = "upload"
        self.path = os.path.join("test_files", "SteamSetup.exe")

        self.button_select_file = Input(driver, self.BUTTON_SELECT_FILE_LOC, "Upload file page -> Select file")
        self.button_upload = Button(driver, self.BUTTON_UPLOAD_LOC, "Upload File page -> Button upload")
        self.result_text = WebElement(driver, self.RESULT_TEXT_AFTER_UPLOAD, "Result text after upload")
        self.file_name = WebElement(driver, self.UPLOADED_FILES_LOC, "File name after upload")

        self.drag_and_drop = WebElement(driver, self.DRAG_AND_DROP_LOC, "Upload file page -> Drag and drop")
        self.hidden_input = Input(driver, self.HIDDEN_INPUT_LOC, "Upload file page -> Hidden input")
        self.file_name_drag_and_drop = WebElement(driver, self.RESULT_FILE_NAME_AFTER_DRAG_AND_DROP_LOC,
                                                  "Result file name after drag and drop")
        self.success_mark = WebElement(driver, self.SUCCESS_MARK_LOC, "Success mark after drag and drop")

    def upload_file(self):
        normalized_path = os.path.abspath(self.path)
        logger.info(f"Uploading file: {normalized_path}")
        self.button_select_file.element_to_be_clickable()
        self.button_select_file.send_keys(normalized_path)

    def click_on_upload_button(self):
        self.button_upload.click()

    def get_result_text_after_upload_file(self):
        text = self.result_text.get_text()
        return text

    def get_file_name_after_upload(self):
        text = self.file_name.get_text()
        return text

    def click_on_drag_and_drop(self):
        drag_and_drop = self.drag_and_drop.element_to_be_clickable()
        drag_and_drop.click()

    def send_keys_into_hidden_input(self):
        path = os.path.abspath(self.path)
        self.hidden_input.send_keys(path)

    def get_result_file_name_after_drag_and_drop(self):
        text = self.file_name_drag_and_drop.get_text()
        return text

    def get_success_mark(self):
        mark = self.success_mark.get_text()
        return mark
