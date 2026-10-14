## 2024-05-18 - Prevent DOM-based XSS in Gallery View
**Vulnerability:** The application was vulnerable to DOM-based XSS when displaying the user's generated image history in the gallery tab. User input encoded with `encodeURIComponent()` does not escape single quotes (`'`). This meant a malicious URL could break out of the single-quoted `onclick` attribute when injected via `innerHTML`: `<img src="..." onclick="viewImage('${item.url}')">`.
**Learning:** `encodeURIComponent()` does not escape single quotes, leaving single-quoted HTML attributes vulnerable if input is injected via `innerHTML`.
**Prevention:** Always use safe DOM manipulation APIs (e.g., `document.createElement`, direct property assignment like `element.onclick`) instead of `innerHTML` when handling user data or attributes.
