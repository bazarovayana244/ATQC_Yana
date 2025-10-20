from playwright.sync_api import Page, expect
from ui_automation.pages.locators import (login_field, password_field, submit_button, email_items_css)

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto("https://mail.ukr.net/")

    def login(self, username: str, password: str):
        self.page.fill(login_field, username)
        self.page.fill(password_field, password)
        self.page.click(submit_button)

        self.page.wait_for_url("https://mail.ukr.net/desktop*")

        expect(self.page.locator(email_items_css)).to_be_visible(timeout=30000)

