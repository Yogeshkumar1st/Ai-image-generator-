## 2024-05-30 - Prevent XSS in dynamic HTML attributes
**Vulnerability:** User-controlled input (URLs) containing single quotes injected into HTML `onclick` attributes via string interpolation (`innerHTML`) allowed arbitrary JavaScript execution (XSS).
**Learning:** Directly injecting unescaped variables into inline event handlers (like `onclick='...'`) within `innerHTML` is dangerous.
**Prevention:** Always use safe DOM manipulation methods like `document.createElement()`, setting properties, and attaching event listeners instead of constructing HTML strings with user input.