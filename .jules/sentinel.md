## 2024-05-29 - DOM-based XSS via encodeURIComponent
**Vulnerability:** The application stores `encodeURIComponent`-encoded URLs in `localStorage` and injects them into the DOM using `innerHTML` with a single-quoted `onclick` attribute (e.g., `onclick="viewImage('${item.url}')"`).
**Learning:** `encodeURIComponent()` does not escape single quotes (`'`). This allows an attacker to break out of single-quoted HTML attributes and execute arbitrary JavaScript.
**Prevention:** Prefer using safe DOM manipulation APIs (e.g., `document.createElement`, direct property assignment) over `innerHTML` string assignments when handling user input.
