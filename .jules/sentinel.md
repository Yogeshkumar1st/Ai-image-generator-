## 2025-05-23 - [Unsafe localStorage Usage]
**Vulnerability:** Found direct injection of `localStorage` data into the DOM using `innerHTML` in `loadHistory` function.
**Learning:** The application treats `localStorage` as trusted storage, but it can be manipulated by other scripts (XSS) or user input, leading to stored XSS vulnerabilities.
**Prevention:** Avoid `innerHTML` when rendering user-generated content or data from storage. Use `document.createElement` and set attributes/properties securely.
