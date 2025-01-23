from pathlib import Path

import pytest

from config.config_reader import ConfigReader
from pages.main_page import MainPage
from pages.upload import UploadPage
from scripts import GET_ELEMENT_BY_ID


@pytest.mark.parametrize("file_path", [Path("test_files/SteamSetup.exe")])
def test_upload_file(chrome_driver, file_path):
    main_page = MainPage(chrome_driver)
    upload_page = UploadPage(chrome_driver)
    chrome_driver.get(ConfigReader().get("herokuapp_url"))
    main_page.go_to_file_upload_page()

    upload_page.upload_file(file_path)
    file_name = chrome_driver.execute_script(GET_ELEMENT_BY_ID)

    assert file_name.endswith(file_path.name), f"Expected: {file_name.endswith(file_path.name)}, Actual: '{file_name}'"

    upload_page.click_on_upload_button()

    expected_result_text = "File Uploaded!"
    result_text = upload_page.get_result_text_after_upload_file()
    expected_file_name = file_path.name
    result_file_name = upload_page.get_file_name_after_upload()

    assert expected_result_text == result_text, f"Expected text: {expected_result_text} Actual text: {result_text}"
    assert expected_file_name == result_file_name, f"Expected file name: {expected_file_name} Actual file name: {result_file_name}"


@pytest.mark.parametrize("file_path", [Path("test_files/SteamSetup.exe")])
def test_upload_dialog_window(chrome_driver, file_path):
    main_page = MainPage(chrome_driver)
    upload_page = UploadPage(chrome_driver)
    chrome_driver.get(ConfigReader().get("herokuapp_url"))
    main_page.go_to_file_upload_page()

    upload_page.click_on_drag_and_drop()
    upload_page.send_path_into_hidden_input(file_path)

    expected_file_name = file_path.name
    result_file_name = upload_page.get_result_file_name_after_drag_and_drop()
    expected_mark = "✔"
    result_mark = upload_page.get_success_mark()

    assert expected_file_name == result_file_name, f"Expected file name: {expected_file_name} Actual file name: {result_file_name}"
    assert expected_mark == result_mark, f"Expected mark: {expected_mark} Actual mark: {result_mark}"
