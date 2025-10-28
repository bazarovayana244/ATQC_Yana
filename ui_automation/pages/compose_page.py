from playwright.sync_api import Page, expect
from ui_automation.pages import locators

class ComposePage:
    def __init__(self, page: Page):
        self.page = page

    def open_compose(self):
        self.page.click(locators.compose_button)
        expect(self.page.locator(locators.to_field)).to_be_visible(timeout=10000)

    def send_email(self, to: str, subject: str, body: str):
        self.page.fill(locators.to_field, to)
        self.page.fill(locators.subject_field, subject)

        frame = self.page.frame_locator(locators.iframe_locator)
        frame.locator(locators.body_field).fill(body)

        self.page.click(locators.send_button)
        expect(self.page.locator(locators.popup_button_inbox)).to_be_visible(timeout=10000)
        expect(self.page.locator(locators.sent_folder)).to_be_visible(timeout=10000)

    def open_sent_folder(self):
        self.page.click(locators.sent_folder)
        expect(self.page.locator(locators.email_items_css).first).to_be_visible(timeout=10000)

    def get_last_sent_email_subject(self):
        return self.page.locator(locators.email_items_css).first.inner_text()
