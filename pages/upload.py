import os

from browser.browser import logger
from elements.button import Button
from elements.input import Input
from elements.web_element import WebElement
from pages.base_page import BasePage


class UploadPage(BasePage):
    UNIQUE_ELEMENT_LOC = "file-upload"

    BUTTON_SELECT_FILE_LOC = "file-upload"
    BUTTON_UPLOAD_LOC = "file-submit"
    UPLOADED_FILES_LOC = "uploaded-files"
    RESULT_TEXT_AFTER_UPLOAD = "//h3"

    DRAG_AND_DROP_LOC = "drag-drop-upload"
    HIDDEN_INPUT_LOC = "//input[contains(@class, 'dz-hidden-input')]"
    RESULT_FILE_NAME_AFTER_DRAG_AND_DROP_LOC = "(//div[contains(@class, 'dz-filename')]//span)[1]"
    SUCCESS_MARK_LOC = "(//div[contains(@class, 'dz-success-mark')]//span)[2]"

    def __init__(self, browser):
        super().__init__(browser)
        self.name = "upload"

        self.button_select_file = Input(browser, self.BUTTON_SELECT_FILE_LOC, "Upload file page -> Select file")
        self.button_upload = Button(browser, self.BUTTON_UPLOAD_LOC, "Upload File page -> Button upload")
        self.result_text = WebElement(browser, self.RESULT_TEXT_AFTER_UPLOAD, "Result text after upload")
        self.file_name = WebElement(browser, self.UPLOADED_FILES_LOC, "File name after upload")

        self.drag_and_drop = WebElement(browser, self.DRAG_AND_DROP_LOC, "Upload file page -> Drag and drop")
        self.hidden_input = Input(browser, self.HIDDEN_INPUT_LOC, "Upload file page -> Hidden input")
        self.file_name_drag_and_drop = WebElement(browser, self.RESULT_FILE_NAME_AFTER_DRAG_AND_DROP_LOC,
                                                  "Result file name after drag and drop")
        self.success_mark = WebElement(browser, self.SUCCESS_MARK_LOC, "Success mark after drag and drop")

    def upload_file(self, path):
        normalized_path = os.path.abspath(path)
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

    def send_path_into_hidden_input(self, file_path):
        path = os.path.abspath(file_path)
        self.hidden_input.send_keys_into_hidden_input(path)

    def get_result_file_name_after_drag_and_drop(self):
        text = self.file_name_drag_and_drop.get_text()
        return text

    def get_success_mark(self):
        mark = self.success_mark.get_text()
        return mark
