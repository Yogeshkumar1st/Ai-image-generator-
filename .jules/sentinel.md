## 2025-05-24 - DOM-based XSS in Gallery View
**Vulnerability:** Cross-Site Scripting (XSS) via `innerHTML` when interpolating user-controlled image URLs from localStorage into the DOM.
**Learning:** Interpolating user data directly into `innerHTML` strings without proper escaping allows attribute breakout. The application was vulnerable to escaping the `onclick` attribute using single quotes.
**Prevention:** Always use safe DOM APIs like `document.createElement()`, setting properties (e.g., `src`) and attaching event listeners (e.g., `onclick`) directly on the node.