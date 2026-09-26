## 2024-05-18 - [DOM-based XSS via innerHTML]
**Vulnerability:** A DOM-based XSS vulnerability existed where user input passed through `encodeURIComponent` was inserted into an HTML string with single quotes via `innerHTML`. `encodeURIComponent` does not escape single quotes, allowing the string to break out of the `onclick` attribute and execute arbitrary JavaScript.
**Learning:** Using string interpolation with `innerHTML` for dynamic content is inherently risky, even with partial encoding, especially inside event handler attributes.
**Prevention:** Always use safe DOM APIs like `document.createElement` and assign properties directly (e.g., `img.src = ...`, `img.onclick = ...`) rather than constructing HTML strings.
