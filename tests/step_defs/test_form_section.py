import time

from pytest_bdd import given, when, then, parsers, scenarios

from pages.edit_page import EditPage
from pages.shopify_page import ShopifyPage

scenarios('../features/form_section.feature')


def test_conftest():
    pass


@given(parsers.parse('the user add form with coupon "{coupon_code}" into the first regular page'))
def add_form_to_first_regular_page(page, coupon_code):
    edit_page = EditPage(page)
    edit_page.click_on_first_page_in_page_list()
    edit_page.add_form_with_coupon(coupon_code)
    edit_page.switch_tab("Settings")
    edit_page.publish_page()


@given('the user add form without coupon into the first regular page')
def add_form_to_first_regular_page(page):
    edit_page = EditPage(page)
    edit_page.click_on_first_page_in_page_list()
    edit_page.add_form_without_coupon()
    edit_page.switch_tab("Settings")
    edit_page.publish_page()


@then('the user should see the Published successfully modal pop up')
def check_if_publish_successfully_modal_pop_up(page):
    edit_page = EditPage(page)
    edit_page.is_publish_successfully_modal_pop_up()


@when(parsers.parse('the user submit form with "{email}"'))
def submit_form(page, email):
    edit_page = EditPage(page)
    # switch tab to shopify store after clicking "view page"
    with page.context.expect_page():
        edit_page.click_on_span_contains_text("View page")
    # switch tab to shopify store after clicking "view page"
    shopify_page = ShopifyPage(page.context.pages[1])
    shopify_page.input_store_password()
    page.context.pages[1].close()
    with page.context.expect_page():
        edit_page.click_on_span_contains_text("View page")
    page.context.pages[1].wait_for_load_state(state="networkidle", timeout=60000)
    shopify_page = ShopifyPage(page.context.pages[1])
    email = email.replace("@", "+_" + time.strftime("%Y%m%d_%H%M%S" + "@"))
    shopify_page.submit_form(email)


@then(parsers.parse('the user should see the coupon "{coupon_code}" is shown'))
def the_user_see_coupon_code(page, coupon_code):
    set_active_tab = page.context.pages.pop(1)
    shopify_page = ShopifyPage(set_active_tab)
    shopify_page.is_coupon_show(coupon_code), "submit form failed"


@then(parsers.parse('the user should see the message "{subscribing_message}" show'))
def see_the_subscribing_message_without_coupon(page, subscribing_message):
    set_active_tab = page.context.pages.pop(1)
    shopify_page = ShopifyPage(set_active_tab)
    shopify_page.is_subscribing_without_coupon_message_show(subscribing_message)
