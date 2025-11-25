import pytest
from utils.browser_factory import BrowserFactory
from utils.logger import Logger

def pytest_addoption(parser):
    parser.addoption(
        "--headless",
        action="store",
        default="false",
        help="Run browser in headless mode: true or false"
    )
    parser.addoption(
        "--ui-browser",
        action="store",
        default="firefox",
        help="Browser to use for UI tests: firefox, chrome, or webkit"
    )

@pytest.fixture(scope="session")
def headless_option(pytestconfig):
    return pytestconfig.getoption("--headless").lower() == "true"

@pytest.fixture(scope="session")
def browser_option(pytestconfig):
    return pytestconfig.getoption("--ui-browser").lower()

@pytest.fixture
def browser_page(headless_option, browser_option):
    log = Logger()
    log.info(f"Launching browser from fixture, headless={headless_option}, browser={browser_option}")

    browser, pw, context, page = BrowserFactory.get_browser(
        browser_name=browser_option,
        headless=headless_option,
        args=["--window-size=1920,1080"]
    )

    yield page

    log.info("Closing browser from fixture")
    browser.close()
    pw.stop()
