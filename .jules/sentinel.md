## 2025-02-14 - Prevent XSS in dynamic HTML generation
**Vulnerability:** XSS via `innerHTML` and untrusted URLs breaking out of HTML attributes.
**Learning:** Using `innerHTML` with variable interpolation inside HTML attributes (like `src` or `onclick`) allows attackers to break out and execute arbitrary JS, even if the URL appears to be from a controlled source.
**Prevention:** Use safer DOM APIs like `document.createElement`, direct property assignment (`img.src = url`), and event listeners (`img.onclick`) instead of string-based HTML construction.
