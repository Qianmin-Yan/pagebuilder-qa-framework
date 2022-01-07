from playwright.sync_api import Error

from constants.contants import USER_NAME, PASSWORD
from locators.automizely_login_locators import LoginPageLocators
from locators.page_builder_base_page_locators import PBBasePageLocators
from pages.base_page import BasePage


class AutomizelyLoginPage(BasePage):

    def login(self, request):
        # with self.page.expect_navigation():
        self.page.goto(request.config.getoption('--base-url'))
        self.page.wait_for_load_state()
        while True:
            if self.page.is_visible(LoginPageLocators.trying_too_often_error):
                self.page.reload()
            elif self.is_element_present_before_timeout(LoginPageLocators.login_btn, timeout=5000) \
                    and self.page.is_disabled(LoginPageLocators.login_btn):
                self.page.fill(LoginPageLocators.email, USER_NAME)
                self.page.fill(LoginPageLocators.password, PASSWORD)
                try:
                    with self.page.expect_navigation():
                        self.page.click(LoginPageLocators.login_btn)
                except Error:
                    pass
            elif self.page.is_visible(LoginPageLocators.return_to_login):
                self.page.click(LoginPageLocators.return_to_login)
            else:
                break

    def is_login(self):
        assert self.is_element_present(PBBasePageLocators.page), "Failed to login"
