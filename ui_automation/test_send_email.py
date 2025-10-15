#Add one more suite with test: send email to test@example.com and check if email is sent (it appears into "sent" folder)###

from playwright.sync_api import sync_playwright
import time

class UkrNetMail:
    def __init__(self, page):
        self.page = page
        self.login_field = "input[name='login']"
        self.password_field = "input[name='password']"
        self.submit_button = "button[type='submit']"
        self.compose_button = "button:has-text('Написати листа')"
        self.to_field = "#compose-to"
        self.subject_field = "#compose-subject"
        self.iframe_locator = "iframe[id^='mce_']"
        self.body_field = "body#tinymce"
        self.send_button = "button:has-text('Надіслати')"
        self.sent_folder = "span:has-text('Надіслані')"
        self.email_items_css = "[data-msglist-main-link]"

    def open(self):
        self.page.goto("https://mail.ukr.net/")

    def login(self, username, password):
        self.page.fill(self.login_field, username)
        self.page.fill(self.password_field, password)
        self.page.click(self.submit_button)
        time.sleep(7)

    def send_email(self, to, subject, body_text):
        self.page.click(self.compose_button)
        time.sleep(2)
        self.page.fill(self.to_field, to)
        self.page.fill(self.subject_field, subject)

        frame = self.page.frame_locator(self.iframe_locator)
        frame.locator(self.body_field).fill(body_text)

        self.page.click(self.send_button)
        time.sleep(5)

    def open_sent_folder(self):
        self.page.click(self.sent_folder)
        time.sleep(5)

    def get_last_sent_email_subject(self):
        return self.page.locator(self.email_items_css).nth(0).inner_text()

def test_send_email_and_check_sent():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        mail_page = UkrNetMail(page)

        mail_page.open()
        mail_page.login("test.playwright@ukr.net", "q!RamZWyGBa4Z!j")

        subject_text = "Test Email for Trainee AQA"
        body_text = "Hello! This is a test email sent via Playwright POM."

        mail_page.send_email("test@example.com", subject_text, body_text)

        mail_page.open_sent_folder()
        last_subject = mail_page.get_last_sent_email_subject().strip()
        expected_subject = subject_text.strip()
        if expected_subject in last_subject:
            print("Success")
        else:
            print("Fail", repr(last_subject))

        browser.close()
