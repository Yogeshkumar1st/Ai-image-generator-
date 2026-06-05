## 2024-05-24 - Fix XSS in History Rendering
**Vulnerability:** XSS vulnerability in `loadHistory()` caused by unescaped single quotes in `item.url` breaking out of the `onclick` handler string literal when rendered via `innerHTML`.
**Learning:** Using string interpolation with `innerHTML` for dynamically constructing event handlers (e.g. `onclick="..."`) is dangerous if the injected data contains quotes, as it can break out of the attribute and execute arbitrary code.
**Prevention:** Avoid `innerHTML` for dynamic content. Instead, use safe DOM manipulation methods like `document.createElement()`, assign properties directly (e.g., `img.src = item.url`), and attach event listeners securely (e.g., `img.onclick = () => viewImage(item.url)`).
