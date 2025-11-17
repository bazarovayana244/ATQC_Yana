import re
from playwright.sync_api import expect
from ui_automation.pages.login_page import LoginPage
from ui_automation.pages import locators
from utils.browser_factory import BrowserFactory
from utils.logger import Logger

class TestLogin:
    def test_successful_login(self):
        log = Logger()
        log.info("Starting test_successful_login")

        browser, pw = BrowserFactory.get_browser(
            browser_name="chrome",
            headless=False,
            viewport={"width": 1920, "height": 1080}
        )

        page = browser.new_page()
        login_page = LoginPage(page)

        login_page.open()
        login_page.login("test.playwright@ukr.net", "q!RamZWyGBa4Z!j")

        expect(page).to_have_url(re.compile(r"https://mail\.ukr\.net/desktop/.*"), timeout=10000)
        assert "desktop" in page.url, f"Expected 'desktop' in URL, got {page.url}"

        compose_btn = page.locator(locators.compose_button)
        expect(compose_btn).to_be_visible(timeout=10000)
        assert compose_btn.is_visible(), "Compose button is not visible after login"

        log.info("Login successful")

        log.info("Closing browser")
        browser.close()
        pw.stop()
