## 2024-05-28 - [DOM XSS via unencoded single quotes]
**Vulnerability:** DOM-based Cross-Site Scripting (XSS) in `loadHistory()` due to `encodeURIComponent` not encoding single quotes (`'`), which are then interpolated into an inline event handler (`onclick="viewImage('${item.url}')"`) via `innerHTML`.
**Learning:** Standard JavaScript `encodeURIComponent` does not encode single quotes. This creates XSS vectors when unescaped single quotes break out of string literals in event handlers.
**Prevention:** Avoid `innerHTML` and inline event handlers with string interpolation. Always use DOM APIs (`document.createElement`, element properties) or event listeners for dynamic content.
