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

@pytest.fixture(scope="session")
def headless_option(pytestconfig):
    return pytestconfig.getoption("--headless").lower() == "true"


@pytest.fixture
def browser_page(headless_option):
    log = Logger()
    log.info(f"Launching browser from fixture, headless={headless_option}")

    browser, pw, context, page = BrowserFactory.get_browser(
        browser_name="firefox",
        headless=headless_option,
        args=["--window-size=1920,1080"]
    )

    yield page

    log.info("Closing browser from fixture")
    browser.close()
    pw.stop()
