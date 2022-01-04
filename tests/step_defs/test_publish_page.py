from pytest_bdd import given, when, then, parsers, scenarios, scenario

from constants.contants import DATA_KEEPER
from locators.edit_page_locators import EditPageLocators
from pages.base_page import BasePage
from pages.edit_page import EditPage
from utils.request_utils import delete_all_pages, get_admin_api_base_url, get_headers

scenarios('../features/publish_page.feature')


def test_conftest():
    pass


@given(parsers.parse('the user click on menu "{page_type}"'))
def the_user_click_on_menu(request, page, page_type):
    pb_base_page = BasePage(page)
    DATA_KEEPER['page_type'] = page_type
    DATA_KEEPER["admin_api_base_url"] = get_admin_api_base_url(request)
    page.on("request", lambda r: get_headers(r))
    pb_base_page.click_on_span_contains_text(page_type)


@when(parsers.parse('the user choose from template "{template_name}" to publish "{page_type}"'))
def publish_page_from_template(page, template_name, page_type):
    edit_page = EditPage(page)
    # wait for getting created pages length, avoid to create page in duplicated page url
    edit_page.wait_for_page_list_counted()
    edit_page.click_on_template_in_page_list(template_name)
    if page_type in ["Product pages", "Collection pages"]:
        edit_page.assign_product_or_collection_for_page_creation(page_type)
    edit_page.publish_page()
    if page_type == "Home page":
        page.wait_for_timeout(500)
        if edit_page.page.is_visible(EditPageLocators.confirm_to_publish_home_page_modal):
            edit_page.click_on_span_contains_text("Confirm")


@then('the user should see the Published successfully modal pop up')
def check_if_publish_successfully_modal_pop_up(page):
    edit_page = EditPage(page)
    edit_page.is_publish_successfully_modal_pop_up()


def teardown_function():
    headers = DATA_KEEPER.get("headers")
    page_type = DATA_KEEPER.get("page_type")
    page_type = page_type.lower().replace(" ", "-").rstrip('s')
    get_delete_pages_url = DATA_KEEPER.get("admin_api_base_url") + "/pages"
    unpublish_url = DATA_KEEPER.get("admin_api_base_url") + "/pages/{page_id}/unpublish.action"
    delete_all_pages(get_delete_pages_url, unpublish_url, page_type, headers=headers)
