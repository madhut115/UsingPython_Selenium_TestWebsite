
from pages.dropdown_page import DropdownPage

def test_dropdown(setup):
    driver = setup
    dd = DropdownPage(driver)
    dd.load_page()
    dd.select_day("Monday")
    assert "Monday" in dd.get_selected_day()
