import pytest
from utils.browser_factory import BrowserFactory
from utils.logger import Logger
from utils.testrail_client import TestRailClient

@pytest.fixture(scope="session")
def headless_option(pytestconfig):
    return pytestconfig.getoption("--headless", default="false").lower() == "true"

@pytest.fixture(scope="session")
def testrail():
    base_url = "https://atqcyana.testrail.io/"
    username = "bazarovayana244@gmail.com"
    api_key = "4Dl.awvJDWSezZZsoU8h-lQSBFPhm0a0uDw2BPU7t"
    run_id = 13
    case_ids = {
        "test_successful_login": 44,
        "test_email_details_non_empty": 43,
        "test_latest_two_emails_exist": 42,
        "test_send_email_and_check_sent": 41
    }
    client = TestRailClient(base_url, username, api_key, run_id, case_ids)
    return client

@pytest.fixture
def browser_page(headless_option):
    log = Logger()
    log.info(f"Launching browser, headless={headless_option}")

    browser, pw, context, page = BrowserFactory.get_browser(
        browser_name="chrome",
        headless=headless_option,
        args=["--window-size=1920,1080"]
    )

    yield page

    log.info("Closing browser")
    browser.close()
    pw.stop()
