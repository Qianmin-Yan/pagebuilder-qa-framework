import time

from locators.shopify_page_locators import ShopifyPageLocators
from pages.base_page import BasePage


class ShopifyPage(BasePage):

    def input_store_password(self):
        if self.page.is_visible(ShopifyPageLocators.password):
            self.page.fill(ShopifyPageLocators.password, "123456")
            self.page.click(ShopifyPageLocators.submit)
        else:
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

    def is_element_exist(self, coupon_code):
        time.sleep(1)
        return self.page.is_visible(ShopifyPageLocators.coupon_code.format(coupon_code))

    def the_email_exists(self, email):
        self.page.click(ShopifyPageLocators.customer_menu)
        self.page.fill(ShopifyPageLocators.find_customer, email)
        return self.page.is_visible(ShopifyPageLocators.customer_search_result)

    def is_product_list_display_correctly(self, added_products_total):
        assert len(
            self.page.query_selector_all(ShopifyPageLocators.products_added_to_list_section)) == added_products_total
