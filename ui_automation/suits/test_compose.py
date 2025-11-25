import datetime
from ui_automation.pages.login_page import LoginPage
from ui_automation.pages.compose_page import ComposePage
from ui_automation.pages import locators
from utils.logger import Logger
from playwright.sync_api import expect

class TestComposeEmail:

    def test_send_email_and_check_sent(self, browser_page):
        log = Logger()
        log.info("Start test_send_email_and_check_sent")

        page = browser_page
        login_page = LoginPage(page)
        compose_page = ComposePage(page)

        login_page.open()
        login_page.login("test.playwright@ukr.net", "q!RamZWyGBa4Z!j")

        expect(page.locator(locators.compose_button)).to_be_visible()

        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        subject_text = f"Test Email {now}"

        compose_page.open_compose()
        compose_page.send_email("test@example.com", subject_text, "Hello world")

        compose_page.open_sent_folder()
        last_subject = compose_page.get_last_sent_email_subject().strip()

        assert subject_text in last_subject
        log.info("Email found in Sent folder")
