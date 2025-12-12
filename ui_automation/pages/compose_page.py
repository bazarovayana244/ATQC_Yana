from playwright.sync_api import Page, expect
from ui_automation.pages import locators
from utils.logger import Logger

class ComposePage:
    def __init__(self, page: Page):
        self.page = page
        self.log = Logger()

    def open_compose(self):
        self.log.info("Clicking compose button")
        self.page.click(locators.compose_button)
        expect(self.page.locator(locators.to_field)).to_be_visible(timeout=10000)
        self.log.info("Compose form opened successfully")

    def send_email(self, to: str, subject: str, body: str):
        self.log.info(f"Filling email fields - To: {to}, Subject: {subject}")
        self.page.fill(locators.to_field, to)
        self.page.fill(locators.subject_field, subject)

        frame = self.page.frame_locator(locators.iframe_locator)
        self.log.info("Filling email body in iframe")
        frame.locator(locators.body_field).fill(body)

        self.log.info("Clicking send button")
        self.page.click(locators.send_button)
        expect(self.page.locator(locators.popup_button_inbox)).to_be_visible(timeout=10000)
        expect(self.page.locator(locators.sent_folder)).to_be_visible(timeout=10000)
        self.log.info("Email sent successfully")

    def open_sent_folder(self):
        self.log.info("Opening Sent folder")
        self.page.click(locators.sent_folder)
        expect(self.page.locator(locators.email_items_css).first).to_be_visible(timeout=10000)
        self.log.info("Sent folder loaded successfully")

    def get_last_sent_email_subject(self):
        subject = self.page.locator(locators.email_items_css).first.inner_text()
        self.log.info(f"Last sent email subject: {subject}")
        return subject
