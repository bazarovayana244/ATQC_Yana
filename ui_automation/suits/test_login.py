import pytest
from playwright.sync_api import expect
from ui_automation.pages.login_page import LoginPage
from ui_automation.pages import locators

@pytest.mark.usefixtures("page")
class TestLogin:

    def test_successful_login(self, page):
        login_page = LoginPage(page)

        login_page.open()
        login_page.login("test.playwright@ukr.net", "q!RamZWyGBa4Z!j")
        expect(page).to_have_url("https://mail.ukr.net/desktop*", timeout=10000)

        assert "desktop" in page.url, f"Expected 'desktop' in URL, got {page.url}"

        compose_btn = page.locator(locators.compose_button)
        expect(compose_btn).to_be_visible(timeout=10000)

        assert compose_btn.is_visible(), "Compose button is not visible after login"

        print("Login successful")
