from pytest_bdd import given, then, parsers, scenarios

from pages.edit_page import EditPage
from pages.shopify_page import ShopifyPage

scenarios('../features/image_section.feature')


def test_conftest():
    pass


@given(parsers.parse('the user add image with link "{link}" into the first regular page'))
def add_image_to_first_regular_page(page, link):
    edit_page = EditPage(page)
    edit_page.click_on_first_page_in_page_list()
    edit_page.add_image(link)
    edit_page.switch_tab("Settings")
    edit_page.publish_page()


@then('the user should see the Published successfully modal pop up')
def check_if_publish_successfully_modal_pop_up(page):
    edit_page = EditPage(page)
    edit_page.is_publish_successfully_modal_pop_up()


@then('the user should see the image shows')
def check_if_image_shows(page):
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
    shopify_page.is_image_show()


@then(parsers.parse('the user will be redirected to "{link}" in current page when clicking on image'))
def check_if_user_is_redirected_when_clicking_image(page, link):
    shopify_page = ShopifyPage(page.context.pages[1])
    shopify_page.is_redirected_when_clicking_image_link(link)