## 2024-05-12 - Fix XSS in loadHistory via DOM APIs
**Vulnerability:** XSS via unescaped single quotes in `item.url` bypassing standard `encodeURIComponent` and injected via `innerHTML` into an `onclick` attribute.
**Learning:** Always use DOM APIs like `document.createElement`, `img.src`, and `img.onclick` to assign dynamic variables instead of `innerHTML`, even if the string seems safely encoded, as standard encoding might not cover single quotes.
**Prevention:** Enforce using DOM APIs instead of `innerHTML` for rendering user-generated content across the project.
