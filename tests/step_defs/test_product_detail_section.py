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


@when(parsers.parse('the user add product detail into the first "{page_type}" with random product'))
def add_product_detail_into_first_page(page, page_type):
    edit_page = EditPage(page)
    edit_page.click_on_first_page_in_page_list()
    edit_page.add_product_detail_with_random_product()
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
    # switch tab to shopify store after clicking "view page"
    with page.context.expect_page() as new_page_info:
        edit_page.click_on_span_contains_text("View page")
    new_page = new_page_info.value
    shopify_page = ShopifyPage(new_page)
    shopify_page.input_store_password()
    if page_type == "Home page":
        new_page.wait_for_load_state()
    else:
        shopify_page.page.close()
        # switch tab to shopify store after clicking "view page"
        with page.context.expect_page() as new_page_info:
            edit_page.click_on_span_contains_text("View page")
        new_page = new_page_info.value
        # waiting for page loading, otherwise will return "NoneType" error
        new_page.wait_for_load_state()
        shopify_page = ShopifyPage(new_page)
    shopify_page.is_product_detail_display_correctly(DATA_KEEPER.get("product_title"))


@when('the user add product detail into the first product page with random product')
def add_product_detail_into_product_page_with_random_product(page):
    edit_page = EditPage(page)
    edit_page.click_on_first_page_in_page_list()
    edit_page.add_product_detail_with_random_product_to_product_page()
    edit_page.switch_tab("Settings")
    edit_page.publish_page()
