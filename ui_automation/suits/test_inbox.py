import pytest
from ui_automation.pages.login_page import LoginPage
from ui_automation.pages.inbox_page import InboxPage
from ui_automation.pages import locators
from playwright.sync_api import expect

@pytest.mark.usefixtures("page")
class TestInboxPage:

    def test_latest_two_emails_exist(self, page):
        login_page = LoginPage(page)
        inbox_page = InboxPage(page)

        login_page.open()
        login_page.login("test.playwright@ukr.net", "q!RamZWyGBa4Z!j")

        expect(page.locator(locators.compose_button)).to_be_visible(timeout=10000)

        emails = inbox_page.get_latest_two_emails()
        assert len(emails) == 2, f"Expected 2 emails, found {len(emails)}"

    def test_email_details_non_empty(self, page):
        login_page = LoginPage(page)
        inbox_page = InboxPage(page)

        login_page.open()
        login_page.login("test.playwright@ukr.net", "q!RamZWyGBa4Z!j")

        expect(page.locator(locators.compose_button)).to_be_visible(timeout=10000)

        inbox_page.open_email_by_index(0)
        from_email, to_email, subject = inbox_page.get_email_details()

        assert from_email != "", "From field is empty"
        assert to_email != "", "To field is empty"

        assert page.locator(locators.subject_xpath).is_visible()(timeout=15000), "Subject element is not visible"

        print("Email details are visible")
