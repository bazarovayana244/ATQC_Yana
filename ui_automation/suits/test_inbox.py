from ui_automation.pages.login_page import LoginPage
from ui_automation.pages.inbox_page import InboxPage
from ui_automation.pages import locators
from utils.logger import Logger
from playwright.sync_api import expect

class TestInboxPage:

    def test_latest_two_emails_exist(self, browser_page, testrail):
        test_name = "test_latest_two_emails_exist"
        log = Logger()
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

            testrail.add_result_for_case(test_name, 1, "Test passed")
            log.info("Result sent to TestRail")

        except Exception as e:
            testrail.add_result_for_case(test_name, 5, f"Failed: {e}")
            log.error(f"[TestRail ERROR] Cannot send result: {e}")
            raise

    def test_email_details_non_empty(self, browser_page, testrail):
        test_name = "test_email_details_non_empty"
        log = Logger()
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

            testrail.add_result_for_case(test_name, 1, "Test passed")
            log.info("Result sent to TestRail")

        except Exception as e:
            testrail.add_result_for_case(test_name, 5, f"Failed: {e}")
            log.error(f"[TestRail ERROR] Cannot send result: {e}")
            raise
