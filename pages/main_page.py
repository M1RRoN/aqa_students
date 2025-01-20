from elements.button import Button
from pages.base_page import BasePage


class MainPage(BasePage):
    UNIQUE_LOC = "//*[@id='content']//h1[contains(text(), 'Welcome to the-internet')]"

    BUTTON_BASIC_AUTH_LOC = "//*[@id='content']//a[contains(text(), 'Basic Auth')]"
    BUTTON_JAVASCRIPT_ALERTS_LOC = "//*[@id='content']//a[contains(text(), 'JavaScript Alerts')]"
    BUTTON_CONTEXT_MENU_LOC = "//*[@id='content']//a[contains(text(), 'Context Menu')]"
    BUTTON_DYNAMIC_CONTENT_LOC = "//*[@id='content']//a[contains(text(), 'Dynamic Content')]"
    BUTTON_HORIZONTAL_SLIDER_LOC = "//*[@id='content']//a[contains(text(), 'Horizontal Slider')]"
    BUTTON_HOVERS_PAGE_LOC = "//*[@id='content']//a[contains(text(), 'Hovers')]"
    BUTTON_ALERTS_FRAME_WINDOWS_LOC = "//h5[contains(text(), 'Alerts, Frame & Windows')]"
    BUTTON_INFINITE_SCROLL_LOC = "//*[@id='content']//a[contains(text(), 'Infinite Scroll')]"
    BUTTON_FILE_UPLOAD_LOC = "//*[@id='content']//a[contains(text(), 'File Upload')]"


    def __init__(self, browser):
        super().__init__(browser)
        self.name = "main_page"

        self.button_js_alerts = Button(browser, self.BUTTON_JAVASCRIPT_ALERTS_LOC, "Main page -> Alerts page")
        self.button_basic_auth = Button(browser, self.BUTTON_BASIC_AUTH_LOC, "Main page -> Basic Auth page")
        self.button_context_menu = Button(browser, self.BUTTON_CONTEXT_MENU_LOC,
                                          "Main page -> Context Menu page")
        self.button_dynamic_content = Button(browser, self.BUTTON_DYNAMIC_CONTENT_LOC,
                                             "Main page -> Dynamic Content page")
        self.button_horizontal_slider = Button(browser, self.BUTTON_HORIZONTAL_SLIDER_LOC,
                                               "Main page -> Horizontal Slider page")
        self.button_hovers = Button(browser, self.BUTTON_HOVERS_PAGE_LOC,
                                         "Main page -> Hovers page")
        self.button_alerts_frame_windows = Button(browser, self.BUTTON_ALERTS_FRAME_WINDOWS_LOC,
                                                  "Main page -> Alerts, Frame & Windows page")
        self.button_infinite_scroll = Button(browser, self.BUTTON_INFINITE_SCROLL_LOC,
                                             "Main page -> Infinite Scroll page")
        self.button_file_upload = Button(browser, self.BUTTON_FILE_UPLOAD_LOC, "Main page -> File Upload page")

    def go_to_js_alerts_page(self):
        self.button_js_alerts.click()

    def go_to_basic_auth_page(self):
        self.button_basic_auth.click()

    def go_to_context_menu_page(self):
        self.button_context_menu.click()

    def go_to_dynamic_content_page(self):
        self.button_dynamic_content.click()

    def go_to_horizontal_slider_page(self):
        self.button_horizontal_slider.click()

    def go_to_hovers_page(self):
        self.button_hovers.click()

    def go_to_alerts_frame_windows_page(self):
        self.button_alerts_frame_windows.click()

    def go_to_infinite_scroll_page(self):
        self.button_infinite_scroll.click()

    def go_to_file_upload_page(self):
        self.button_file_upload.click()
