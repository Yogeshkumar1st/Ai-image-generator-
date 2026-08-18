## 2024-05-24 - DOM-based XSS via encodeURIComponent bypassing single quotes
**Vulnerability:** XSS payload executed when clicking history items because `encodeURIComponent` does not escape single quotes (`'`), allowing breakout from `onclick='...'` in `innerHTML` assignment.
**Learning:** `encodeURIComponent()` does not escape single quotes, so user input encoded with it can still break out of single-quoted HTML attributes when injected via `innerHTML`.
**Prevention:** Prefer using safe DOM manipulation APIs (e.g., `document.createElement`, direct property assignment like `img.onclick`) over `innerHTML` string concatenation.
