from elements.base_element import BaseElement


class WebElement(BaseElement):
    def get_all_image_sources(self):
        images = self.presence_of_all_elements_located()
        src_values = [img.get_attribute("src") for img in images if img.get_attribute("src")]
        return src_values