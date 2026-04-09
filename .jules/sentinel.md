
## 2024-05-24 - [HIGH] XSS via unescaped single quotes in encodeURIComponent
**Vulnerability:** A DOM-based XSS vulnerability existed in the gallery view because `encodeURIComponent` does not encode single quotes ('). This allowed an attacker to break out of single-quoted HTML attributes (`onclick="viewImage('...')`) when rendering user history from localStorage using string interpolation (`innerHTML`).
**Learning:** Standard JavaScript `encodeURIComponent` does not escape single quotes. Interpolating user-controlled data into single-quoted event handlers via `innerHTML` is inherently unsafe, even if partially encoded.
**Prevention:** Always rely on DOM API methods (e.g., `document.createElement`, `setAttribute`, `element.onclick`) rather than `innerHTML` to construct elements with user-generated content, as they handle escaping automatically and securely.
