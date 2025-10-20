import datetime
from playwright.sync_api import Page, expect
from ui_automation.pages.locators import (compose_button, to_field, subject_field, iframe_locator, body_field, send_button, sent_folder, email_items_css)

class ComposePage:
    def __init__(self, page: Page):
        self.page = page

    def open_compose(self):
        self.page.click(compose_button)
        expect(self.page.locator(to_field)).to_be_visible(timeout=10000)

    def send_email(self, to: str, subject: str, body: str):
        self.page.fill(to_field, to)
        self.page.fill(subject_field, subject)

        frame = self.page.frame_locator(iframe_locator)
        frame.locator(body_field).fill(body)

        self.page.click(send_button)

        expect(self.page.locator(sent_folder)).to_be_visible(timeout=10000)

    def open_sent_folder(self):
        self.page.click(sent_folder)
        expect(self.page.locator(email_items_css).first).to_be_visible(timeout=10000)

    def get_last_sent_email_subject(self):
        return self.page.locator(email_items_css).first.inner_text()
