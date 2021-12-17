from pytest_bdd import parsers, given, then

from pages.automizely_login_page import AutomizelyLoginPage
from pages.base_page import BasePage


@given(parsers.parse('I navigate to PageBuilder website with valid credential'), target_fixture="login")
def login(page):
    login_page = AutomizelyLoginPage(page)
    login_page.login()


@then(parsers.parse('I should see the PageBuilder logo'), target_fixture="verify login")
def verify_page_title(page):
    pb_base_page = BasePage(page)
    pb_base_page.is_page_logo_visible()
