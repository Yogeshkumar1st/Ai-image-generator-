## 2025-01-24 - DOM XSS in encodeURIComponent bypass
**Vulnerability:** DOM-based XSS when injecting `encodeURIComponent` output into single-quoted event handler attributes (`onclick='...'`) via `innerHTML`.
**Learning:** JavaScript's `encodeURIComponent()` does not escape single quotes (`'`). Attackers can break out of single-quoted HTML attributes even if the input was encoded.
**Prevention:** Use safe DOM manipulation APIs (e.g., `document.createElement`, direct property assignment like `element.src` and `element.onclick`) instead of assigning raw strings to `innerHTML`.
