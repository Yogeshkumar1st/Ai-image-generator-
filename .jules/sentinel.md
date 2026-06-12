## 2025-01-01 - DOM XSS in LocalStorage History Rendering
**Vulnerability:** DOM-based XSS via innerHTML injection when rendering image history items loaded from localStorage.
**Learning:** Interpolating URLs into `innerHTML` is insecure even if standard URL encoding is assumed, as single quotes are not escaped and permit breaking out of the attribute.
**Prevention:** Use `document.createElement` and direct property assignments (like `img.src` and `img.onclick`) rather than `innerHTML` when building DOM elements with user-controlled input.
