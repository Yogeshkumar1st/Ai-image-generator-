import pytest
from playwright.sync_api import sync_playwright
import os
import json

def test_gallery_loading():
    """
    Tests that legitimate images load correctly in the gallery.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the page
        page.goto(f"file://{os.getcwd()}/index.html")

        # Valid payload
        valid_url = "https://via.placeholder.com/150"
        payload = [
            {
                "url": valid_url,
                "prompt": "Test Image"
            }
        ]

        # Set localStorage
        page.evaluate(f"localStorage.setItem('xhistory', JSON.stringify({json.dumps(payload)}))")

        # Switch to Gallery tab
        page.click("text=Gallery")

        # Check if the image is present in the DOM
        # The selector should be .gallery-item img[src="..."]
        img_locator = page.locator(f'.gallery-item img[src="{valid_url}"]')

        # Wait for it to be attached
        img_locator.wait_for(state="attached", timeout=5000)

        assert img_locator.count() == 1, "Gallery image not found"

        browser.close()
