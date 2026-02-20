## 2026-02-20 - [XSS in History Loading]
**Vulnerability:** DOM-based XSS in `loadHistory` function where user input (prompts) was injected directly into `onclick` attribute via `innerHTML`.
**Learning:** `localStorage` data was trusted and rendered unsafely. Using `innerHTML` with string interpolation for event handlers allows code injection if input is not strictly controlled or escaped.
**Prevention:** Always use `document.createElement()` and assign properties (e.g., `element.onclick = fn`) instead of constructing HTML strings. Treat `localStorage` content as untrusted user input.
