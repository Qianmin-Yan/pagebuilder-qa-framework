from constants.contants import USER_NAME, PASSWORD
from locators.automizely_login_locators import LoginPageLocators
from pages.base_page import BasePage


class AutomizelyLoginPage(BasePage):

    def login(self):
        self.page.goto("/")
        self.page.wait_for_timeout(1000)
        self.page.wait_for_selector(LoginPageLocators.email).fill(USER_NAME)
        self.page.wait_for_selector(LoginPageLocators.password).fill(PASSWORD)
        with self.page.expect_navigation():
            self.page.click(LoginPageLocators.login_btn)
