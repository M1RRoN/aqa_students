from elements.label import Label
from pages.base_page import BasePage


class DynamicContent(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='content']//h3[contains(text(), 'Dynamic Content')]"

    DYNAMIC_IMAGE_LOC = "//*[@id='content']//img[contains(@src, 'Avatar-{id}')]"
    URL = "https://the-internet.herokuapp.com/dynamic_content"

    def __init__(self, driver):
        super().__init__(driver)
        self.name = "dynamic_content"

        self.slider = Label(driver, 10, "Dynamic content -> Image", self.DYNAMIC_IMAGE_LOC)

    def change_image(self):
        self.driver.refresh()
