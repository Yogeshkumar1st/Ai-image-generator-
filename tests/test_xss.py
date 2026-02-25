import os
from playwright.sync_api import sync_playwright

def test_xss_protection():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        filepath = os.path.abspath("index.html")
        page.goto(f"file://{filepath}")

        # Inject malicious payload
        # We use a payload that attempts to break out of the src attribute
        malicious_payload = 'x" onerror="window.xss=true'

        page.evaluate(f'''() => {{
            const history = [{{ url: '{malicious_payload}', prompt: 'test' }}];
            localStorage.setItem('xhistory', JSON.stringify(history));
        }}''')

        # Click Gallery tab to trigger loadHistory
        page.click("text=Gallery")

        # 1. Check that the image element exists
        img = page.query_selector('.gallery-item img')
        if not img:
            print("FAILURE: Image element not created")
            exit(1)

        # 2. Check for XSS execution (window.xss)
        xss_triggered = page.evaluate("() => window.xss === true")
        if xss_triggered:
            print("FAILURE: XSS execution detected via window.xss")
            exit(1)

        # 3. Check for onerror attribute presence
        # Get the outer HTML or check attributes specifically
        # Note: In a fixed version, the src attribute will contain the payload,
        # but it won't be parsed as a separate onerror attribute.

        # We can check if the element has the 'onerror' attribute
        has_onerror = page.evaluate("document.querySelector('.gallery-item img').hasAttribute('onerror')")

        if has_onerror:
            print("FAILURE: onerror attribute found on image element")
            exit(1)

        # 4. Verify src contains the payload (proving it was treated as value)
        src_value = page.evaluate("document.querySelector('.gallery-item img').getAttribute('src')")
        if malicious_payload not in src_value:
             print(f"WARNING: src value '{src_value}' does not contain payload '{malicious_payload}'")
             # This might happen due to URL encoding, but let's see.

        print("SUCCESS: XSS Payload neutralized. Image created without executing script.")

        browser.close()

if __name__ == "__main__":
    test_xss_protection()
