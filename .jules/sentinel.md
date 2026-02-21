# Sentinel Journal

## 2026-02-21 - DOM-based XSS in Gallery History
**Vulnerability:** Found a DOM-based Cross-Site Scripting (XSS) vulnerability where user input stored in `localStorage` was rendered using `innerHTML` without proper sanitization. Specifically, the `onclick` attribute was constructed using template literals, allowing a malicious URL containing a single quote to break out of the string context and execute arbitrary JavaScript.
**Learning:** Relying on `encodeURIComponent` to sanitize URLs for HTML attributes is insufficient because it does not escape single quotes (`'`), which are valid delimiters in JavaScript strings within HTML attributes.
**Prevention:** Always use safe DOM manipulation methods (e.g., `document.createElement`, `element.setAttribute`, `element.addEventListener`) instead of `innerHTML` when handling user-controlled data. This ensures that data is treated as text/values rather than executable code.
