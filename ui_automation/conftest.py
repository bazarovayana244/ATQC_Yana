import pytest
from utils.browser_factory import BrowserFactory
from utils.logger import Logger
from utils.testrail_client import TestRailClient

@pytest.fixture(scope="session")
def headless_option(pytestconfig):
    return pytestconfig.getoption("--headless", default="true").lower() == "true"

@pytest.fixture(scope="session")
def testrail():
    base_url = "https://atqcyana.testrail.io"
    username = "bazarovayana244@gmail.com"
    api_key = "xF5v9aEMlHBkppDdS2Ca-GYHc09Ovwp5RurDAAuBO"
    run_id = 13

    client = TestRailClient(base_url, username, api_key, run_id)
    client.fetch_run_tests()

    return client

@pytest.fixture
def browser_page(headless_option):
    log = Logger()
    log.info(f"Launching browser, headless={headless_option}")

    browser, pw, context, page = BrowserFactory.get_browser(
        browser_name="firefox",
        headless=headless_option,
        args=["--window-size=1920,1080"]
    )

    yield page

    log.info("Closing browser")
    browser.close()
    pw.stop()
