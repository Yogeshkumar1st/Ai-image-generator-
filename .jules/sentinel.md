## 2024-07-08 - XSS via innerHTML with unescaped single quotes
**Vulnerability:** XSS vulnerability in image gallery history. `encodeURIComponent` does not escape single quotes (`'`), allowing an attacker to break out of HTML attributes like `onclick` when URLs are interpolated using `innerHTML`.
**Learning:** Never interpolate unescaped variables directly into HTML strings or attributes using `innerHTML`. `encodeURIComponent` does not make a string safe for injection into an HTML attribute wrapped in single quotes.
**Prevention:** Use safe DOM manipulation like `document.createElement()` and assign properties (e.g., `img.src` and `img.onclick`) directly.
