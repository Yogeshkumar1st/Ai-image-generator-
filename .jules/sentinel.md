## 2024-07-27 - Fix XSS Vulnerability in History Gallery
**Vulnerability:** XSS vulnerability found in `loadHistory` due to injecting user-controlled URLs directly into `innerHTML` without sanitization.
**Learning:** Avoid using `innerHTML` for displaying user-controlled input, particularly when constructing complex HTML tags where attributes could contain execution payloads.
**Prevention:** Use DOM API methods like `document.createElement()` to create DOM elements safely, assigning properties (like `img.src`) which safely escapes the values.
