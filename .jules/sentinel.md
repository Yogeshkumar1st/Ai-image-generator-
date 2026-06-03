## 2024-05-24 - DOM XSS via innerHTML and localStorage
**Vulnerability:** Found DOM XSS where JSON parsed from localStorage (`xhistory`) was directly injected into the DOM via `innerHTML` without sanitization.
**Learning:** Data from `localStorage` can be manipulated by malicious scripts or extensions and should not be trusted.
**Prevention:** Always use safe DOM APIs like `document.createElement` and set properties (e.g., `src`, `onclick`) directly instead of `innerHTML` when rendering user-controllable data.
