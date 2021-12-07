import time

from pytest_bdd import when, then, parsers, scenarios, given

from pages.automizely_login_page import AutomizelyLoginPage
from pages.shopify_page import ShopifyPage
from locators.edit_page_locators import EditPageLocators
from pages.edit_page import EditPage
from pages.base_page import BasePage

scenarios('../features/product_list_section.feature')


@given(parsers.parse('I navigate to pagebuilder website with valid credential'))
def login(page):
    login_page = AutomizelyLoginPage(page)
    login_page.login()


@then(parsers.parse('I should see the pagebuilder logo'))
def verify_page_title(page):
    pb_base_page = BasePage(page)
    pb_base_page.is_page_logo_visible()


@given(parsers.parse('the user click on menu "{page_type}"'))
def the_user_click_on_menu(page, page_type):
    pb_base_page = BasePage(page)
    pb_base_page.click_on_span_contains_text(page_type)


@when(parsers.parse('the user add product list into the first "{page_type}" with "{added_products_total}" products'))
def add_product_list_into_first_page(page, page_type, added_products_total):
    edit_page = EditPage(page)
    edit_page.click_on_first_page_in_page_list()
    added_products_total = int(added_products_total)
    edit_page.add_product_list_with_products(added_products_total)
    edit_page.switch_tab("Settings")
    edit_page.publish_page()
    if page_type == "Home page":
        time.sleep(1)
        if edit_page.page.is_visible(EditPageLocators.confirm_to_publish_home_page_modal):
            edit_page.click_on_span_contains_text("Confirm")


@then('the user should see the Published successfully modal pop up')
def check_if_publish_successfully_modal_pop_up(page):
    edit_page = EditPage(page)
    edit_page.is_publish_successfully_modal_pop_up(), "publish page failed"


@then(parsers.parse('the user is able to see "{added_products_total}" product in live page product list section'))
def check_if_product_list_display_correctly(page, added_products_total):
    added_products_total = int(added_products_total)
    edit_page = EditPage(page)
    shopify_page = ShopifyPage(page)
    edit_page.click_on_span_contains_text("View page")
    shopify_page.input_store_password()
    edit_page.click_on_span_contains_text("View page")
    shopify_page.is_product_list_display_correctly(added_products_total)
