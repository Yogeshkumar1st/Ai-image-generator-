## 2025-02-12 - DOM-Based XSS in Image Gallery
**Vulnerability:** XSS via `innerHTML` assignment in `loadHistory()` function which directly parses user-controlled URLs from `localStorage`. The payload was `'-alert(1)-'` which was breaking out of single quotes in `onclick="viewImage('url')"`.
**Learning:** `encodeURIComponent` does not encode single quotes (`'`), so URLs can still break out of attribute context if single-quoted. Furthermore, assigning directly to `innerHTML` allows arbitrary HTML execution.
**Prevention:** Use safe DOM manipulation APIs like `document.createElement`, set properties directly (e.g. `.src`), and use `addEventListener` instead of inline handlers like `onclick`.
