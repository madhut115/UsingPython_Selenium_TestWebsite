
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator)).click()

    def enter_text(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).clear()
        self.driver.find_element(*by_locator).send_keys(text)

    def get_text(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).text

    def select_dropdown_by_visible_text(self, by_locator, value):
        from selenium.webdriver.support.ui import Select
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))
        Select(self.driver.find_element(*by_locator)).select_by_visible_text(value)
