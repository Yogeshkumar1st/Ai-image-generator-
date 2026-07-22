## 2025-05-18 - XSS via localStorage in Gallery History
**Vulnerability:** XSS vulnerability in `loadHistory` due to rendering `localStorage` data using `innerHTML` with unsanitized URL properties.
**Learning:** Building HTML dynamically via template literals with untrusted properties like `url` and injecting it via `innerHTML` is inherently unsafe and can easily lead to XSS.
**Prevention:** Use secure DOM manipulation methods like `document.createElement`, `.src`, and `.onclick` instead of `innerHTML` when handling user-controlled data or properties from `localStorage`.
