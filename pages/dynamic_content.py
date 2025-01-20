from elements.label import Label
from elements.web_element import WebElement
from pages.base_page import BasePage


class DynamicContentPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='content']//h3[contains(text(), 'Dynamic Content')]"

    DYNAMIC_IMAGE_LOC = "//*[@id='content']//img[contains(@src, 'Avatar')]"
    BUTTON_DYNAMIC_CONTENT_LOC = "//*[@id='content']//a[contains(text(), 'Dynamic Content')]"

    def __init__(self, browser):
        super().__init__(browser)
        self.name = "dynamic_content"

        self.slider = Label(browser, self.DYNAMIC_IMAGE_LOC, "Dynamic content -> Image")
        self.unique_element = WebElement(browser, self.UNIQUE_ELEMENT_LOC, "Dynamic Content -> unique element")
        self.image = WebElement(browser, self.DYNAMIC_IMAGE_LOC, "Dynamic Content -> images")

    def page_is_open(self):
        self.wait_for_open()

    def refresh_page_while_not_find_identical_images(self):
        src_list = self.get_all_image_sources(self.image.locator)

        while len(set(src_list)) == 3:
            self.browser.refresh()
            src_list = self.get_all_image_sources(self.image.locator)
        return src_list

    def get_all_image_sources(self, locator):
        images = self.browser.presence_of_all_elements_located(locator)
        src_values = [img.get_attribute("src") for img in images if img.get_attribute("src")]
        return src_values
