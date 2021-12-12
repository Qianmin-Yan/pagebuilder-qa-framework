from constants.contants import USER_NAME, PASSWORD
from locators.automizely_login_locators import LoginPageLocators
from pages.base_page import BasePage


class AutomizelyLoginPage(BasePage):

    def login(self):
        self.page.goto("/")
        self.page.wait_for_timeout(3000)
        self.page.click(LoginPageLocators.email)
        self.page.fill(LoginPageLocators.email, USER_NAME)
        self.page.click(LoginPageLocators.password)
        self.page.fill(LoginPageLocators.password, PASSWORD)
        with self.page.expect_navigation():
            self.page.click(LoginPageLocators.login_btn)
