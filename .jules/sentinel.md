## 2024-05-24 - DOM-based XSS via innerHTML and single quotes
**Vulnerability:** A DOM-based Cross-Site Scripting (XSS) vulnerability exists in `index.html` where user-controlled image URLs are rendered using `innerHTML`. JavaScript's `encodeURIComponent()` does not escape single quotes (`'`), allowing an attacker to break out of single-quoted HTML attributes like `onclick='...'`.
**Learning:** Even when user input is encoded with `encodeURIComponent()`, it is not safe to inject directly into single-quoted HTML attributes using `innerHTML` because single quotes remain unescaped.
**Prevention:** Prefer using safe DOM manipulation APIs (e.g., `document.createElement`, direct property assignment) over `innerHTML` assignments when rendering user-controlled data.
