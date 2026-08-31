## 2024-05-24 - DOM XSS via encodeURIComponent and innerHTML
**Vulnerability:** User-controlled input in `encodeURIComponent` was embedded into an `onclick` attribute via `innerHTML`. Since `encodeURIComponent` does not escape single quotes (`'`), users could break out of the single-quoted attribute string and execute arbitrary JavaScript.
**Learning:** Using `innerHTML` for DOM construction is risky when integrating user input, even if URL-encoded, due to unescaped characters like single quotes breaking context.
**Prevention:** Prefer safe DOM manipulation APIs like `document.createElement` and direct property assignments (e.g., `element.onclick = ...; element.src = ...`) instead of raw string interpolation with `innerHTML`.
