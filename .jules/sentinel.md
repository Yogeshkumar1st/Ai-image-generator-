## 2024-07-10 - [encodeURIComponent XSS vulnerability]
**Vulnerability:** XSS payload executed by escaping single quotes even when using `encodeURIComponent`.
**Learning:** `encodeURIComponent` does not encode single quotes ('). Using `innerHTML` to interpolate string components with single quotes leaves the code vulnerable to XSS.
**Prevention:** Do not use `innerHTML` to interpolate string components. Use `document.createElement` and direct property assignment instead.
