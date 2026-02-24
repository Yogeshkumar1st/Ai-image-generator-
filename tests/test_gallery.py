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

        # Valid payload
        valid_url = "https://example.com/image.png"
        payload = [{"url": valid_url, "prompt": "Valid Test"}]

        # Serialize to JSON string for localStorage
        json_str = json.dumps(payload)

        # Set localStorage
        page.evaluate("(data) => localStorage.setItem('xhistory', data)", json_str)

        # Switch tab to trigger loadHistory
        page.click("text=Gallery")

        # Check if the image is rendered correctly
        try:
            # We expect an img tag with the src
            img_locator = page.locator(f"img[src='{valid_url}']")
            img_locator.wait_for(timeout=2000)

            # Click the image to verify onclick handler
            img_locator.click()

            # Check if result area shows the image
            result_img = page.locator("#resultImage")
            # Wait for result image to be visible
            result_img.wait_for(state="visible", timeout=2000)

            # Check src matches
            src = result_img.get_attribute("src")
            if src == valid_url:
                print("PASS: Gallery functionality verified.")
                browser.close()
                sys.exit(0)
            else:
                print(f"FAIL: Result image src mismatch. Expected {valid_url}, got {src}")
                browser.close()
                sys.exit(1)

        except Exception as e:
            print(f"FAIL: Functionality test failed: {e}")
            browser.close()
            sys.exit(1)

if __name__ == "__main__":
    run()
