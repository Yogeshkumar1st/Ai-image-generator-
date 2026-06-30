## 2024-06-30 - XSS via unsanitized innerHTML
**Vulnerability:** XSS vulnerability in `loadHistory` where `localStorage` data was injected into the DOM via string interpolation and `innerHTML`.
**Learning:** Using `innerHTML` with unsanitized user data, even if stored locally (like `localStorage`), is a major security risk.
**Prevention:** Avoid `innerHTML` for dynamic content creation. Use `document.createElement`, direct property assignments (like `img.src` and `img.onclick`), and `appendChild` instead.
