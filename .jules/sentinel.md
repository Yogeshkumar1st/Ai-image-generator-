## 2024-05-08 - Fix XSS via unescaped single quotes
**Vulnerability:** XSS in gallery history via single quotes in URL breaking out of template literals in innerHTML.
**Learning:** `encodeURIComponent` does not encode single quotes ('). Using innerHTML with single-quoted attributes and unescaped single quotes creates an XSS vector.
**Prevention:** Always use DOM API methods like `document.createElement` and direct property assignment instead of string interpolation for user data.
