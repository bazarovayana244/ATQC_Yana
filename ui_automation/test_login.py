###Automate the following scenario: 1. Login to email box  2. Get the latest 2 emails from the mail list using different kinds of locators (xpath, css)###
from playwright.sync_api import sync_playwright
import time

def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://mail.ukr.net/")

        page.fill("input[name='login']", "test.playwright@ukr.net")
        page.fill("input[name='password']", "q!RamZWyGBa4Z!j")
        page.click("button[type='submit']")

        page.wait_for_url("https://mail.ukr.net/desktop/u0/msglist/inbox")

        browser.close()

def test_latest_two_emails():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://mail.ukr.net/")

        page.fill("input[name='login']", "test.playwright@ukr.net")
        page.fill("input[name='password']", "q!RamZWyGBa4Z!j")
        page.click("button[type='submit']")

        time.sleep(7)

        css_locators = page.locator("[data-msglist-main-link]").all_text_contents()
        xpath_locators = page.locator("//*[@data-msglist-main-link]").all_text_contents()

        print("1.", css_locators[0])
        print("2.", css_locators[1])

        print("1.", xpath_locators[0])
        print("2.", xpath_locators[1])

        browser.close()
