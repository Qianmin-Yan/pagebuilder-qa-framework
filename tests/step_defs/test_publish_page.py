import time
from pytest_bdd import given, when, then, parsers, scenarios

from locators.edit_page_locators import EditPageLocators
from pages.automizely_login_page import AutomizelyLoginPage
from pages.base_page import BasePage
from pages.edit_page import EditPage

scenarios('../features/publish_page.feature')


@given(parsers.parse('I navigate to website "{url}" with valid credential'))
def login(page, url):
    login_page = AutomizelyLoginPage(page)
    login_page.login(url)


@then(parsers.parse('I should see the page title "{page_title}"'))
def verify_page_title(page, page_title):
    assert page.title() == page_title, "Fail to login"


@given(parsers.parse('the user click on menu "{page_type}"'))
def the_user_click_on_menu(page, page_type):
    pb_base_page = BasePage(page)
    pb_base_page.click_on_span_contains_text(page_type)


@when(parsers.parse('the user choose from template "{template_name}" to publish "{page_type}"'))
def publish_page_from_template(page, template_name, page_type):
    edit_page = EditPage(page)
    edit_page.click_on_template_in_page_list(template_name)
    edit_page.publish_page()
    if page_type == "Home page":
        time.sleep(0.5)
        if edit_page.page.is_visible(EditPageLocators.confirm_to_publish_home_page_modal):
            edit_page.click_on_span_contains_text("Confirm")


@when(parsers.parse('the user choose template "{template_name}" to publish "{page_type}"'))
def publish_page_with_template(page, template_name, page_type):
    edit_page = EditPage(page)
    edit_page.click_on_template_in_page_list(template_name)
    edit_page.assign_product_or_collection(page_type)
    edit_page.publish_page()


@then('the user should see the Published successfully modal pop up')
def check_if_publish_successfully_modal_pop_up(page):
    edit_page = EditPage(page)
    assert edit_page.is_publish_successfully_modal_pop_up(), "publish page failed"
