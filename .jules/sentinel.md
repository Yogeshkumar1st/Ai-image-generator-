## 2025-10-24 - DOM-based XSS via encodeURIComponent Bypass
**Vulnerability:** A DOM-based XSS vulnerability existed in the `loadHistory()` function where user input was interpolated directly into `div.innerHTML`.
**Learning:** `encodeURIComponent()` does not escape single quotes (`'`). This allows breaking out of single-quoted HTML attributes like `onclick='...'`.
**Prevention:** Avoid `innerHTML` whenever possible and rely on native DOM element creation and property assignment to implicitly handle encoding.