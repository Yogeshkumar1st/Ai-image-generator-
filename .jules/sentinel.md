## 2024-05-18 - [Stored XSS via localStorage and innerHTML]
**Vulnerability:** Unsanitized user data from localStorage rendered via innerHTML allowing Cross-Site Scripting (XSS).
**Learning:** Stored data in localStorage cannot be blindly trusted when constructing DOM elements, as malicious input can execute arbitrary JavaScript.
**Prevention:** Always use safe DOM API methods (e.g., document.createElement, textContent, or setAttribute) instead of innerHTML when rendering user-generated content or stored state.
