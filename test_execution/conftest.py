import pytest
from playwright.sync_api import sync_playwright

def pytest_addoption(parser):
    parser.addoption(
        "--headless", action="store", default="true",
        help="Run browser in headless mode: true or false"
    )

@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def browser(pytestconfig, playwright_instance):
    headless_option = pytestconfig.getoption("--headless").lower() == "true"
    browser = playwright_instance.chromium.launch(headless=headless_option)
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    page.close()
    context.close()

