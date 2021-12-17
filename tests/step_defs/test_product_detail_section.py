from pytest_bdd import when, then, parsers, scenarios, given

from constants.contants import DATA_KEEPER
from pages.shopify_page import ShopifyPage
from locators.edit_page_locators import EditPageLocators
from pages.edit_page import EditPage
from pages.base_page import BasePage

scenarios('../features/product_detail_section.feature')


def test_conftest():
    pass


@given(parsers.parse('the user click on menu "{page_type}"'))
def the_user_click_on_menu(page, page_type):
    pb_base_page = BasePage(page)
    pb_base_page.click_on_span_contains_text(page_type)


@when(parsers.parse('the user add product detail into the blank "{page_type}" with random product'))
def add_product_detail_into_first_page(page, page_type):
    edit_page = EditPage(page)
    DATA_KEEPER["page_type"] = page_type
    edit_page.create_blank_page(page_type)
    if page_type in ["Collection pages", "Product pages"]:
        edit_page.add_product_detail_with_random_product_to_product_collection_page(page_type)
    else:
        edit_page.add_product_detail_with_random_product_to_regular_home_blogPost_page()
    edit_page.switch_tab("Settings")
    edit_page.publish_page()
    if page_type == "Home page":
        page.wait_for_timeout(500)
        if edit_page.page.is_visible(EditPageLocators.confirm_to_publish_home_page_modal):
            edit_page.click_on_span_contains_text("Confirm")


@then('the user should see the Published successfully modal pop up')
def check_if_publish_successfully_modal_pop_up(page):
    edit_page = EditPage(page)
    edit_page.is_publish_successfully_modal_pop_up(), "publish page failed"


@then(parsers.parse('the user is able to see the same product in "{page_type}"'))
def check_if_product_detail_display_correctly(page, page_type):
    edit_page = EditPage(page)
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
    shopify_page.is_product_detail_display_correctly(DATA_KEEPER.get("product_title"))


@when(parsers.parse('the user click on "{button_name}"'))
def click_button(page, button_name):
    shopify_page = ShopifyPage(page.context.pages[1])
    if button_name == "Buy it now":
        with shopify_page.page.expect_navigation():
            shopify_page.click_on_button_contains_text(button_name)
    else:
        shopify_page.click_on_button_contains_text(button_name)


@then("the product appeared in cart")
def check_if_add_to_cart_success(page):
    shopify_page = ShopifyPage(page.context.pages[1])
    shopify_page.is_product_in_cart(DATA_KEEPER.get("product_title"))
    shopify_page.page.go_back()


@then("the user is navigated to checkout page")
def is_navigated_to_checkout_page(page):
    page = page.context.pages[1]
    assert "checkouts" in page.url, "checkout failed"
