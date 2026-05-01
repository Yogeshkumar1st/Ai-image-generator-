
## 2024-05-15 - [CRITICAL] Incomplete encoding in DOM XSS via encodeURIComponent
**Vulnerability:** DOM-based XSS vulnerability in `index.html` where `item.url` was injected into a single-quoted `onclick` attribute within an `innerHTML` string. The payload was seemingly encoded with `encodeURIComponent`, but this function does NOT encode single quotes (`'`).
**Learning:** Standard JavaScript `encodeURIComponent` does not encode single quotes (`'`). This creates a critical XSS vector if these unescaped components are interpolated into single-quoted HTML attributes in `innerHTML` templates.
**Prevention:** Avoid `innerHTML` entirely for rendering user-generated content. Always rely on DOM API methods (`document.createElement`, `element.setAttribute()`, `element.onclick = ...`) where the browser automatically handles secure string escaping for attributes and properties.
