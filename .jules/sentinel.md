## 2024-07-26 - DOM XSS via InnerHTML
**Vulnerability:** DOM XSS was possible due to unescaped variables injected into `innerHTML`.
**Learning:** Using template literals to inject user-controlled data into `innerHTML` allows attribute breakout and script execution.
**Prevention:** Use `document.createElement()` and assign values directly to element properties like `.src` and `.onclick` to ensure safe encoding by the browser.
