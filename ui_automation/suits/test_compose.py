import datetime
from ui_automation.pages.login_page import LoginPage
from ui_automation.pages.compose_page import ComposePage
from ui_automation.pages import locators
from utils.logger import Logger
from playwright.sync_api import expect

class TestComposeEmail:

    def test_send_email_and_check_sent(self, browser_page, testrail):
        log = Logger()
        test_name = "test_send_email_and_check_sent"
        log.info(f"Start {test_name}")

        page = browser_page
        login_page = LoginPage(page)
        compose_page = ComposePage(page)

        try:
            login_page.open()
            login_page.login("atqc_@ukr.net", "L!_Zu5@dVyXPEFL")

            expect(page.locator(locators.compose_button)).to_be_visible()

            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            subject_text = f"Test Email {now}"

            compose_page.open_compose()
            compose_page.send_email("test@example.com", subject_text, "Hello world")

            compose_page.open_sent_folder()
            last_subject = compose_page.get_last_sent_email_subject().strip()

            assert subject_text in last_subject
            log.info("Email found in Sent folder")

            testrail.add_result_for_case(test_name, status_id=1, comment="Test passed (automated)")

        except AssertionError as ae:
            testrail.add_result_for_case(test_name, status_id=5, comment=f"Assertion failed: {ae}")
            raise
        except Exception as e:
            testrail.add_result_for_case(test_name, status_id=5, comment=f"Error: {e}")
            raise
