## 2024-05-20 - Unescaped Single Quotes in URL parameters
**Vulnerability:** DOM-based XSS when assigning user-influenced URLs containing unescaped single quotes to `innerHTML`, specifically breaking out of single-quoted attributes like `onclick='...'`.
**Learning:** `encodeURIComponent()` does not escape single quotes.
**Prevention:** Use safe DOM manipulation APIs like `document.createElement` and direct property assignments instead of `innerHTML`.
