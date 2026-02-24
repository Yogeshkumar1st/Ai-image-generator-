import os
import json
import sys
from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        file_path = os.path.abspath("index.html")
        page.goto(f"file://{file_path}")

        # Payload designed to break out of src attribute
        payload_url = 'x" onerror="window.xss_triggered=true'
        malicious_payload = [{"url": payload_url, "prompt": "XSS Test"}]

        # Serialize to JSON string for localStorage
        json_str = json.dumps(malicious_payload)

        # Set localStorage
        page.evaluate("(data) => localStorage.setItem('xhistory', data)", json_str)

        # Switch tab to trigger loadHistory
        page.click("text=Gallery")

        # Wait a bit
        page.wait_for_timeout(1000)

        # Check trigger
        is_triggered = page.evaluate("window.xss_triggered || false")

        browser.close()

        if is_triggered:
            print("FAIL: XSS vulnerability detected!")
            sys.exit(1)
        else:
            print("PASS: No XSS detected.")
            sys.exit(0)

if __name__ == "__main__":
    run()
