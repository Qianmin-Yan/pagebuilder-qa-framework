
class LoginPageLocators:
    """
    Login page locators
    """
    email = "//input[@name='username']"
    password = "//input[@name='password']"
    login_btn = "#submit-button"
    trying_too_often_error = "div:has-text('You are trying too often. Please reopen the page try again later.')"
    return_to_login = "//a[text()='Return to log in']"




