## 2024-08-17 - Fix DOM-based XSS in gallery history rendering
**Vulnerability:** DOM-based XSS in `loadHistory` function due to unsafe assignment of user-controlled `item.url` to `innerHTML` when rendering gallery history.
**Learning:** `encodeURIComponent()` does not escape single quotes, allowing breakout from single-quoted HTML attributes like `onclick='...'`.
**Prevention:** Use safe DOM manipulation APIs like `document.createElement` and direct property assignment (e.g. `img.src = item.url`, `img.onclick`) instead of string concatenation with `innerHTML`.
