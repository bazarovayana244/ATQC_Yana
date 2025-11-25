import re
from playwright.sync_api import expect
from ui_automation.pages.login_page import LoginPage
from ui_automation.pages import locators
from utils.logger import Logger

class TestLogin:

    def test_successful_login(self, browser_page):
        log = Logger()
        log.info("Start test_successful_login")

        page = browser_page
        login_page = LoginPage(page)

        login_page.open()
        login_page.login("test.playwright@ukr.net", "q!RamZWyGBa4Z!j")

        expect(page).to_have_url(re.compile(r"https://mail\.ukr\.net/desktop/.*"))

        compose_btn = page.locator(locators.compose_button)
        expect(compose_btn).to_be_visible(timeout=10000)
        assert compose_btn.is_visible()

        log.info("Login successful")
