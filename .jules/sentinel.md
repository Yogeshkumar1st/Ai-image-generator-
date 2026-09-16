## 2024-05-15 - DOM-based XSS via innerHTML and string interpolation
**Vulnerability:** A DOM-based Cross-Site Scripting (XSS) vulnerability was found in the `loadHistory()` function. User input from `localStorage` was embedded directly into the DOM using `.innerHTML` with string interpolation into an `onclick` attribute.
**Learning:** `encodeURIComponent()` does not escape single quotes (`'`). This allows an attacker to break out of single-quoted HTML attributes (like `onclick='...'`) when the encoded input is injected via `.innerHTML`.
**Prevention:** Always use safe DOM manipulation APIs (e.g., `document.createElement`, direct property assignment `img.src`, `img.onclick`) instead of assigning complex HTML strings containing user data to `innerHTML`.
