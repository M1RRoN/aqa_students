import time

import pyautogui
import pytest
from selenium.webdriver.common.by import By

from config.config_reader import ConfigReader
from pages.upload import UploadPage


@pytest.mark.parametrize("driver", ["chrome"], indirect=True)
def test_upload_file(driver):
    upload = UploadPage(driver)
    driver.get(ConfigReader().get("herokuapp_url"))
    upload.goto(By.XPATH, upload.BUTTON_FILE_UPLOAD_LOC)

    upload.upload_file.upload_file((By.XPATH, "//*[@id='file-upload']"), upload.FILE_PATH)
    file_name = driver.execute_script("return document.getElementById('file-upload').value;")

    assert file_name.endswith("SteamSetup.exe"), f"Ожидалось имя файла, но было '{file_name}'"

    driver.find_element(By.XPATH, upload.BUTTON_UPLOAD_LOC).click()

    assert "File Uploaded!" == driver.find_element(By.XPATH, "//h3").text, "Текст не совпадает"
    assert "SteamSetup.exe" == driver.find_element(By.XPATH, upload.UPLOADED_FILES_LOC).text, "Название файла не совпадает"


@pytest.mark.parametrize("driver", ["chrome"], indirect=True)
def test_upload_dialog_window(driver):
    upload = UploadPage(driver)
    driver.get(ConfigReader().get("herokuapp_url"))

    file_input = driver.find_element(By.XPATH, upload.DRAG_AND_DROP_LOC)
    file_input.click()
    driver.find_element(By.XPATH, "//input[contains(@class, 'dz-hidden-input')]").send_keys(upload.FILE_PATH)

    assert "SteamSetup.exe" == driver.find_element(By.XPATH, "(//div[contains(@class, 'dz-filename')]//span)[1]").text
    assert "✔" == driver.find_element(By.XPATH, "(//div[contains(@class, 'dz-success-mark')]//span)[2]").text


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
