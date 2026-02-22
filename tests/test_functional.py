from playwright.sync_api import sync_playwright
import os
import json

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the page
        page_path = f"file://{os.path.abspath('index.html')}"
        page.goto(page_path)

        # Inject valid history into localStorage
        valid_history = [
            {"url": "https://via.placeholder.com/150", "prompt": "Test Image 1"},
            {"url": "https://via.placeholder.com/200", "prompt": "Test Image 2"}
        ]

        page.evaluate(f"""
            localStorage.setItem('xhistory', JSON.stringify({json.dumps(valid_history)}));
        """)

        # Click the "Gallery" tab to trigger loadHistory
        page.click("text=Gallery")

        # Check if images are displayed
        images = page.locator(".gallery-item img")
        count = images.count()

        if count == 2:
            print("FUNCTIONAL TEST PASSED: Correct number of images displayed.")
        else:
            print(f"FUNCTIONAL TEST FAILED: Expected 2 images, found {count}.")
            browser.close()
            exit(1)

        # Verify src attributes
        src1 = images.nth(0).get_attribute("src")
        # LocalStorage unshift adds to the start, so order is reversed if we just added.
        # But here we set the whole array. loadHistory iterates over it.
        # history.forEach appendChild so order is preserved as in the array.

        # Wait, let's check loadHistory again.
        # history.forEach(item => { ... galleryGrid.appendChild(div); });

        if src1 == valid_history[0]["url"]:
             print("FUNCTIONAL TEST PASSED: Image source is correct.")
        else:
             print(f"FUNCTIONAL TEST FAILED: Expected {valid_history[0]['url']}, found {src1}.")
             browser.close()
             exit(1)

        browser.close()

if __name__ == "__main__":
    run()
