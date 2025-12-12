import re
from playwright.sync_api import expect
from ui_automation.pages.login_page import LoginPage
from ui_automation.pages import locators
from utils.logger import Logger

class TestLogin:

    def test_successful_login(self, browser_page, testrail):
        test_name = "test_successful_login"
        log = Logger()
        log.info("Start test_successful_login")

        page = browser_page
        login_page = LoginPage(page)

        try:
            login_page.open()
            login_page.login("atqc_@ukr.net", "L!_Zu5@dVyXPEFL")

            expect(page).to_have_url(re.compile(r"https://mail\.ukr\.net/desktop/.*"))
            expect(page.locator(locators.compose_button)).to_be_visible(timeout=10000)

            testrail.add_result_for_case(test_name, 1, "Test passed")
            log.info("Result sent to TestRail")

        except Exception as e:
            testrail.add_result_for_case(test_name, 5, f"Failed: {e}")
            log.error(f"[TestRail ERROR] Cannot send result: {e}")
            raise
