## 2024-05-24 - DOM XSS in Gallery Renderer
**Vulnerability:** An XSS vulnerability existed when rendering user image generation history, because `loadHistory` interpolated user-controlled data (`item.url`) directly into HTML strings (`div.innerHTML`).
**Learning:** Using `innerHTML` with string interpolation (even for attributes like `src` or `onclick`) is unsafe, as an attacker can inject single quotes to break out of attributes and execute malicious code. Even if URLs are encoded, characters like `'` may remain unencoded or be interpreted during rendering.
**Prevention:** Always use safe DOM APIs like `document.createElement()`, set element properties like `.src` directly, and attach event listeners via `.addEventListener()` instead of inline `onclick` attributes.
