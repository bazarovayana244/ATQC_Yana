###Implement the same task using Page Object approach and any of Python framework (Unittest, Pytest, etc)
#Add one more test to the suite: to check the details of the specific email: from, to and subject fields
#Add one more suite with test: send email to test@example.com and check if email is sent (it appears into "sent" folder)###

from playwright.sync_api import sync_playwright
import time

class UkrNetMailPage:
    def __init__(self, page):
        self.page = page
        self.login_field = "input[name='login']"
        self.password_field = "input[name='password']"
        self.submit_button = "button[type='submit']"
        self.email_items_css = "[data-msglist-main-link]"
        self.email_items_xpath = "//*[@data-msglist-main-link]"

    def open(self):
        self.page.goto("https://mail.ukr.net/")

    def login(self, username, password):
        self.page.fill(self.login_field, username)
        self.page.fill(self.password_field, password)
        self.page.click(self.submit_button)
        time.sleep(6)

    def get_latest_two_emails_css(self):
        subjects = self.page.locator(self.email_items_css).all_text_contents()
        return subjects[:2]

    def get_latest_two_emails_xpath(self):
        subjects = self.page.locator(self.email_items_xpath).all_text_contents()
        return subjects[:2]

    def open_email_by_index(self, index=0):
        self.page.locator(self.email_items_css).nth(index).click()
        time.sleep(4)

    def get_email_details(self):
        from_emails = self.page.locator('span[aria-label="Відправник"] span._0DwAbJNo').nth(0).inner_text()

        to_emails = self.page.locator('span[aria-label="Відправник"] span._0DwAbJNo').nth(1).inner_text()

        subject = self.page.locator('h1').inner_text()

        return from_emails, to_emails, subject

def test_get_latest_two_emails():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        mail_page = UkrNetMailPage(page)

        mail_page.open()
        mail_page.login("test.playwright@ukr.net", "q!RamZWyGBa4Z!j")

        css_emails = mail_page.get_latest_two_emails_css()
        print("1.", css_emails[0])
        print("2.", css_emails[1])

        xpath_emails = mail_page.get_latest_two_emails_xpath()
        print("1.", xpath_emails[0])
        print("2.", xpath_emails[1])

        browser.close()


def test_email_details():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        mail_page = UkrNetMailPage(page)

        mail_page.open()
        mail_page.login("test.playwright@ukr.net", "q!RamZWyGBa4Z!j")

        mail_page.open_email_by_index(0)

        from_email, to_email, subject = mail_page.get_email_details()

        print("From:", from_email)
        print("To:", to_email)
        print("Subject:", subject)

        browser.close()
