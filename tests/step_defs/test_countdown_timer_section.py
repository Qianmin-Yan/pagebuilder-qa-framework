from pytest_bdd import given, then, scenarios

from pages.edit_page import EditPage
from pages.shopify_page import ShopifyPage

scenarios('../features/countdown_timer_section.feature')


def test_conftest():
    pass


@given('the user add countdown timer into the first regular page')
def add_form_to_first_regular_page(page):
    edit_page = EditPage(page)
    edit_page.click_on_first_page_in_page_list()
    edit_page.add_countdown_timer()
    edit_page.switch_tab("Settings")
    edit_page.publish_page()


@then('the user should see the Published successfully modal pop up')
def check_if_publish_successfully_modal_pop_up(page):
    edit_page = EditPage(page)
    edit_page.is_publish_successfully_modal_pop_up()


@then('the user should see the countdown timer shows')
def check_if_countdown_timer_shows(page):
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
    shopify_page.is_countdown_timer_show()
