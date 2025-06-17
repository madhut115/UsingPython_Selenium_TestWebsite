
from pages.checkbox_page import CheckboxPage

def test_checkbox(setup):
    driver = setup
    cb = CheckboxPage(driver)
    cb.load_page()
    cb.click_checkbox()
    assert "Checked!" in cb.get_result()
