from ui_automation.pages.login_page import LoginPage
from ui_automation.pages.inbox_page import InboxPage
from ui_automation.pages import locators
from utils.logger import Logger
from playwright.sync_api import expect

class TestInboxPage:

    def test_latest_two_emails_exist(self, browser_page, testrail):
        log = Logger()
        test_name = "test_latest_two_emails_exist"
        log.info(f"Start {test_name}")

        page = browser_page
        login_page = LoginPage(page)
        inbox_page = InboxPage(page)

        try:
            login_page.open()
            login_page.login("atqc_@ukr.net", "L!_Zu5@dVyXPEFL")

            expect(page.locator(locators.compose_button)).to_be_visible()

            emails = inbox_page.get_latest_two_emails()
            assert len(emails) == 2

            log.info(f"Latest emails: {emails}")
            testrail.add_result_for_case(test_name, status_id=1, comment="Test passed (automated)")

        except AssertionError as ae:
            testrail.add_result_for_case(test_name, status_id=5, comment=f"Assertion failed: {ae}")
            raise
        except Exception as e:
            testrail.add_result_for_case(test_name, status_id=5, comment=f"Error: {e}")
            raise

    def test_email_details_non_empty(self, browser_page, testrail):
        log = Logger()
        test_name = "test_email_details_non_empty"
        log.info(f"Start {test_name}")

        page = browser_page
        login_page = LoginPage(page)
        inbox_page = InboxPage(page)

        try:
            login_page.open()
            login_page.login("atqc_@ukr.net", "L!_Zu5@dVyXPEFL")

            expect(page.locator(locators.compose_button)).to_be_visible()

            inbox_page.open_email_by_index(0)
            from_email, to_email, subject = inbox_page.get_email_details()

            assert from_email
            assert to_email
            assert page.locator(locators.subject_xpath).is_visible()

            log.info(f"Email details OK: {from_email}, {to_email}, {subject}")
            testrail.add_result_for_case(test_name, status_id=1, comment="Test passed (automated)")

        except AssertionError as ae:
            testrail.add_result_for_case(test_name, status_id=5, comment=f"Assertion failed: {ae}")
            raise
        except Exception as e:
            testrail.add_result_for_case(test_name, status_id=5, comment=f"Error: {e}")
            raise

