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

    def assign_product_or_collection(self, page_type):
        if page_type == "Product pages":
            self.click_on_span_contains_text("Select products")
        else:
            self.click_on_span_contains_text("Select collections")
        self.page.click(EditPageLocators.checkbox_button_in_product_chosen_modal.format(1))
        self.click_on_span_contains_text("Add")

    def add_product_list_with_products(self, added_products_total):
        self.page.click(EditPageLocators.content_tab)
        self.page.wait_for_timeout(2000)
        if self.page.is_visible(EditPageLocators.span_contain_text.format("Product list")):
            self.click_on_span_contains_text("Product list")
            if self.page.is_visible(EditPageLocators.added_product_in_product_list):
                while self.page.is_visible(EditPageLocators.delete_button):
                    self.page.click(EditPageLocators.delete_button)
        else:
            self.click_on_span_contains_text("Add section")
            self.page.wait_for_selector("h2:has-text('Sales boost')").scroll_into_view_if_needed()
            self.page.dispatch_event("text=Product listAdd >> button", "click")

        self.click_on_span_contains_text("Add products")
        for i in range(0, added_products_total):
            self.page.click(EditPageLocators.checkbox_button_in_product_chosen_modal.format(i + 1))
        self.click_on_span_contains_text("Add")
        self.page.click(EditPageLocators.back_button)

    def switch_tab(self, tab_name):
        if tab_name == "Settings":
            self.page.click(EditPageLocators.settings_tab)
        elif tab_name == "Content":
            self.page.click(EditPageLocators.settings_tab)
        elif tab_name == "Style":
            self.page.click(EditPageLocators.style_tab)

    def add_form_with_coupon(self):
        self.page.click(EditPageLocators.content_tab)
        self.page.wait_for_timeout(2000)
        if self.page.is_visible(EditPageLocators.span_contain_text.format("Form")):
            self.click_on_span_contains_text("Form")
            if self.page.is_checked(EditPageLocators.form_without_coupon_option):
                self.page.click(EditPageLocators.form_with_coupon_option)
                self.page.fill(EditPageLocators.form_coupon_input, "test")
        else:
            self.click_on_span_contains_text("Add section")
            self.page.dispatch_event("text=FormAdd >> button", "click")
            self.page.click(EditPageLocators.form_with_coupon_option)
            self.page.fill(EditPageLocators.form_coupon_input, "test")
        self.page.click(EditPageLocators.back_button)

    def view_live_page(self):
        self.click_on_span_contains_text("View live page")

    def add_product_detail_with_random_product(self):
        self.page.click(EditPageLocators.content_tab)
        self.page.wait_for_timeout(2000)
        if self.page.is_visible(EditPageLocators.span_contain_text.format("Product detail")):
            self.click_on_span_contains_text("Product detail")
            if self.page.is_visible(EditPageLocators.added_product_in_product_detail):
                self.click_on_span_contains_text("Change product")
            else:
                self.click_on_span_contains_text("Select product")
        else:
            self.click_on_span_contains_text("Add section")
            self.page.dispatch_event("text=Product detailAdd >> button", "click")
            self.click_on_span_contains_text("Select product")
        # enable force click, avoiding the click event intercepts by the ancestor element
        while self.page.is_disabled(EditPageLocators.span_contain_text.format("Add")):
            self.page.wait_for_selector(
                EditPageLocators.radio_button_in_product_chosen_modal.format(random.randint(1, 8)),
                state="visible").click(force=True)
        self.click_on_span_contains_text("Add")
        DATA_KEEPER['product_title'] = self.get_added_product_title()
        self.page.click(EditPageLocators.back_button)

    def get_added_product_title(self):
        return self.page.text_content(EditPageLocators.added_product_title)

    def get_added_products_title(self):
        products_title = []
        for product in self.page.query_selector_all(EditPageLocators.added_product_title):
            products_title.append(product.text_content())

    def add_product_detail_with_random_product_to_product_page(self):
        while self.page.is_visible(EditPageLocators.delete_button):
            self.page.click(EditPageLocators.delete_button)
        self.click_on_span_contains_text("Select products")
        self.page.click(EditPageLocators.checkbox_button_in_product_chosen_modal.format(random.randint(1, 8)))
        self.click_on_span_contains_text("Add")
        DATA_KEEPER['product_title'] = self.get_added_product_title()
