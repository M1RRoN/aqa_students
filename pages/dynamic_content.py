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

    # def get_image_sources(self, url, tag, attribute):
    #     self.driver.all_elements(self.URL, "img", "src")

    # def comparison_image(self, images):
    #     while attempts < max_attempts:
    #         image_sources = get_image_sources()
    #         print(f"Попытка {attempts + 1}: {image_sources}")
    #
    #         if has_two_identical(image_sources):
    #             print("Найдены одинаковые изображения!")
    #             break
    #
    #         driver.refresh()  # Обновляем страницу
    #         attempts += 1
    #     else:
    #         assert False, "Не удалось найти хотя бы два одинаковых изображения за ограниченное количество попыток"