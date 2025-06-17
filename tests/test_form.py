
from pages.form_page import FormPage

def test_simple_form(setup):
    driver = setup
    form = FormPage(driver)
    form.load_form()
    form.submit_message("Hello LambdaTest")
    assert "Hello LambdaTest" in form.get_output_message()
