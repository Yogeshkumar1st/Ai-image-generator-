
import pytest
from playwright.sync_api import sync_playwright
import os
import json

@pytest.fixture(scope="module")
def browser_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        yield context
        browser.close()

def test_xss_vulnerability(browser_context):
    page = browser_context.new_page()
    file_path = os.path.abspath("index.html")
    file_url = f"file://{file_path}"

    page.goto(file_url)

    # Malicious payload:
    # If the code uses `innerHTML = " <img src='${url}' ...>"`
    # A payload like `"><img src=x onerror=window.xss=true>` will result in:
    # `<img src=""><img src=x onerror=window.xss=true> ...`
    malicious_payload = '"><img src=x onerror=window.xss=true>'

    # Inject malicious payload into localStorage
    page.evaluate(f"""
        localStorage.setItem('xhistory', JSON.stringify([
            {{ url: '{malicious_payload}', prompt: 'hacked' }}
        ]));
    """)

    # Reload page to ensure clean state
    page.reload()

    # Click the "Gallery" tab to trigger `loadHistory()` which injects the HTML
    page.click("text=Gallery")

    # Wait a moment for the XSS to execute
    page.wait_for_timeout(500)

    # Check if window.xss is true
    is_triggered = page.evaluate("window.xss === true")

    # Assert that XSS was NOT triggered.
    # If the code is vulnerable, `is_triggered` will be True, and this assertion will fail.
    # Note: We want to DETECT the vulnerability first, so we expect this to FAIL if the code is vulnerable.
    assert not is_triggered, "XSS Vulnerability detected! Malicious script executed via localStorage."

    page.close()

def test_history_functionality(browser_context):
    page = browser_context.new_page()
    file_path = os.path.abspath("index.html")
    file_url = f"file://{file_path}"

    page.goto(file_url)

    valid_url = "https://via.placeholder.com/150"

    # Set up localStorage with a valid image
    page.evaluate(f"""
        localStorage.setItem('xhistory', JSON.stringify([
            {{ url: '{valid_url}', prompt: 'test image' }}
        ]));
    """)

    # Reload to ensure clean state
    page.reload()

    # Click Gallery tab to load history
    page.click("text=Gallery")

    # Verify the image is present in the gallery grid
    # We search for an img element with the specific src
    # The original code uses: <img src="${item.url}" onclick="...">
    gallery_img = page.locator(f"#galleryGrid img[src='{valid_url}']")

    # Wait for it to appear
    try:
        gallery_img.wait_for(state="visible", timeout=2000)
    except:
        pass # It might fail if not visible yet

    assert gallery_img.count() > 0, "History image not loaded in gallery."

    # Click the image
    gallery_img.first.click()

    # Verify it switches back to Creator tab
    creator_tab = page.locator("#creatorTab")
    assert creator_tab.is_visible(), "Did not switch back to Creator tab."

    # Verify the main result image is updated
    result_img = page.locator("#resultImage")
    assert result_img.is_visible()
    # Note: src attribute might be absolute path in browser, so check if it ends with valid_url or contains it
    src = result_img.get_attribute("src")
    assert valid_url in src, "Image did not load in the result area."

    page.close()
