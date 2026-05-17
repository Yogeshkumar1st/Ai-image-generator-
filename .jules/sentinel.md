## 2024-05-17 - [XSS in loadHistory]
**Vulnerability:** XSS via `innerHTML` and unescaped single quotes in `onclick` attribute when loading gallery history. `encodeURIComponent` does not encode single quotes, which allows escaping the `onclick="viewImage('...` handler.
**Learning:** `encodeURIComponent` does not escape single quotes (`'`). When interpolating such a URL into an HTML attribute wrapped in single quotes via `innerHTML`, it leads to XSS.
**Prevention:** Avoid `innerHTML` for dynamic content. Use DOM APIs like `document.createElement`, `img.src = ...`, and direct event handler assignments (`img.onclick = ...`) which are not susceptible to this string-interpolation XSS.
