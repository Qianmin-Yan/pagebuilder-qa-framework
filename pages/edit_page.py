import random

from constants.contants import DATA_KEEPER
from locators.edit_page_locators import EditPageLocators
from pages.base_page import BasePage
from utils.date_utils import is_today_the_last_day_in_current_month


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
        self.page.wait_for_timeout(1000)
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
        self.page.wait_for_timeout(1000)
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

    def add_product_detail_with_coutndown_timer_to_regular_page(self):
        self.switch_tab("Content")
        self.add_section("Product", "Product detail")
        self.assign_product_to_product_detail()
        DATA_KEEPER['product_title'] = self.get_added_product_title()
        self.enable_countdown_timer_in_product_detail()
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

    def add_countdown_timer(self):
        self.switch_tab("Content")
        self.page.wait_for_timeout(1000)
        if self.page.is_visible(EditPageLocators.span_contain_text.format("Countdown timer")):
            self.click_on_span_contains_text("Countdown timer")
        else:
            self.add_section("Sales boost", "Countdown timer")
        self.scroll_into_view(":nth-match([class='Polaris-Connected'],2)")
        self.page.click(":nth-match([class='Polaris-Connected'],2)")
        self.page.click(EditPageLocators.today)
        self.page.select_option(selector=EditPageLocators.time_selector, value="00:00:00")
        self.page.click(":nth-match([class='Polaris-Connected'],3)")
        if is_today_the_last_day_in_current_month():
            self.page.click(EditPageLocators.next_month_button)
            self.page.click(EditPageLocators.first_day_in_month)
        else:
            self.page.click(EditPageLocators.tomorrow)
        self.page.click(EditPageLocators.back_button)

    def add_image(self, link):
        self.switch_tab("Content")
        self.add_section("Media", "Image")
        self.upload_image()
        self.page.type(EditPageLocators.destination_url, link)
        self.page.click(EditPageLocators.back_button)

    def add_video(self, link):
        self.switch_tab("Content")
        self.page.wait_for_timeout(1000)
        if len(self.page.query_selector_all(EditPageLocators.span_contain_text.format("Video"))) > 0:
            while len(self.page.query_selector_all(EditPageLocators.span_contain_text.format("Video"))) > 1:
                self.page.click(EditPageLocators.video_section_delete_button, force=True)
            self.click_on_span_contains_text("Video")
        else:
            self.add_section("Media", "Video")
        self.page.fill(EditPageLocators.video_link, link)

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
        self.page.click(EditPageLocators.add_section.format(section_name), force=True)

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

    def wait_for_page_list_counted(self):
        self.wait_for_selector_state(EditPageLocators.page_list_counted, "visible")

    def upload_image(self):
        self.click_on_span_contains_text("Remove")
        # the file path is based on the runner path
        self.page.set_input_files(selector="//input[@type='file']", files="./test_data/test.gif")

    def enable_countdown_timer_in_product_detail(self):
        self.scroll_into_view(EditPageLocators.div_contain_text.format("Sales boost"))
        self.click_on_div_contains_text("Sales boost")
        self.scroll_into_view(EditPageLocators.h3_contain_text.format("Countdown timer"))
        self.page.check(EditPageLocators.show_countdown_timer_btn)

    def set_video_display_ratio_and_width(self, display_ratio, display_width):
        self.scroll_into_view(EditPageLocators.display_width_label)
        self.page.select_option(selector=EditPageLocators.display_ratio_option, label=display_ratio)
        self.page.select_option(selector=EditPageLocators.display_width_option, label=display_width)
        self.page.click(EditPageLocators.back_button)

    def validate_youtube_link(self, link, is_valid):
        # lose focus to trigger the validation
        self.page.click(EditPageLocators.h3_contain_text.format("Video"))
        if is_valid == "invalid" and link != "":
            assert self.page.is_visible(
                "text=Enter a valid YouTube URL"), "URL validation issue, invalid link take as valid link"
        elif is_valid == "invalid" and link == "":

            assert self.page.is_visible(
                "text=This field is required"), "URL validation issue, this field is required, but no error shows"
        elif is_valid == "valid":
            assert self.page.is_enabled(
                EditPageLocators.span_contain_text.format(
                    "Save")), "URL validation issue, valid link take as invalid link"
