from ui_automation.pages.login_page import LoginPage

def test_login(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("test.playwright@ukr.net", "q!RamZWyGBa4Z!j")

    print("Login successful")
