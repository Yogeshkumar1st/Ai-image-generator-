import pytest
import json
import os
from playwright.sync_api import sync_playwright

def test_xss_prevention():
    """
    Tests that malicious content in localStorage does not execute arbitrary JavaScript.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the page
        page.goto(f"file://{os.getcwd()}/index.html")

        # malicious payload
        # " onerror="window.xss_triggered=true"
        # This tries to break out of the src attribute and add an onerror handler
        payload = [
            {
                "url": 'x" onerror="window.xss_triggered=true',
                "prompt": "XSS Attempt"
            }
        ]

        # Set localStorage
        page.evaluate(f"localStorage.setItem('xhistory', JSON.stringify({json.dumps(payload)}))")

        # Switch to Gallery tab to trigger loadHistory()
        page.click("text=Gallery")

        # Wait for potential execution
        page.wait_for_timeout(1000)

        # Check if the variable was set
        xss_triggered = page.evaluate("window.xss_triggered === true")

        browser.close()

        # If xss_triggered is True, the vulnerability exists.
        # The test should pass only if xss_triggered is False.
        assert not xss_triggered, "XSS Payload executed! Vulnerability found."
