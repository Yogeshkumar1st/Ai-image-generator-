## 2024-05-24 - Fix XSS in gallery loading
**Vulnerability:** XSS vulnerability in `loadHistory()` caused by interpolating unsanitized URL into `innerHTML` using string templates.
**Learning:** Even if data is controlled locally in `localStorage`, using `innerHTML` to interpolate dynamic values, especially URLs which may contain unescaped single quotes or malicious payloads, exposes the application to XSS.
**Prevention:** Avoid `innerHTML` for dynamic UI construction. Instead, use safe DOM manipulation via `document.createElement` and direct property assignments (e.g. `img.src = url`).
