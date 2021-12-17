import random

from constants.contants import DATA_KEEPER
from locators.edit_page_locators import EditPageLocators
from pages.base_page import BasePage


class EditPage(BasePage):

    def publish_page(self):
        self.page.click(EditPageLocators.publish_btn)
        self.page.click(EditPageLocators.save_btn)

    def back_to_page_list(self):
        self.page.wait_for_selector(EditPageLocators.done_it_btn).click()

    def get_page_name(self):
        return self.page.get_attribute(EditPageLocators.page_name, "value")

    def is_publish_successfully_modal_pop_up(self):
        assert self.wait_for_selector_state(selector=EditPageLocators.publish_successfully_modal,
                                            state='visible'), "publish page failed"

    def assign_product_or_collection_for_page_creation(self, page_type):
        if page_type == "Product pages":
            self.click_on_span_contains_text("Select products")
        else:
            self.click_on_span_contains_text("Select collections")
        self.page.click(EditPageLocators.checkbox_button_in_product_chosen_modal.format(1))
        self.click_on_span_contains_text("Add")

    def add_product_list_with_products(self, added_products_total):
        self.switch_tab("Content")
        self.page.wait_for_timeout(1000)
        if self.page.is_visible(EditPageLocators.span_contain_text.format("Product list")):
            self.click_on_span_contains_text("Product list")
            if self.page.is_visible(EditPageLocators.added_product_in_product_list):
                while self.page.is_visible(EditPageLocators.delete_button):
                    self.page.click(EditPageLocators.delete_button)
        else:
            self.add_section("Sales boost", "Product list")
        self.assign_product_to_product_list(added_products_total)
        self.page.click(EditPageLocators.back_button)

    def switch_tab(self, tab_name):
        if tab_name == "Settings":
            self.page.click(EditPageLocators.settings_tab)
        elif tab_name == "Content":
            self.page.click(EditPageLocators.content_tab)
        elif tab_name == "Style":
            self.page.click(EditPageLocators.style_tab)

    def add_form_with_coupon(self, coupon_code):
        self.switch_tab("Content")
        self.page.wait_for_timeout(2000)
        if self.page.is_visible(EditPageLocators.span_contain_text.format("Form")):
            self.click_on_span_contains_text("Form")
            if self.page.is_checked(EditPageLocators.form_without_coupon_option):
                self.page.click(EditPageLocators.form_with_coupon_option)
                self.page.fill(EditPageLocators.form_coupon_input, coupon_code)
        else:
            self.add_section("Form", "Form")
            self.page.click(EditPageLocators.form_with_coupon_option)
            self.page.fill(EditPageLocators.form_coupon_input, coupon_code)
        self.page.click(EditPageLocators.back_button)

    def add_form_without_coupon(self):
        self.page.click(EditPageLocators.content_tab)
        self.page.wait_for_timeout(2000)
        if self.page.is_visible(EditPageLocators.span_contain_text.format("Form")):
            self.click_on_span_contains_text("Form")
            if self.page.is_checked(EditPageLocators.form_with_coupon_option):
                self.page.click(EditPageLocators.form_without_coupon_option)
        else:
            self.add_section("Form", "Form")
        self.page.click(EditPageLocators.back_button)

    def view_live_page(self):
        self.click_on_span_contains_text("View live page")

    def add_product_detail_with_random_product_to_regular_home_blogPost_page(self):
        self.switch_tab("Content")
        self.add_section("Product", "Product detail")
        self.assign_product_to_product_detail()
        DATA_KEEPER['product_title'] = self.get_added_product_title()
        self.enable_buy_now_btn()
        self.page.click(EditPageLocators.back_button)

    def add_product_detail_with_random_product_to_product_collection_page(self, page_type):
        self.assign_product_or_collection_for_page_creation(page_type)
        if page_type == "Product pages":
            DATA_KEEPER['product_title'] = self.get_added_product_title()
            self.switch_tab("Content")
            self.add_section("Product", "Product detail")
        else:
            self.switch_tab("Content")
            self.add_section("Product", "Product detail")
            self.assign_product_to_product_detail()
            DATA_KEEPER['product_title'] = self.get_added_product_title()
        self.enable_buy_now_btn()
        self.page.click(EditPageLocators.back_button)

    def get_added_product_title(self):
        return self.page.text_content(EditPageLocators.added_product_title)

    def get_added_products_title(self):
        products_title = []
        for product in self.page.query_selector_all(EditPageLocators.added_product_title):
            products_title.append(product.text_content())

    def assign_product_to_product_detail(self):
        self.click_on_span_contains_text("Select product")
        # enable force click, avoiding the click event intercepts by the ancestor element
        while self.page.is_disabled(EditPageLocators.span_contain_text.format("Add")):
            self.page.wait_for_selector(
                EditPageLocators.radio_button_in_product_chosen_modal.format(random.randint(1, 8)),
                state="visible").click(force=True)
        self.click_on_span_contains_text("Add")

    def assign_product_to_product_list(self, added_products_total):
        self.click_on_span_contains_text("Add products")
        for i in range(0, added_products_total):
            self.page.click(EditPageLocators.checkbox_button_in_product_chosen_modal.format(i + 1))
        self.click_on_span_contains_text("Add")

    def add_section(self, modal_name, section_name, ):
        self.click_on_span_contains_text("Add section")
        self.page.locator("h2:has-text('{}')".format(modal_name)).scroll_into_view_if_needed()
        self.page.dispatch_event("text={}Add >> button".format(section_name), "click")

    def enable_buy_now_btn(self):
        self.page.locator(EditPageLocators.buy_now_btn).scroll_into_view_if_needed()
        if self.page.is_checked(EditPageLocators.buy_now_btn):
            pass
        else:
            self.page.wait_for_timeout(1000)
            self.page.click(EditPageLocators.buy_now_btn, force=True)

    def create_blank_page(self, page_type):
        if page_type in ["Collection pages", "Blog post pages"]:
            self.page.click("text=Create a blank page")
        else:
            self.page.click("text=Create a page")
            self.page.click("//span[text()='Create']")
