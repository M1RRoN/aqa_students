from elements.label import Label
from elements.web_element import WebElement
from pages.base_page import BasePage


class DynamicContentPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='content']//h3[contains(text(), 'Dynamic Content')]"

    DYNAMIC_IMAGE_LOC = "//*[@id='content']//img[contains(@src, 'Avatar')]"
    BUTTON_DYNAMIC_CONTENT_LOC = "//*[@id='content']//a[contains(text(), 'Dynamic Content')]"

    def __init__(self, driver):
        super().__init__(driver)
        self.name = "dynamic_content"

        self.slider = Label(driver,self.DYNAMIC_IMAGE_LOC, "Dynamic content -> Image")
        self.unique_element = WebElement(driver, self.UNIQUE_ELEMENT_LOC, "Dynamic Content -> unique element")
        self.image = WebElement(driver, self.DYNAMIC_IMAGE_LOC, "Dynamic Content -> images")

    def page_is_open(self):
        self.wait_for_open()

    def refresh_page_while_not_find_identical_images(self):
        src_list = self.image.get_all_image_sources()

        while len(set(src_list)) == 3:
            self.driver.refresh()
            src_list = self.image.get_all_image_sources()
        return src_list
