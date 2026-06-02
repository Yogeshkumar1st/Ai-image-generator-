## 2024-06-02 - [XSS in Image Gallery]
**Vulnerability:** Cross-Site Scripting (XSS) in `loadHistory` via unsanitized `innerHTML` when rendering image tags from `localStorage` history.
**Learning:** `innerHTML` allows arbitrary code execution if user-controlled input (even from `localStorage`, which could be injected or manipulated) is passed to it, specifically via event handlers like `onclick` or `onerror`.
**Prevention:** Use `document.createElement` and DOM properties (e.g., `img.src = url; img.onclick = () => viewImage(url);`) instead of string concatenation with `innerHTML`.
