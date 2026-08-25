## 2024-05-23 - DOM-based XSS in Gallery
**Vulnerability:** DOM-based Cross-Site Scripting (XSS) via `innerHTML` when rendering user-controlled data (image URLs) from `localStorage`.
**Learning:** Using `innerHTML` to interpolate string values from unvalidated sources like `localStorage` allows attackers to inject arbitrary executable scripts by breaking out of HTML attributes.
**Prevention:** Always use safe DOM manipulation APIs such as `document.createElement()` and direct property assignments (e.g., `img.src = ...`) instead of `innerHTML` when handling user-controlled data.
