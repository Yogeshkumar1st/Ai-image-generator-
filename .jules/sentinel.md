## 2024-05-18 - XSS via unescaped single quotes in encodeURIComponent
**Vulnerability:** XSS payload was injected into an `onclick` handler via `encodeURIComponent` output.
**Learning:** `encodeURIComponent` does not encode single quotes (`'`), allowing an attacker to break out of single-quoted HTML attributes or inline JS function arguments.
**Prevention:** Use secure DOM API methods (`document.createElement`, `setAttribute`, etc.) instead of interpolating data into `innerHTML`, especially for event handlers.
