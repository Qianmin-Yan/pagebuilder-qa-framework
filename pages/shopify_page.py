import time

from locators.shopify_page_locators import ShopifyPageLocators
from pages.base_page import BasePage


class ShopifyPage(BasePage):

    def input_store_password(self):
        if self.wait_for_selector_state(ShopifyPageLocators.password, "visible"):
            print("find element password input")
            self.page.fill(ShopifyPageLocators.password, "123456")
            self.page.click(ShopifyPageLocators.submit)
        else:
            print("didn't find element password input")
            pass

    def close_preview_bar(self):
        if self.page.is_visible(ShopifyPageLocators.preview_bar_iframe):
            self.page.frame(ShopifyPageLocators.preview_bar_iframe).locator(
                ShopifyPageLocators.close_preview_bar).click()
        else:
            pass

    def submit_form(self, email):
        self.page.fill(ShopifyPageLocators.email_input, email)
        self.page.click(ShopifyPageLocators.subscribe_btn)

    def is_element_exists(self, coupon_code):
        assert self.wait_for_selector_state(ShopifyPageLocators.coupon_code.format(coupon_code), "visible")

    def the_email_exists(self, email):
        self.page.click(ShopifyPageLocators.customer_menu)
        self.page.fill(ShopifyPageLocators.find_customer, email)
        return self.page.is_visible(ShopifyPageLocators.customer_search_result)

    def is_product_list_display_correctly(self, added_products_total):
        assert len(
            self.page.query_selector_all(ShopifyPageLocators.products_added_to_list_section)) == added_products_total
