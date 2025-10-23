from playwright.sync_api import Page, expect
from ui_automation.pages import locators

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto("https://mail.ukr.net/")

    def login(self, username: str, password: str):
        self.page.fill(locators.login_field, username)
        self.page.fill(locators.password_field, password)
        self.page.click(locators.submit_button)

        expect(self.page.locator(locators.compose_button)).to_be_visible(timeout=10000)
