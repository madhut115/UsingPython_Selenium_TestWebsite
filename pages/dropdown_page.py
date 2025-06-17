
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DropdownPage(BasePage):
    DROPDOWN_LINK = (By.LINK_TEXT, "Select Dropdown List")
    DAY_SELECT = (By.ID, "select-demo")
    SELECTED_TEXT = (By.CLASS_NAME, "selected-value")

    def load_page(self):
        self.click(self.DROPDOWN_LINK)

    def select_day(self, day):
        self.select_dropdown_by_visible_text(self.DAY_SELECT, day)

    def get_selected_day(self):
        return self.get_text(self.SELECTED_TEXT)
