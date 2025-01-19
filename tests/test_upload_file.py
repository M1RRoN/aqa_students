import time

import pyautogui
import pytest
from selenium.webdriver.common.by import By

from config.config_reader import ConfigReader
from pages.main_page import MainPage
from pages.upload import UploadPage


def test_upload_file(chrome_driver):
    main_page = MainPage(chrome_driver)
    upload_page = UploadPage(chrome_driver)
    chrome_driver.get(ConfigReader().get("herokuapp_url"))
    main_page.go_to_file_upload_page()

    upload_page.upload_file()
    file_name = chrome_driver.execute_script("return document.getElementById('file-upload').value;")

    assert file_name.endswith("SteamSetup.exe"), f"Expected: {file_name.endswith("SteamSetup.exe")}, Actual: '{file_name}'"

    upload_page.click_on_upload_button()

    expected_result_text = "File Uploaded!"
    result_text = upload_page.get_result_text_after_upload_file()
    expected_file_name = "SteamSetup.exe"
    result_file_name = upload_page.get_file_name_after_upload()

    assert expected_result_text == result_text, f"Expected text: {expected_result_text} Actual text: {result_text}"
    assert expected_file_name == result_file_name, f"Expected file name: {expected_file_name} Actual file name: {result_file_name}"


def test_upload_dialog_window(chrome_driver):
    main_page = MainPage(chrome_driver)
    upload_page = UploadPage(chrome_driver)
    chrome_driver.get(ConfigReader().get("herokuapp_url"))
    main_page.go_to_file_upload_page()

    upload_page.click_on_drag_and_drop()
    upload_page.send_keys_into_hidden_input()

    expected_file_name = "SteamSetup.exe"
    result_file_name = upload_page.get_result_file_name_after_drag_and_drop()
    expected_mark = "✔"
    result_mark = upload_page.get_success_mark()

    assert expected_file_name == result_file_name, f"Expected file name: {expected_file_name} Actual file name: {result_file_name}"
    assert expected_mark == result_mark, f"Expected mark: {expected_mark} Actual mark: {result_mark}"


@pytest.mark.parametrize("driver", ["chrome"], indirect=True)
def test_drag_and_drop(driver):
    upload = UploadPage(driver)
    driver.get(ConfigReader().get("herokuapp_url"))

    upload_area = driver.find_element(By.ID, "drag-drop-upload")
    rect = upload_area.rect
    upload_area_x = rect['x'] + rect['width'] // 2
    upload_area_y = rect['y'] + rect['height'] // 2
    time.sleep(5)

    pyautogui.hotkey('win', 'r')
    time.sleep(1)

    pyautogui.write("explorer")
    pyautogui.press('enter')
    time.sleep(1)

    for _ in range(5):
        pyautogui.press('tab')
    pyautogui.write("C:\\PycharmProjects\\aqa_students\\test_files")
    pyautogui.press('enter')
    time.sleep(1)

    file_x = 1130
    file_y = 560

    time.sleep(1)

    pyautogui.moveTo(file_x, file_y)
    time.sleep(1)
    pyautogui.mouseDown()
    time.sleep(1)

    pyautogui.moveTo(upload_area_x, upload_area_y)
    time.sleep(1)
    pyautogui.moveTo(upload_area_x, upload_area_y)
    time.sleep(1)
    pyautogui.mouseUp()

    assert "✔" == driver.find_element(By.XPATH, "(//div[contains(@class, 'dz-success-mark')]//span)[2]").text, "Иконка не совпадает"
