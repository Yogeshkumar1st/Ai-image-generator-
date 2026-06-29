## 2024-05-18 - XSS Vulnerability via innerHTML in Gallery History
**Vulnerability:** XSS vulnerability through `innerHTML` in the gallery history. URL parameters from Pollinations API contain unsanitized user prompts. When single quotes are in the prompt, it breaks out of the HTML attribute `onclick` due to how the `item.url` was constructed in the string literal.
**Learning:** `encodeURIComponent` does not escape single quotes, leaving the code vulnerable to XSS if the value is interpolated into single-quoted HTML attributes using `innerHTML`.
**Prevention:** Always use `document.createElement` and direct property assignment (e.g. `img.src` and `img.onclick`) instead of `innerHTML` when building HTML dynamically in JavaScript, especially when dealing with external inputs.
