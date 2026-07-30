## 2024-05-15 - Prevent DOM XSS in Gallery History
**Vulnerability:** XSS vulnerability found in `loadHistory()` where user-controlled URLs from localStorage were unsafely injected into the DOM via string interpolation in `innerHTML`.
**Learning:** Interpolating unvalidated data directly into `innerHTML` allows arbitrary HTML execution, even if the source is localStorage (which could be poisoned by other means).
**Prevention:** Always use secure DOM manipulation methods like `document.createElement` and set properties (e.g., `img.src`, `img.onclick`) rather than generating HTML strings.