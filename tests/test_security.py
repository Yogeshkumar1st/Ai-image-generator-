import pytest
from playwright.sync_api import sync_playwright
import os

def test_dom_xss_in_history():
    """Test that malicious data in localStorage does not trigger XSS."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        # Variable to check if alert was triggered
        alert_triggered = []

        # Listen for dialogs (like alert)
        def handle_dialog(dialog):
            alert_triggered.append(dialog.message)
            dialog.accept()

        page.on("dialog", handle_dialog)

        # Get absolute path to index.html
        file_path = f"file://{os.path.abspath('index.html')}"

        # First load to initialize localStorage
        page.goto(file_path)

        # Inject malicious payload into localStorage
        malicious_payload = '[{"url": "javascript:alert(\'XSS\')\\" onerror=\\"alert(\'XSS\')", "prompt": "malicious"}]'

        # We'll use a standard image tag payload that would trigger onerror if innerHTML is used
        malicious_payload_2 = '[{"url": "x\\" onerror=\\"alert(\'XSS\')", "prompt": "malicious"}]'

        page.evaluate(f"localStorage.setItem('xhistory', JSON.stringify([{'{'}url: 'x\" onerror=\"alert(\\'XSS\\')', prompt: 'malicious'{'}'}]))")

        # Reload the page to trigger loadHistory with the malicious payload
        page.goto(file_path)

        # Click the gallery tab to trigger loadHistory
        page.evaluate("switchTab('gallery')")

        # Wait for a brief moment to ensure any alerts would have triggered
        page.wait_for_timeout(1000)

        # Assert that no alerts were triggered
        assert len(alert_triggered) == 0, f"XSS alert was triggered: {alert_triggered}"

        # Also check that the img tag is safely rendered and not executing scripts
        img_src = page.locator(".gallery-item img").get_attribute("src")
        assert "onerror=" in img_src or img_src == 'x" onerror="alert(\'XSS\')', "Payload should be treated as literal src string"

        browser.close()
