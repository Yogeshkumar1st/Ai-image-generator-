## 2024-05-24 - Unescaped Single Quotes in encodeURIComponent
**Vulnerability:** Stored DOM XSS in the image gallery history via unescaped single quotes.
**Learning:** JavaScript's `encodeURIComponent()` does not escape single quotes (`'`). User input encoded with this function can still break out of single-quoted HTML attributes like `onclick='...'`.
**Prevention:** Prefer using safe DOM manipulation APIs (e.g., `document.createElement`, direct property assignment) over `innerHTML` assignments when handling URLs or user input.