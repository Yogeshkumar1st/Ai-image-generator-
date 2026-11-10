## 2024-05-24 - encodeURIComponent DOM XSS
**Vulnerability:** DOM-based XSS via `encodeURIComponent` not escaping single quotes (`'`), leading to payload injection into `onclick` attribute in `innerHTML`.
**Learning:** `encodeURIComponent` does not escape single quotes, which can break out of single-quoted HTML attributes.
**Prevention:** Avoid `innerHTML` and use safe DOM manipulation APIs like `document.createElement` and direct property assignments.
