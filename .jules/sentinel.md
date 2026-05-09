
## 2024-05-09 - [DOM XSS via unescaped single quotes in encodeURIComponent]
**Vulnerability:** A DOM XSS vulnerability existed in `index.html` where `encodeURIComponent` was used to encode user prompts, which were then interpolated into single-quoted HTML attributes via `innerHTML`.
**Learning:** Standard JavaScript `encodeURIComponent` does NOT encode single quotes (`'`). If an application relies on `encodeURIComponent` for sanitization and injects the output into single-quoted attributes (`<img src='...'>`), an attacker can easily break out of the attribute by providing a single quote and injecting a payload like `' onerror='alert(1)`.
**Prevention:** Never use `innerHTML` with string interpolation for user-controlled data, even if it has passed through `encodeURIComponent`. Always use the standard DOM API (`document.createElement`, `element.src = value`, `element.setAttribute`) to ensure the browser handles the data securely as a value rather than executing it as markup.
