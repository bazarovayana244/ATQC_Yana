import pytest
from utils.logger import Logger

# Removed custom fixtures and used default from pytest-playwright
# example: pytest ui_automation/suits/ --headed --browser=firefox

@pytest.fixture
def browser_page(page):
    log = Logger()
    log.info("Launching browser from Playwright fixture")
    yield page
    log.info("Closing browser from Playwright fixture")
