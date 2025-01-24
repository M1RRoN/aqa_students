from elements.label import Label
from elements.multi_web_element import MultiWebElement
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

    def get_all_image_sources(self):
        lambda_xpath_locator = lambda x: f"({self.image.locator[1]})[{x}]"
        images_multi = MultiWebElement(
            driver=self.browser,
            lambda_xpath_locator=lambda_xpath_locator,
            description="Image elements"
        )

        src_values = []
        for image in images_multi:
            src = image.get_attribute("src")
            if src:
                src_values.append(src)

        return src_values

    def refresh_page_while_not_find_identical_images(self, count_src):
        src_list = self.get_all_image_sources()

        while len(set(src_list)) == count_src:
            self.browser.refresh()
            src_list = self.get_all_image_sources()

        return src_list
