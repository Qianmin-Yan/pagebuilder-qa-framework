from locators.shopify_page_locators import ShopifyPageLocators
from pages.base_page import BasePage


class ShopifyPage(BasePage):

    def input_store_password(self):
        if self.wait_for_selector_state(ShopifyPageLocators.password, "visible"):
            self.page.fill(ShopifyPageLocators.password, "123456")
            self.page.click(ShopifyPageLocators.submit)
            pass

    def close_preview_bar(self):
        if self.page.is_visible(ShopifyPageLocators.preview_bar_iframe):
            self.page.frame(ShopifyPageLocators.preview_bar_iframe).locator(
                ShopifyPageLocators.close_preview_bar).click()
        else:
            pass

    def submit_form(self, email):
        self.scroll_into_view(ShopifyPageLocators.form_section)
        self.page.fill(ShopifyPageLocators.email_input, email)
        self.page.click(ShopifyPageLocators.subscribe_btn)

    def is_coupon_show(self, coupon_code):
        assert self.wait_for_selector_state(ShopifyPageLocators.coupon_code.format(coupon_code), "visible")

    def the_email_exists(self, email):
        self.page.click(ShopifyPageLocators.customer_menu)
        self.page.fill(ShopifyPageLocators.find_customer, email)
        return self.page.is_visible(ShopifyPageLocators.customer_search_result)

    def is_product_list_display_correctly(self, added_products_total):
        assert len(
            self.page.query_selector_all(ShopifyPageLocators.products_added_to_list_section)) == added_products_total

    def is_subscribing_without_coupon_message_show(self, message):
        assert self.page.wait_for_selector(ShopifyPageLocators.subscribing_message,
                                           state="visible").text_content() == message

    def is_product_detail_display_correctly(self, product_title):
        self.scroll_into_view(ShopifyPageLocators.product_detail_section)
        assert self.page.text_content(
            ShopifyPageLocators.product_title_in_product_detail_section).strip() == product_title, "display wrong product"

    def is_product_in_cart(self, product_title):
        self.page.wait_for_timeout(1000)
        self.page.click(ShopifyPageLocators.cart)
        assert self.page.wait_for_selector(ShopifyPageLocators.cart_item_title).text_content() == product_title, "add product to cart failed"

    def click_on_button_contains_text(self, text):
        self.page.click(ShopifyPageLocators.button_contains_text.format(text))
