from locators.shopify_page_locators import ShopifyPageLocators
from pages.base_page import BasePage


class ShopifyPage(BasePage):

    def input_store_password(self):
        if self.is_element_present(ShopifyPageLocators.password):
            self.page.fill(ShopifyPageLocators.password, "123456")
            self.page.click(ShopifyPageLocators.submit)
            pass

    def close_preview_bar(self):
        if self.is_element_present(ShopifyPageLocators.preview_bar_iframe):
            self.page.frame(ShopifyPageLocators.preview_bar_iframe).locator(
                ShopifyPageLocators.close_preview_bar).click()
        else:
            pass

    def submit_form(self, email):
        self.scroll_into_view(ShopifyPageLocators.form_section)
        self.page.fill(ShopifyPageLocators.email_input, email)
        self.page.click(ShopifyPageLocators.subscribe_btn)

    def is_coupon_show(self, coupon_code):
        assert self.is_element_present(ShopifyPageLocators.coupon_code.format(coupon_code))

    def the_email_exists(self, email):
        self.page.click(ShopifyPageLocators.customer_menu)
        self.page.fill(ShopifyPageLocators.find_customer, email)
        return self.page.is_visible(ShopifyPageLocators.customer_search_result)

    def is_product_list_display_correctly(self, added_products_total):
        self.page.wait_for_selector(ShopifyPageLocators.products_added_to_list_section)
        assert len(
            self.page.query_selector_all(ShopifyPageLocators.products_added_to_list_section)) == added_products_total

    def is_subscribing_without_coupon_message_show(self, message):
        assert self.page.wait_for_selector(ShopifyPageLocators.subscribing_message,
                                           state="visible").text_content() == message

    def is_product_detail_display_correctly(self, product_title):
        assert self.page.text_content(
            ShopifyPageLocators.product_title_in_product_detail_section).strip() == product_title, "display wrong product"

    def is_product_in_cart(self, product_title):
        self.page.wait_for_timeout(2000)
        self.page.click(ShopifyPageLocators.cart)
        assert self.page.wait_for_selector(
            ShopifyPageLocators.cart_item_title).text_content() == product_title, "add product to cart failed"

    def click_on_button_contains_text(self, text):
        self.page.wait_for_selector(ShopifyPageLocators.button_contains_text.format(text)).click()

    def is_countdown_timer_show(self):
        assert self.is_element_present(ShopifyPageLocators.countdown_timer_section), "countdown timer didn't appear"

    def is_countdown_timer_in_product_detail_shows(self):
        assert self.is_element_present(
            ShopifyPageLocators.countdown_timer_section_in_product_detail), "countdown timer didn't show"

    def is_image_show(self):
        assert self.is_element_present(ShopifyPageLocators.image_in_image_section), "image didn't show"

    def is_redirected_when_clicking_image_link(self, link):
        with self.page.expect_navigation():
            self.page.click(ShopifyPageLocators.image_in_image_section)
        assert link.strip("/") in self.page.url, "navigation failed"

    def is_vide_show(self):
        assert self.is_element_present(ShopifyPageLocators.youtube_iframe_in_video_section)

    def is_video_able_to_be_played(self, viewport_size):
        self.page.set_viewport_size(viewport_size)
        self.page.reload(wait_until="networkidle")
        youtube_large_play_button = self.element_inside_frame(ShopifyPageLocators.youtube_iframe_in_video_section,
                                                              ShopifyPageLocators.youtube_large_play_button)
        while youtube_large_play_button.is_visible():
            self.page.locator(ShopifyPageLocators.video_section).evaluate('node => node.scrollIntoView(top)')
            youtube_large_play_button.click()
        assert "playing-mode" in self.element_inside_frame(ShopifyPageLocators.youtube_iframe_in_video_section,
                                                           ShopifyPageLocators.youtube_player).get_attribute(
            "class"), "failed to play the youtube video"

    def is_video_able_to_be_paused(self):
        self.element_inside_frame(ShopifyPageLocators.youtube_iframe_in_video_section,
                                  ShopifyPageLocators.youtube_small_play_button).click()
        assert "paused-mode" in self.element_inside_frame(ShopifyPageLocators.youtube_iframe_in_video_section,
                                                          ShopifyPageLocators.youtube_player).get_attribute(
            "class"), "failed to pause the youtube video"
