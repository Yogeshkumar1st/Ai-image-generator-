## 2024-05-24 - [Fix XSS in gallery]
**Vulnerability:** XSS vulnerability through gallery item `url` injected into `onclick` attribute using `innerHTML`.
**Learning:** `encodeURIComponent` does not escape single quotes, which allows breaking out of inline event handler attributes like `onclick` when interpolating variables using `innerHTML`.
**Prevention:** Avoid building HTML dynamically with `innerHTML` and interpolating URLs or user input into attributes. Use `document.createElement` and direct property assignments (e.g. `img.onclick = () => viewImage(item.url)`).
