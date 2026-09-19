## 2024-05-28 - DOM-based XSS in loadHistory
**Vulnerability:** DOM-based XSS through single-quote breakout in `onclick` attribute when creating gallery items using `innerHTML`.
**Learning:** `encodeURIComponent()` escapes double quotes but not single quotes (`'`). When inserting user-controlled URLs (like the Pollinations AI URL containing the encoded prompt) into a single-quoted HTML attribute (like `onclick='...'`), an attacker can break out of the attribute and execute arbitrary JavaScript.
**Prevention:** Use safe DOM manipulation APIs like `document.createElement`, `element.setAttribute`, or direct property assignment instead of string interpolation and `innerHTML`.
