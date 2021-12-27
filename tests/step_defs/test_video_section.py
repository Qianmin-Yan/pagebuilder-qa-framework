import json

from pytest_bdd import given, then, parsers, scenarios, when

from pages.edit_page import EditPage
from pages.shopify_page import ShopifyPage

scenarios('../features/video_section.feature')


def test_conftest():
    pass


@when(parsers.parse('the user add youtube video with link "{link}" into the first regular page'))
def add_image_to_first_regular_page(page, link):
    edit_page = EditPage(page)
    edit_page.click_on_first_page_in_page_list()
    edit_page.add_video(link)


@then('the user should see the Published successfully modal pop up')
def check_if_publish_successfully_modal_pop_up(page):
    edit_page = EditPage(page)
    edit_page.is_publish_successfully_modal_pop_up()


@then('the user should see the video shows')
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
    shopify_page.is_vide_show()


@then(parsers.parse('the user is able to play and pause the video in screen {viewport_size}'))
def check_if_user_is_redirected_when_clicking_image(page, viewport_size):
    shopify_page = ShopifyPage(page.context.pages[1])
    viewport_size = json.loads(viewport_size)
    shopify_page.is_video_able_to_be_played(viewport_size)
    shopify_page.is_video_able_to_be_paused()


@when(parsers.parse('the user set the video display ratio "{display_ratio}" and display width "{display_width}'))
def set_video_display_ratio_and_width(page, display_ratio, display_width):
    edit_page = EditPage(page)
    edit_page.set_video_display_ratio_and_width(display_ratio, display_width)
    edit_page.switch_tab("Settings")
    edit_page.publish_page()


@then(parsers.parse('the user will be reminded if the link "{link}" "{is_valid}"'))
def validate_youtube_link(page, link, is_valid):
    edit_page = EditPage(page)
    edit_page.validate_youtube_link(link, is_valid)
