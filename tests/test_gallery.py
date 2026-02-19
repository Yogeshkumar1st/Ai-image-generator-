import pytest
import os
from playwright.sync_api import sync_playwright

def test_gallery_loading_and_xss():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Load the local HTML file
        page.goto(f"file://{os.path.abspath('index.html')}")

        # Define a mock XSS payload
        # This payload tries to close the img tag and execute a script
        # The original code: <img src="${item.url}" onclick="viewImage('${item.url}')">
        # If url is: "><img src=x onerror=window.xss=true><"
        # Result: <img src=""><img src=x onerror=window.xss=true><" ...>
        # Or simpler: x" onerror="window.xss=true
        # Result: <img src="x" onerror="window.xss=true" ...>

        xss_payload = 'x" onerror="window.xss=true'

        # Mock local storage with a normal item and the malicious item
        page.evaluate(f"""
            localStorage.setItem('xhistory', JSON.stringify([
                {{url: 'https://via.placeholder.com/150', prompt: 'normal prompt'}},
                {{url: '{xss_payload}', prompt: 'malicious prompt'}}
            ]));
        """)

        # Set a flag to detect XSS execution
        page.evaluate("window.xss = false;")

        # Reload/Switch to gallery to trigger loadHistory
        page.evaluate("switchTab('gallery')")

        # Check if the normal image is in the DOM
        # The malicious one might break the DOM or just be another image depending on injection

        # Verify normal image presence
        # We look for the one with the correct src
        normal_img = page.locator('img[src="https://via.placeholder.com/150"]')
        assert normal_img.count() == 1

        # Click the image to ensure event listener works
        normal_img.click()

        # Verify we are back in creator tab and image is loaded
        assert page.locator('#creatorTab').is_visible()
        assert page.locator('#resultImage').is_visible()
        assert page.get_attribute('#resultImage', 'src') == "https://via.placeholder.com/150"

        # Check for XSS execution
        is_xss_executed = page.evaluate("window.xss")

        # In the vulnerable version, we expect XSS to execute (is_xss_executed should be True)
        # But we want the test to pass eventually.
        # So we can assert based on expected behavior for the "fixed" version?
        # Or better: Print the status.

        print(f"XSS Executed: {is_xss_executed}")

        # For the final verification (after fix), we want is_xss_executed to be False.
        # But for the "reproduction", we expect True.
        # To make this test useful for regression, let's assert it is False.
        # This means the test will FAIL now, and PASS after fix.

        assert is_xss_executed is False, "XSS Payload executed! Vulnerability confirmed."

        browser.close()
