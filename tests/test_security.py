import os
import pytest
from playwright.sync_api import sync_playwright

def test_xss_vulnerability():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Get absolute path to index.html
        file_path = f"file://{os.path.abspath('index.html')}"
        page.goto(file_path)

        # Inject malicious payload into localStorage
        # The vulnerable code: div.innerHTML = `<img src="${item.url}" onclick="viewImage('${item.url}')">`;
        # So a payload like: x')"><script>alert(1)</script>
        # We need it to break out of the single quotes of viewImage('')
        # Payload: https://example.com/a')"); alert("XSS
        # If injected, innerHTML becomes: <img src="https://example.com/a')"); alert("XSS" onclick="viewImage('https://example.com/a')"); alert("XSS')">
        # Let's try an easier one that breaks the src and injects onerror
        # Payload: x" onerror="alert('XSS')
        # Wait, the stored item url goes into both src and onclick.
        # `<img src="${item.url}" onclick="viewImage('${item.url}')">`
        # Payload for URL: #')"); window.xssTriggered = true; //

        # Setup an event to catch if XSS triggered
        page.evaluate("window.xssTriggered = false;")

        # Inject payload
        xss_payload = "dummy_url'); window.xssTriggered = true; //"

        # Inject into localStorage safely without JS string interpolation breaking
        page.evaluate("""
            ([url]) => {
                let history = [{ url: url, prompt: "malicious prompt" }];
                localStorage.setItem('xhistory', JSON.stringify(history));
            }
        """, [xss_payload])

        # Trigger loadHistory by switching tab
        page.evaluate("switchTab('gallery')")

        # Click the image to trigger the XSS
        # Since the HTML might be malformed, let's just wait and see if it triggered
        page.locator('.gallery-item img').click()

        # Check if XSS triggered
        xss_triggered = page.evaluate("window.xssTriggered")

        assert not xss_triggered, "XSS vulnerability detected!"

        browser.close()

def test_gallery_functionality():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Get absolute path to index.html
        file_path = f"file://{os.path.abspath('index.html')}"
        page.goto(file_path)

        # Inject normal payload into localStorage
        normal_url = "https://image.pollinations.ai/prompt/cat"
        page.evaluate(f"""
            let history = [{{ url: "{normal_url}", prompt: "cat" }}];
            localStorage.setItem('xhistory', JSON.stringify(history));
        """)

        # Trigger loadHistory by switching tab
        page.evaluate("switchTab('gallery')")

        # Verify image is displayed
        assert page.locator('.gallery-item img').count() == 1

        # Click the image
        page.locator('.gallery-item img').click()

        # Verify it switches to creator tab and shows the image
        assert page.locator('.tabs .tab:nth-child(1)').get_attribute('class') == 'tab active'

        # Verify the result image src
        assert page.locator('#resultImage').get_attribute('src') == normal_url

        browser.close()
