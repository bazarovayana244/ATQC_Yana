import datetime
from ui_automation.pages.login_page import LoginPage
from ui_automation.pages.compose_page import ComposePage
from ui_automation.pages import locators
from utils.browser_factory import BrowserFactory
from utils.logger import Logger
from playwright.sync_api import expect

class TestComposeEmail:

    def test_send_email_and_check_sent(self):
        log = Logger()
        log.info("Starting test_send_email_and_check_sent")

        browser, pw, context, page = BrowserFactory.get_browser(
            browser_name="chrome",
            headless=False,
            args=["--window-size=1920,1080", "--disable-gpu"]
        )

        login_page = LoginPage(page)
        compose_page = ComposePage(page)

        login_page.open()
        login_page.login("test.playwright@ukr.net", "q!RamZWyGBa4Z!j")
        log.info("Login successful")

        expect(page.locator(locators.compose_button)).to_be_visible(timeout=10000)

        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        subject_text = f"Test Email for Trainee AQA {now}"
        body_text = "Hello! This is a test email sent via Playwright POM."
        log.info(f"Sending email with subject: {subject_text}")

        compose_page.open_compose()
        compose_page.send_email("test@example.com", subject_text, body_text)

        compose_page.open_sent_folder()
        last_subject = compose_page.get_last_sent_email_subject().strip()
        assert subject_text in last_subject, f"Expected: {subject_text}, Found: {last_subject}"
        log.info(f"Email sent successfully and found in Sent folder: {last_subject}")

        log.info("Closing browser")
        browser.close()
        pw.stop()

