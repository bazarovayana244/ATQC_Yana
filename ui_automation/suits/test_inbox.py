from ui_automation.pages.login_page import LoginPage
from ui_automation.pages.inbox_page import InboxPage
from ui_automation.pages import locators
from utils.logger import Logger
from playwright.sync_api import expect

class TestInboxPage:

    def test_latest_two_emails_exist(self, browser_page):
        log = Logger()
        log.info("Start test_latest_two_emails_exist")

        page = browser_page
        login_page = LoginPage(page)
        inbox_page = InboxPage(page)

        login_page.open()
        login_page.login("test.playwright@ukr.net", "q!RamZWyGBa4Z!j")

        expect(page.locator(locators.compose_button)).to_be_visible()

        emails = inbox_page.get_latest_two_emails()
        assert len(emails) == 2

        log.info(f"Latest emails: {emails}")


    def test_email_details_non_empty(self, browser_page):
        log = Logger()
        log.info("Start test_email_details_non_empty")

        page = browser_page
        login_page = LoginPage(page)
        inbox_page = InboxPage(page)

        login_page.open()
        login_page.login("test.playwright@ukr.net", "q!RamZWyGBa4Z!j")

        expect(page.locator(locators.compose_button)).to_be_visible()

        inbox_page.open_email_by_index(0)
        from_email, to_email, subject = inbox_page.get_email_details()

        assert from_email
        assert to_email
        assert page.locator(locators.subject_xpath).is_visible()

        log.info(f"Email details OK: {from_email}, {to_email}, {subject}")
