import time

from locators.edit_page_locators import EditPageLocators
from pages.automizely_login_page import AutomizelyLoginPage


def test_publish_page(page):
    automizely_login_page = AutomizelyLoginPage(page)
    automizely_login_page.login()
    page.wait_for_load_state()
    page.click("text=Christmas 01 page_list")
    page.click("text=PublishedUnpublished >> span span span")
    page.click("button:has-text('Save')")
    assert page.text_content("span[aria-label='congratulate']") == "🎉Published successfully!"
    # add product list
    page.click("button:has-text('Later')")
    page.click("text=Page 24Success Publishedpages/page-24")
    page.click("[aria-label='Content config']")
    page.click("div[role='button']:has-text('Add section')")
    # scroll product list section into view
    page.query_selector("h2:has-text('Sales boost')").scroll_into_view_if_needed()
    page.dispatch_event("text=Product listAdd >> button", "click")
    page.click("button:has-text('Add products')")
    i = 1
    while i < 4:
        page.click(EditPageLocators.checkbox_in_product_chosen_modal.format(i))
        i = i + 1
    page.click("text=3 selected productsAdd >> button")
    breakpoint()
    page.click("[aria-label='back']")
    page.click("[aria-label='Settings']")
    page.click("button:has-text('Save')")
    time.sleep(30)
    # with page.expect_popup() as popup_info:
    #     page.click("button:has-text('View page')")
    # page1 = popup_info.value
    # page1.click("input[name='password']")
    # page1.fill("input[name='password']", "123456")
    # page1.click("button:has-text('Enter')")
    # page1.close()
    #
    # # Click button:has-text("View page")
    # with page.expect_popup() as popup_info:
    #     page.click("button:has-text('View page')")
    # page2 = popup_info.value
    # page2.click(
    #     "#automizely_page_builder_content >> :nth-match(div:has-text('You might also like test20055 $20,154.00 Buy now test20052 $20,151.00 Buy now te'), 4)")
    # page.click("button:has-text('Later')")
    # page.click("text=Page 4Success Publishedpages/page-4")
    # page.click("[aria-label='Content config']")
    # page.click("div[role='button']:has-text('Form')")
    # page.fill("#PolarisRadioButton28", "customCoupon")
    # page.click("text=Shopify discount code")
    # page.click("input[name='presentation_settings.items[7].data.couponCode']")
    # page.fill("input[name='presentation_settings.items[7].data.couponCode']", "test_coupon")
    # page.click("button:has-text('Save')")
    # with page.expect_popup() as popup_info:
    #     page.click("button:has-text('View page')")
    # page3 = popup_info.value
    #
    # context.close()
    # browser.close()
