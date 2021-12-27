from playwright.sync_api import Page

from constants.contants import PASSWORD
from locators.automizely_login_locators import LoginPageLocators
from locators.page_builder_base_page_locators import PBBasePageLocators


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def is_page_logo_visible(self):
        while self.page.is_visible(PBBasePageLocators.return_to_login, timeout=5000):
            self.page.click(PBBasePageLocators.return_to_login)
            self.page.type(LoginPageLocators.password, PASSWORD)
            self.page.click(LoginPageLocators.login_btn)
            self.page.wait_for_timeout(2000)
        assert self.wait_for_selector_state(PBBasePageLocators.page, "visible"), "Failed to login"

    def click_on_span_contains_text(self, text):
        self.page.click(PBBasePageLocators.span_contain_text.format(text))

    def click_on_element_contains_text(self, selector, text):
        self.page.click(selector.format(text))

    def click_on_div_contains_text(self, text):
        self.page.click(PBBasePageLocators.div_contain_text.format(text))

    def click_on_template_in_page_list(self, text):
        self.page.click(PBBasePageLocators.template_in_page_list.format(text))

    def click_on_first_page_in_page_list(self):
        self.page.click(PBBasePageLocators.first_page_in_page_list)

    def view_the_first_page(self):
        self.click_on_span_contains_text("View live page")

    def wait_for_selector_state(self, selector, state):
        locator = self.page.locator(selector)
        locator.wait_for(timeout=30000, state=state)
        return True

    def scroll_into_view(self, selector):
        self.page.wait_for_selector(selector).scroll_into_view_if_needed()

    def element_inside_frame(self, frame_locator, element_locator):
        return self.page.frame_locator(frame_locator).locator(element_locator)
