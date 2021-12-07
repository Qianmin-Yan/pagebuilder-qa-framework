from locators.regular_page_locators import RegularPageLocators
from pages.base_page import BasePage


class RegularPage(BasePage):

    def create_a_new_page_from_templates(self, template_name):
        self.click_on_element_contains_text(RegularPageLocators.template, template_name)

    def view_page(self, page_name):
        self.click_on_element_contains_text(RegularPageLocators.page_in_page_list, page_name)
