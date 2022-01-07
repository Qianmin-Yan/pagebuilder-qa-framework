import os

import allure
import pytest
from playwright.sync_api import sync_playwright
from pytest_bdd import parsers, given, then

from pages.automizely_login_page import AutomizelyLoginPage


@given(parsers.parse('I navigate to PageBuilder website with valid credential'), target_fixture="login")
def login(page, request):
    login_page = AutomizelyLoginPage(page)
    login_page.login(request)


@then(parsers.parse('I should see the PageBuilder logo'), target_fixture="verify login")
def verify_page_title(page):
    login_page = AutomizelyLoginPage(page)
    login_page.is_login()


@pytest.fixture()
def page(request):
    with sync_playwright() as play:
        if os.getenv('DOCKER_RUN') or os.getenv('GITHUB_RUN') or not request.config.getoption('--headed'):
            browser = play.chromium.launch(headless=True, args=['--no-sandbox'])
        else:
            browser = play.chromium.launch(headless=False)
        page = browser.new_page()
        global PAGE
        PAGE = page
        yield page
        browser.close()


PAGE = None


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport():
    outcome = yield
    test_result = outcome.get_result()

    if test_result.when in ["setup", "call"]:
        # screenshot for only fail case
        # xfail = hasattr(test_result, 'wasxfail')
        # if test_result.failed or (test_result.skipped and xfail):
        global PAGE
        if PAGE:
            for page in PAGE.context.pages:
                allure.attach(page.screenshot(), name='screenshot', attachment_type=allure.attachment_type.PNG)
                allure.attach(page.content(), name='html_source', attachment_type=allure.attachment_type.HTML)
