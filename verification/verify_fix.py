
from playwright.sync_api import sync_playwright
import os
import time

def verify_history_images():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        # Load local index.html
        file_path = os.path.abspath("index.html")
        page.goto(f"file://{file_path}")

        # Inject valid images into history
        valid_url1 = "https://via.placeholder.com/150/0000FF/808080?text=Image1"
        valid_url2 = "https://via.placeholder.com/150/FF0000/FFFFFF?text=Image2"

        page.evaluate(f"""
            localStorage.setItem('xhistory', JSON.stringify([
                {{ url: '{valid_url1}', prompt: 'Blue Image' }},
                {{ url: '{valid_url2}', prompt: 'Red Image' }}
            ]));
        """)

        page.reload()

        # Click the Gallery tab explicitly using the class or text more specifically
        # The HTML has <div class="tab" onclick="switchTab('gallery')">Gallery</div>
        page.locator(".tab", has_text="Gallery").click()

        # Wait for the tab to become active
        # The active tab gets class 'active'. The second tab should be active.
        page.wait_for_selector(".tab:nth-child(2).active")

        # Wait for images to load in gallery
        page.wait_for_selector("#galleryGrid img")

        # Ensure #galleryTab is visible
        gallery_tab = page.locator("#galleryTab")
        if not gallery_tab.is_visible():
            print("Gallery tab is not visible!")

        # Take screenshot of the gallery
        screenshot_path = "verification/gallery_view_retry.png"
        page.screenshot(path=screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")

        browser.close()

if __name__ == "__main__":
    verify_history_images()
