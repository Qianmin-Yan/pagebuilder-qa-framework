from pytest_bdd import given, when, then, parsers, scenarios

from pages.automizely_login_page import AutomizelyLoginPage
from pages.edit_page import EditPage
from pages.base_page import BasePage
from pages.shopify_page import ShopifyPage

scenarios('../features/form_section.feature')


@given(parsers.parse('I navigate to pagebuilder website with valid credential'))
def login(page):
    login_page = AutomizelyLoginPage(page)
    login_page.login()


@then(parsers.parse('I should see the pagebuilder logo'))
def verify_page_title(page):
    pb_base_page = BasePage(page)
    pb_base_page.is_page_logo_visible()


@given("the user add form with coupon into the first regular page")
def add_form_to_first_regular_page(page):
    edit_page = EditPage(page)
    edit_page.click_on_first_page_in_page_list()
    edit_page.add_form_with_coupon()
    edit_page.switch_tab("Settings")
    edit_page.publish_page()


@then('the user should see the Published successfully modal pop up')
def check_if_publish_successfully_modal_pop_up(page):
    edit_page = EditPage(page)
    edit_page.is_publish_successfully_modal_pop_up()


@given(parsers.parse('the user visit the page "{page_url}"'))
def visit_page(page, page_url):
    shopify_page = ShopifyPage(page)
    shopify_page.page.goto(page_url)
    shopify_page.input_store_password()
    shopify_page.page.goto(page_url)


@when(parsers.parse('the user submit form with "{email}"'))
def submit_form(page, context, email):
    shopify_page = ShopifyPage(page)
    edit_page = EditPage(page)
    breakpoint()
    edit_page.click_on_span_contains_text("View page")
    shopify_page.input_store_password()
    edit_page.click_on_span_contains_text("View page")
    shopify_page.submit_form(email)
    page.frame()


@then(parsers.parse('the user should see the coupon "{coupon_code}" is shown'))
def the_user_see_coupon_code(page, coupon_code):
    shopify_page = ShopifyPage(page)
    shopify_page.is_element_exists(coupon_code), "submit form failed"


@then(parsers.parse('the email "{email}" is created in shopify admin'))
def the_email_is_created_in_shopify_admin(page, email):
    shopify_page = ShopifyPage(page)
    # shopify_page.login_in()
    assert shopify_page.the_email_exists(email), "the email is not created in shopify admin"
