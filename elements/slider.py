from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from elements.base_element import BaseElement


class Slider(BaseElement):
    def scroll_slider(self, move_offset):
        slider = self.driver.find_element(By.XPATH, self.locator)
        actions = ActionChains(self.driver)
        slider.send_keys(Keys.NULL)
        for _ in range(move_offset * 2):
            actions.send_keys(Keys.ARROW_RIGHT).perform()
