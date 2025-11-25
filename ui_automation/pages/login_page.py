from playwright.sync_api import Page, expect
from ui_automation.pages import locators
from utils.logger import Logger

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.log = Logger()

    def open(self):
        self.log.info("Opening login page: https://mail.ukr.net/")
        self.page.goto("https://mail.ukr.net/")

    def login(self, username: str, password: str):
        self.log.info(f"Filling username: {username}")
        self.page.fill(locators.login_field, username)

        self.log.info("Filling password")
        self.page.fill(locators.password_field, password)

        self.log.info("Clicking submit button")
        self.page.click(locators.submit_button)

        self.log.info("Waiting for compose button to be visible")
        expect(self.page.locator(locators.compose_button)).to_be_visible(timeout=10000)
        self.log.info("Login successful, compose button visible")
