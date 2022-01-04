from constants.contants import USER_NAME, PASSWORD
from locators.automizely_login_locators import LoginPageLocators
from locators.page_builder_base_page_locators import PBBasePageLocators
from pages.base_page import BasePage


class AutomizelyLoginPage(BasePage):

    def login(self):
        with self.page.expect_navigation():
            self.page.goto("/")
        while self.page.is_disabled(LoginPageLocators.login_btn):
            self.page.fill(LoginPageLocators.email, USER_NAME)
            self.page.fill(LoginPageLocators.password, PASSWORD)
        with self.page.expect_navigation():
            self.page.click(LoginPageLocators.login_btn)

    def is_login(self):
        while self.page.is_visible(LoginPageLocators.trying_too_often_error, timeout=1000):
            self.page.reload()
            self.page.fill(LoginPageLocators.password, PASSWORD)
            with self.page.expect_navigation():
                self.page.click(LoginPageLocators.login_btn)
        while self.page.is_visible(LoginPageLocators.return_to_login, timeout=5000):
            with self.page.expect_navigation():
                self.page.click(LoginPageLocators.return_to_login)
            while self.page.is_disabled(LoginPageLocators.login_btn):
                self.page.fill(LoginPageLocators.password, PASSWORD)
            with self.page.expect_navigation():
                self.page.click(LoginPageLocators.login_btn)
        assert self.is_element_present(PBBasePageLocators.page), "Failed to login"
