## 2024-07-24 - Secure DOM Manipulation
**Vulnerability:** XSS via `innerHTML` and string interpolation in `loadHistory()`.
**Learning:** Building HTML structures using template literals and injecting them via `innerHTML` with unsanitized data allows malicious script execution, especially when handling dynamic properties like `url`. Even when data is passed through `encodeURIComponent` elsewhere, it might not escape single quotes, breaking attribute encapsulation.
**Prevention:** Always use safe DOM element creation APIs (e.g., `document.createElement`) and direct property assignment (e.g., `img.src = url`, `img.onclick = ...`) rather than concatenating HTML strings and assigning them to `innerHTML`.
