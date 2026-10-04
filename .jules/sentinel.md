## 2024-10-26 - DOM-based XSS via unescaped single quotes
**Vulnerability:** DOM-based XSS in the gallery tab where user input encoded with `encodeURIComponent()` was inserted into a single-quoted `onclick` attribute via `innerHTML`.
**Learning:** JavaScript's `encodeURIComponent()` does not escape single quotes (`'`), allowing attackers to break out of single-quoted HTML attributes and execute arbitrary code.
**Prevention:** Use safe DOM manipulation APIs (e.g., `document.createElement`, direct property assignment) instead of `innerHTML` assignments when inserting dynamic data into the DOM.
