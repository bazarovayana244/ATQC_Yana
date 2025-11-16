from playwright.sync_api import Page, expect
from ui_automation.pages import locators
from utils.logger import Logger

class InboxPage:
    def __init__(self, page: Page):
        self.page = page
        self.log = Logger()

    def wait_for_inbox(self):
        self.log.info("Waiting for inbox to load")
        expect(self.page.locator(locators.email_items_css).first).to_be_visible(timeout=30000)

    def get_latest_two_emails(self):
        self.wait_for_inbox()
        first_subject = self.page.locator(locators.email_items_xpath).nth(0).inner_text()
        second_subject = self.page.locator(locators.email_items_xpath).nth(1).inner_text()
        self.log.info(f"Latest two emails subjects: 1) {first_subject} | 2) {second_subject}")
        return first_subject, second_subject

    def open_email_by_index(self, index=0):
        self.log.info(f"Opening email at index {index}")
        locator = self.page.locator(locators.email_items_css).nth(index)
        expect(locator).to_be_visible(timeout=15000)
        locator.click()
        expect(self.page.locator(locators.subject_xpath)).to_be_visible(timeout=15000)
        self.log.info("Email opened successfully")

    def get_email_details(self):
        from_email = self.page.locator(locators.from_email_xpath).inner_text()
        to_email = self.page.locator(locators.to_email_xpath).inner_text()
        subject = self.page.locator(locators.subject_xpath).inner_text()
        self.log.info(f"Email details - From: {from_email}, To: {to_email}, Subject: {subject}")
        return from_email, to_email, subject
