## 2024-10-24 - DOM-based XSS via `encodeURIComponent` not escaping single quotes
**Vulnerability:** DOM-based XSS in gallery history rendering where URLs are inserted into `innerHTML` using single quotes for the `onclick` attribute.
**Learning:** JavaScript's `encodeURIComponent()` does not escape single quotes (`'`). When user input encoded with this function is placed into single-quoted HTML attributes (like `onclick='...'`), attackers can break out of the attribute and inject arbitrary scripts.
**Prevention:** Prefer using safe DOM manipulation APIs (e.g., `document.createElement`, direct property assignment) over `innerHTML` assignments when dealing with potentially untrusted data.
