from playwright.sync_api import Page, expect
from ui_automation.pages import locators

class InboxPage:
    def __init__(self, page: Page):
        self.page = page

    def wait_for_inbox(self):
        expect(self.page.locator(locators.email_items_css).first).to_be_visible(timeout=30000)

    def get_latest_two_emails(self):
        self.wait_for_inbox()
        first_subject = self.page.locator(locators.email_items_xpath).nth(0).inner_text()
        second_subject = self.page.locator(locators.email_items_xpath).nth(1).inner_text()
        return first_subject, second_subject

    def open_email_by_index(self, index=0):
        locator = self.page.locator(locators.email_items_css).nth(index)
        expect(locator).to_be_visible(timeout=15000)
        locator.click()
        expect(self.page.locator(locators.subject_xpath)).to_be_visible(timeout=15000)

    def get_email_details(self):
        from_email = self.page.locator(locators.from_email_xpath).inner_text()
        to_email = self.page.locator(locators.to_email_xpath).inner_text()
        subject = self.page.locator(locators.subject_xpath).inner_text()
        return from_email, to_email, subject
