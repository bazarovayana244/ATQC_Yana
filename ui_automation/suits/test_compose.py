import datetime
import pytest
from ui_automation.pages.login_page import LoginPage
from ui_automation.pages.compose_page import ComposePage
from ui_automation.pages import locators
from playwright.sync_api import expect

@pytest.mark.usefixtures("page")
class TestComposeEmail:

    def test_send_email_and_check_sent(self, page):
        login_page = LoginPage(page)
        compose_page = ComposePage(page)

        login_page.open()
        login_page.login("test.playwright@ukr.net", "q!RamZWyGBa4Z!j")

        expect(page.locator(locators.compose_button)).to_be_visible(timeout=10000)

        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        subject_text = f"Test Email for Trainee AQA {now}"
        body_text = "Hello! This is a test email sent via Playwright POM."

        compose_page.open_compose()
        compose_page.send_email("test@example.com", subject_text, body_text)

        compose_page.open_sent_folder()

        last_subject = compose_page.get_last_sent_email_subject().strip()
        assert subject_text in last_subject, f"Expected: {subject_text}, Found: {last_subject}"
        print("Email sent and found in Sent folder")
