
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class FormPage(BasePage):
    SIMPLE_FORM_LINK = (By.LINK_TEXT, "Simple Form Demo")
    MESSAGE_INPUT = (By.ID, "user-message")
    SHOW_MESSAGE_BTN = (By.ID, "showInput")
    OUTPUT_TEXT = (By.ID, "message")

    def load_form(self):
        self.click(self.SIMPLE_FORM_LINK)

    def submit_message(self, msg):
        self.enter_text(self.MESSAGE_INPUT, msg)
        self.click(self.SHOW_MESSAGE_BTN)

    def get_output_message(self):
        return self.get_text(self.OUTPUT_TEXT)
