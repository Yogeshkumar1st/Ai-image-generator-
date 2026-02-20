import pytest
from playwright.sync_api import sync_playwright
import os

def test_xss_vulnerability():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        filepath = os.path.abspath("index.html")
        page.goto(f"file://{filepath}")

        # Malicious payload designed to break out of single quotes in onclick
        # logic: viewImage('https://example.com/foo');alert('XSS');//')
        malicious_url = "https://example.com/foo');alert('XSS');//"

        # Inject into localStorage
        page.evaluate(f"""() => {{
            localStorage.setItem('xhistory', JSON.stringify([
                {{ url: "{malicious_url}", prompt: "malicious prompt" }}
            ]));
        }}""")

        # Capture dialogs
        dialog_messages = []
        def handle_dialog(dialog):
            print(f"Dialog triggered: {dialog.message}")
            dialog_messages.append(dialog.message)
            dialog.dismiss()

        page.on("dialog", handle_dialog)

        # Go to Gallery tab
        page.click("text=Gallery")

        # Click the image
        try:
            page.click(".gallery-item img", timeout=2000)
        except Exception:
            page.click(".gallery-item img", force=True)

        # Wait a moment for potential JS execution
        page.wait_for_timeout(1000)

        # Check for XSS
        if dialog_messages:
            pytest.fail(f"SECURITY FAILURE: XSS Vulnerability detected! Alert(s) triggered: {dialog_messages}")

        # Check functionality: Main image src should be updated
        result_src = page.get_attribute("#resultImage", "src")
        print(f"Result Image Src: {result_src}")

        if result_src != malicious_url:
             pytest.fail(f"FUNCTIONALITY FAILURE: Image src not updated correctly. Expected '{malicious_url}', got '{result_src}'")

        print("SECURITY SUCCESS: No XSS detected and functionality preserved.")
        browser.close()

if __name__ == "__main__":
    try:
        test_xss_vulnerability()
    except Exception as e:
        print(e)
        exit(1)
