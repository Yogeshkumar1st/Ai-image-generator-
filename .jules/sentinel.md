## 2024-05-15 - Unescaped Single Quotes in URL Components
**Vulnerability:** XSS via unescaped single quotes in `encodeURIComponent` outputs.
**Learning:** `encodeURIComponent` does not encode single quotes ('). When these are interpolated into single-quoted HTML attributes like `onclick='...'`, an attacker can break out of the attribute and inject JavaScript.
**Prevention:** Avoid interpolating variables into HTML attributes string literals. Always use DOM APIs like `document.createElement`, `element.setAttribute`, or event listener assignments (`element.onclick = ...`) to safely construct DOM elements.
