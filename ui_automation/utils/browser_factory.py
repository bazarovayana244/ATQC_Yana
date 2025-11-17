from playwright.sync_api import sync_playwright
from utils.logger import Logger

class BrowserFactory:

    @staticmethod
    def get_browser(browser_name: str = "chrome", headless: bool = True, args: list = None):
        log = Logger()
        log.info(f"Starting browser: {browser_name}, headless={headless}, args={args}")

        pw = sync_playwright().start()
        browser_name = browser_name.lower()

        launch_options = {"headless": headless}
        if args:
            launch_options["args"] = args

        if browser_name == "firefox":
            browser = pw.firefox.launch(**launch_options)
        elif browser_name == "chrome":
            browser = pw.chromium.launch(channel="chrome", **launch_options)
        else:
            log.error(f"Unsupported browser: {browser_name}")
            pw.stop()
            raise ValueError(f"Unsupported browser: {browser_name}")

        context = browser.new_context()
        page = context.new_page()

        return browser, pw, context, page
