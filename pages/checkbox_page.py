
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckboxPage(BasePage):
    CHECKBOX_DEMO_LINK = (By.LINK_TEXT, "Checkbox Demo")
    SINGLE_CHECKBOX = (By.XPATH, "//input[@type='checkbox']")
    RESULT_TEXT = (By.XPATH, "//p[normalize-space()='Checked!']")

    def load_page(self):
        self.click(self.CHECKBOX_DEMO_LINK)

    def click_checkbox(self):
        self.click(self.SINGLE_CHECKBOX)

    def get_result(self):
        return self.get_text(self.RESULT_TEXT)
