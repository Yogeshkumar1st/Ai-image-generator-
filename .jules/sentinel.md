## 2024-05-24 - Fix DOM-based XSS in Gallery
**Vulnerability:** DOM-based XSS via `innerHTML` injection in the gallery tab history loader, where user input (prompt) encoded with `encodeURIComponent` was interpolated into an HTML string within a single-quoted attribute (`onclick='...'`).
**Learning:** `encodeURIComponent` does not escape single quotes (`'`). Passing user-controlled data into `innerHTML` inside single-quoted attributes is extremely dangerous, even if the data is URL-encoded.
**Prevention:** Use safe DOM manipulation APIs like `document.createElement`, `element.src`, and `element.onclick` instead of `innerHTML` when handling user input or external data.
