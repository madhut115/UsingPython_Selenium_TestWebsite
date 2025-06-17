
import pytest
from selenium import webdriver
from utils.config import URL
import os

@pytest.fixture(scope="function")
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(URL)
    request.node.driver = driver
    yield driver
    if request.node.rep_call.failed:
        screenshot_name = f"reports/{request.node.name}.png"
        driver.save_screenshot(screenshot_name)
    driver.quit()

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
