## 2024-05-18 - XSS in DOM Injection via innerHTML
**Vulnerability:** XSS vulnerability through unsafe string interpolation in `innerHTML` with single-quoted attributes. The `encodeURIComponent` function doesn't escape single quotes, allowing an attacker to break out of the `onclick='...'` attribute.
**Learning:** Even when inputs are partially encoded, using `innerHTML` with string interpolation into attributes is extremely risky. Single quotes are not escaped by `encodeURIComponent`, leading to XSS if used inside a single-quoted HTML attribute.
**Prevention:** Always use safe DOM manipulation methods like `document.createElement()`, setting properties like `element.src` and `element.onclick` directly, instead of using `innerHTML` with untrusted data.
