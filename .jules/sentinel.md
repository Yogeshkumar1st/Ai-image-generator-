## 2024-08-07 - XSS via encodeURIComponent bypass
**Vulnerability:** A DOM-based XSS vulnerability was discovered in the gallery view because user input encoded with encodeURIComponent was injected into a single-quoted onclick HTML attribute via innerHTML.
**Learning:** encodeURIComponent does not escape single quotes. User inputs can still break out of single-quoted attributes to execute arbitrary JavaScript, even after URL encoding.
**Prevention:** Use safe DOM APIs like document.createElement and directly assign properties instead of concatenating untrusted strings into innerHTML.