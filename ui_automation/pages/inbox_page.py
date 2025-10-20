from playwright.sync_api import Page, expect
from ui_automation.pages.locators import (email_items_css, email_items_xpath, from_email_xpath, to_email_xpath, subject_xpath)

class InboxPage:
    def __init__(self, page: Page):
        self.page = page

    def wait_for_inbox(self):
        expect(self.page.locator(email_items_css).first).to_be_visible(timeout=30000)

    def get_latest_two_emails_css(self):
        self.wait_for_inbox()
        subjects = self.page.locator(email_items_css).all_text_contents()
        return subjects[:2]

    def get_latest_two_emails_xpath(self):
        self.wait_for_inbox()
        subjects = self.page.locator(email_items_xpath).all_text_contents()
        return subjects[:2]

    def open_email_by_index(self, index=0):
        locator = self.page.locator(email_items_css).nth(index)
        expect(locator).to_be_visible(timeout=15000)
        locator.click()
        expect(self.page.locator(subject_xpath)).to_be_visible(timeout=15000)

    def get_email_details(self):
        from_email = self.page.locator(from_email_xpath).inner_text()
        to_email = self.page.locator(to_email_xpath).inner_text()
        subject = self.page.locator(subject_xpath).inner_text()
        return from_email, to_email, subject
