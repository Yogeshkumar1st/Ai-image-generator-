## 2024-08-26 - DOM-based XSS via encodeURIComponent bypass
**Vulnerability:** User prompt containing single quotes can break out of string context in `onclick` attribute in history gallery due to `encodeURIComponent` not escaping single quotes and parentheses.
**Learning:** `encodeURIComponent` does not encode characters like single quotes (`'`) and parentheses (`(`, `)`), so placing its output directly inside inline event handlers via `innerHTML` is unsafe and can lead to DOM XSS.
**Prevention:** Use safe DOM manipulation APIs (e.g., `document.createElement`, direct property assignment `img.onclick = ...`) instead of `innerHTML` assignments to prevent execution of injected JavaScript.
