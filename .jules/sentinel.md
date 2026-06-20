## 2025-01-23 - [Critical XSS Fixed in Dynamic Image Gallery]
**Vulnerability:** XSS via unescaped URL parameter in `div.innerHTML`.
**Learning:** `innerHTML` does not escape single quotes, even when parsing from JSON, leading to XSS if not properly sanitized and used.
**Prevention:** Avoid `innerHTML` when building dynamic DOM elements with user-controlled parameters, use programmatic element creation (e.g., `document.createElement('img')`) instead.
