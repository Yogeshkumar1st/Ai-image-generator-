## 2024-10-04 - XSS in loadHistory
**Vulnerability:** DOM-based XSS via unsafe innerHTML assignment with dynamically generated unescaped single quotes in the `onclick` handler attributes inside `loadHistory`.
**Learning:** `encodeURIComponent()` does not escape single quotes, allowing for attribute breakout and Javascript injection when interpolated into an HTML string and inserted via `innerHTML`.
**Prevention:** Avoid `innerHTML` with user-supplied URL data (even encoded). Utilize safe DOM manipulation APIs like `document.createElement()` and assign event handlers directly as functions (`element.onclick = () => {...}`).
