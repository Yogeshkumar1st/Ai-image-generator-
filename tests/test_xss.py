import json
import os
from playwright.sync_api import sync_playwright

def test_xss_in_history_load():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Prepare malicious history item
        malicious_url = "https://example.com/image.jpg?q=');window.xss_triggered=true;//"
        history_data = [{"url": malicious_url, "prompt": "malicious prompt"}]
        history_json = json.dumps(history_data)

        # Load page
        cwd = os.getcwd()
        file_path = f"file://{cwd}/index.html"
        page.goto(file_path)

        # Inject malicious history into localStorage
        # Use json.dumps again for the outer string to be valid JS string literal
        page.evaluate(f"localStorage.setItem('xhistory', {json.dumps(history_json)});")

        # Switch to Gallery tab to trigger loadHistory
        page.click("text=Gallery")

        # Wait for gallery item
        page.wait_for_selector(".gallery-item img")

        # Click the image
        page.click(".gallery-item img")

        # Check if window.xss_triggered is true
        is_xss_triggered = page.evaluate("window.xss_triggered === true")

        browser.close()

        # Assert that XSS was NOT triggered
        assert not is_xss_triggered, "XSS vulnerability detected! malicious JS executed."
        print("Test passed: XSS vulnerability not detected.")

if __name__ == "__main__":
    test_xss_in_history_load()
