from elements.base_element import BaseElement
import os

class Input(BaseElement):
    def send_keys(self):
        pass

    def upload_file(self, file_input_locator, file_path):

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File {file_path} not found!")

        file_input = self.driver.find_element(*file_input_locator)

        file_input.send_keys(file_path)
