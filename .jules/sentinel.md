## 2024-05-24 - [XSS] Unescaped Single Quotes in innerHTML
**Vulnerability:** XSS payload injected via `url` parameter in `localStorage` history due to string interpolation into `innerHTML` `onclick` attribute with unescaped single quotes. Standard `encodeURIComponent` does not encode single quotes.
**Learning:** Using `innerHTML` to interpolate data containing unescaped single quotes into HTML attributes (like `onclick`) creates an XSS vulnerability even if the data appears to be a URL.
**Prevention:** Always use DOM API methods (e.g., `document.createElement`, `setAttribute`, event listeners) instead of `innerHTML` for rendering user-generated content, especially when attributes are involved.
