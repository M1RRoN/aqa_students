from elements.label import Label
from pages.base_page import BasePage


class DynamicContentPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='content']//h3[contains(text(), 'Dynamic Content')]"

    DYNAMIC_IMAGE_LOC = "//*[@id='content']//img[contains(@src, 'Avatar-{id}')]"
    BUTTON_DYNAMIC_CONTENT_LOC = "//*[@id='content']//a[contains(text(), 'Dynamic Content')]"

    def __init__(self, driver):
        super().__init__(driver)
        self.name = "dynamic_content"

        self.slider = Label(driver,"Dynamic content -> Image", self.DYNAMIC_IMAGE_LOC)
