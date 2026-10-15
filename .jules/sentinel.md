## 2024-05-24 - encodeURIComponent Does Not Escape Single Quotes
**Vulnerability:** DOM-based XSS via unescaped single quotes in `localStorage` URLs injected into single-quoted HTML event handlers (`onclick='...'`).
**Learning:** `encodeURIComponent` does not encode single quotes (`'`). When interpolating user input into single-quoted HTML attributes using `innerHTML`, an attacker can break out of the attribute and execute arbitrary JavaScript.
**Prevention:** Prefer using safe DOM manipulation APIs (e.g., `document.createElement`, direct property assignment like `element.onclick`) over `innerHTML` assignments when handling user-controlled data.
