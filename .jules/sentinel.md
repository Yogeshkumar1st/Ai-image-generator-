## 2024-07-28 - DOM-based XSS in Gallery View
**Vulnerability:** XSS vulnerability through `innerHTML` assignment when rendering image gallery history. The URL from localStorage was injected into the `src` and `onclick` attributes without sanitization, allowing arbitrary JS execution via unescaped quotes in the URL.
**Learning:** Even URLs stored from previous generations must be treated as untrusted input. `innerHTML` is inherently dangerous when constructing elements containing user-controlled or dynamically generated data.
**Prevention:** Avoid `innerHTML` for dynamic content. Create elements using `document.createElement()`, and set attributes using properties like `img.src` and direct event listeners like `img.onclick` which automatically handle escaping.
