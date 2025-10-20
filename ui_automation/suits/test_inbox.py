from ui_automation.pages.login_page import LoginPage
from ui_automation.pages.inbox_page import InboxPage

def test_latest_two_emails(page):
    login_page = LoginPage(page)
    inbox_page = InboxPage(page)

    login_page.open()
    login_page.login("test.playwright@ukr.net", "q!RamZWyGBa4Z!j")

    latest_css = inbox_page.get_latest_two_emails_css()
    print("Latest two emails (CSS):", latest_css)

    latest_xpath = inbox_page.get_latest_two_emails_xpath()
    print("Latest two emails (XPath):", latest_xpath)

def test_email_details(page):
    login_page = LoginPage(page)
    inbox_page = InboxPage(page)

    login_page.open()
    login_page.login("test.playwright@ukr.net", "q!RamZWyGBa4Z!j")

    inbox_page.open_email_by_index(0)
    from_email, to_email, subject = inbox_page.get_email_details()

    print("From:", from_email)
    print("To:", to_email)
    print("Subject:", subject)
