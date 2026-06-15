## 2024-06-15 - Fix XSS in History Rendering
**Vulnerability:** XSS in the gallery history due to rendering user-supplied URLs via `innerHTML`. `encodeURIComponent` does not encode single quotes, allowing an attacker to escape the `onclick` handler string and execute arbitrary JavaScript.
**Learning:** `innerHTML` shouldn't be used with interpolated user input, especially within attributes like `onclick`, even if the input has passed through `encodeURIComponent()`.
**Prevention:** Always use safe DOM APIs like `document.createElement()`, `element.src = ...`, and `element.onclick = ...` instead of `innerHTML` to bind event handlers and attributes dynamically.
