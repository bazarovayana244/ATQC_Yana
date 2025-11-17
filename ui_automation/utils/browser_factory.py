from playwright.sync_api import sync_playwright
from utils.logger import Logger

class BrowserFactory:
    @staticmethod
    def get_browser(browser_name: str = "chrome", headless: bool = True, viewport: dict = None):
        log = Logger()
        log.info(f"Starting browser: {browser_name}, headless={headless}, viewport={viewport}")

        pw = sync_playwright().start()
        browser_name = browser_name.lower()

        launch_options = {"headless": headless}
        if viewport is not None:
            launch_options["viewport"] = viewport

        if browser_name == "firefox":
            browser = pw.firefox.launch(**launch_options)
        elif browser_name == "chrome":
            browser = pw.chromium.launch(channel="chrome", **launch_options)
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")

        log.info(f"{browser_name.capitalize()} launched successfully")
        return browser, pw
