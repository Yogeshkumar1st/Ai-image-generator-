from playwright.sync_api import sync_playwright
import os
import sys

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the page
        page.goto(f"file://{os.path.abspath('index.html')}")

        # Inject malicious payload into localStorage
        payload = {
            "url": "\"><img src=x onerror=window.xssDetected=true>",
            "prompt": "Malicious Prompt"
        }

        page.evaluate(f"""
            localStorage.setItem('xhistory', JSON.stringify([{payload}]));
        """)

        # Click the "Gallery" tab to trigger loadHistory
        page.click("text=Gallery")

        # Check if window.xssDetected is true
        is_xss = page.evaluate("window.xssDetected === true")

        if is_xss:
            print("VULNERABILITY DETECTED: XSS payload executed!")
            sys.exit(1)
        else:
            print("SUCCESS: XSS payload did NOT execute.")
            sys.exit(0)

        browser.close()

if __name__ == "__main__":
    run()
