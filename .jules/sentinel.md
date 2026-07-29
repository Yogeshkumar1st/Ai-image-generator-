## 2024-07-29 - Prevent XSS in gallery history rendering
**Vulnerability:** XSS via unsanitized `item.url` passed to `div.innerHTML` in the local storage history rendering logic.
**Learning:** Data from local storage shouldn't be trusted when rendering. Injecting data can lead to DOM-based XSS when `innerHTML` is used instead of safe DOM manipulation methods.
**Prevention:** Avoid using `innerHTML` with unsanitized user input or untrusted data sources like `localStorage`. Prefer using `document.createElement()` and setting attributes directly.