## 2024-06-14 - Fix DOM XSS in Image Gallery
**Vulnerability:** DOM-based XSS vulnerability found in `loadHistory` due to interpolating URLs directly into `innerHTML` strings. The `encodeURIComponent` function used earlier does not escape single quotes (`'`), allowing an attacker to break out of the `onclick` attribute by injecting a payload like `'-alert(1)-'`.
**Learning:** Using `innerHTML` with dynamically injected values is dangerous even if partially encoded. Single quotes (`'`) remain unencoded by standard URI encoding functions.
**Prevention:** Avoid `innerHTML` for dynamic content rendering. Use safe DOM manipulation methods such as `document.createElement()` and direct attribute assignment (e.g., `img.src` and `img.onclick`).
