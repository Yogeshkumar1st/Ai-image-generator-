## 2024-05-24 - [Fix XSS vulnerability in image onclick handler]
**Vulnerability:** XSS vulnerability when rendering gallery items due to unescaped single quotes in URLs interpolated into `onclick` attribute via `innerHTML`.
**Learning:** `encodeURIComponent` does not escape single quotes (`'`). This can create XSS vectors if these unescaped components are interpolated into single-quoted HTML attributes.
**Prevention:** Always rely on DOM API methods (e.g., `document.createElement`, `img.onclick`) instead of `innerHTML` for rendering user-generated content.
