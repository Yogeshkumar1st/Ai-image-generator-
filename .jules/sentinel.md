## 2024-05-24 - [XSS via Single-Quoted Attribute Breakout]
**Vulnerability:** A cross-site scripting (XSS) vulnerability was found where user input was directly interpolated into a single-quoted `onclick` HTML attribute via `innerHTML`.
**Learning:** Even if the input might seem to be somewhat constrained (like a URL string encoded with `encodeURIComponent()`), JavaScript's `encodeURIComponent()` does not escape single quotes (`'`). This allows an attacker to break out of the single-quoted HTML attribute and inject arbitrary JavaScript.
**Prevention:** Avoid string interpolation with `innerHTML` when handling user input. Instead, use safe DOM manipulation methods like `document.createElement()` and set properties directly (e.g., `element.src = value`, `element.onclick = function`).
