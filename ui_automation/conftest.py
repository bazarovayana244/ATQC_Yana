import pytest

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

