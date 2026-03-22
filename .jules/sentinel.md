## 2024-05-20 - encodeURIComponent Does Not Encode Single Quotes
**Vulnerability:** XSS via unescaped single quotes in `onclick` attributes.
**Learning:** Standard `encodeURIComponent` in JavaScript does not escape single quotes (`'`). When an encoded string is interpolated into an HTML attribute bounded by single quotes (e.g., `onclick="viewImage('${url}')"`), an attacker can supply a single quote to break out of the attribute and inject arbitrary JavaScript, leading to Cross-Site Scripting (XSS).
**Prevention:** Always use safe DOM API methods (`document.createElement`, `element.src = url`, `element.addEventListener`) instead of string concatenation and `innerHTML` when rendering user-generated content or URLs.
