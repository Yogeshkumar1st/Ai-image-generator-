## 2024-07-23 - DOM-based XSS in Gallery History
**Vulnerability:** A DOM-based XSS vulnerability existed in `loadHistory()` because user-controlled data (`url`) was inserted directly into an inline HTML string using `innerHTML` and unescaped inside an `onclick` attribute.
**Learning:** Using `innerHTML` to interpolate URL components even if they are processed with `encodeURIComponent` does not escape single quotes (`'`) and leaves the code vulnerable to XSS inside HTML attributes.
**Prevention:** Always use safe DOM manipulation methods like `document.createElement` and direct property assignments (`img.src`, `img.onclick`) instead of constructing HTML strings with `innerHTML`.
