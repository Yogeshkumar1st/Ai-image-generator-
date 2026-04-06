import json
from playwright.sync_api import sync_playwright

def run_cuj(page):
    # Navigate to the file
    page.goto("file:///app/index.html")
    page.wait_for_timeout(500)

    # Inject mock data into localStorage with double serialization
    mock_history = [{"url": "https://image.pollinations.ai/prompt/test", "prompt": "test prompt"}]
    # xhistory expects a JSON string of an array of objects
    js_inject = f"localStorage.setItem('xhistory', {json.dumps(json.dumps(mock_history))});"
    page.evaluate(js_inject)

    # Switch to gallery tab
    page.evaluate("switchTab('gallery')")
    page.wait_for_timeout(500)

    # Wait for the gallery image to be rendered
    page.wait_for_selector(".gallery-item img")

    # Wait to stabilize
    page.wait_for_timeout(500)

    # Click on the image to test the onClick handler (it should switch back to creator tab)
    page.locator(".gallery-item img").click()
    page.wait_for_timeout(1000)

    # Take screenshot at the final state
    page.screenshot(path="/app/screenshots/verification.png")

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            record_video_dir="/app/videos"
        )
        page = context.new_page()
        try:
            run_cuj(page)
        finally:
            context.close()
            browser.close()
