from playwright.sync_api import Page
from locators.page_builder_base_page_locators import PBBasePageLocators
from playwright.sync_api import TimeoutError


class BasePage:

    def __init__(self, page: Page):
        self.page = page

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

    def is_selector_state_matched(self, selector, state):
        try:
            self.page.locator(selector).wait_for(timeout=30000, state=state)
            return True
        except TimeoutError:
            return False

    def scroll_into_view(self, selector):
        self.page.wait_for_selector(selector).scroll_into_view_if_needed()

    def element_inside_frame(self, frame_locator, element_locator):
        return self.page.frame_locator(frame_locator).locator(element_locator)

    def is_element_present(self, selector) -> bool:
        try:
            self.page.wait_for_selector(selector)
            return True
        except TimeoutError:
            return False

    def is_element_present_before_timeout(self, selector, timeout) -> bool:
        try:
            self.page.wait_for_selector(selector, timeout=timeout)
            return True
        except TimeoutError:
            return False
