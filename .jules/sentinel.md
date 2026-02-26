## 2025-02-18 - [CRITICAL] DOM XSS in History Loading
**Vulnerability:** The application was using `innerHTML` to render image elements from `localStorage` history. An attacker could inject malicious JavaScript into `localStorage` (key: `xhistory`), which would execute when the user viewed the gallery.
**Learning:** `localStorage` is not a trusted data source. Even if data seems to originate from the app, it can be manipulated. `innerHTML` should be avoided for rendering any dynamic content.
**Prevention:** Always use DOM API methods like `document.createElement`, `setAttribute`, or property assignment (e.g., `img.src = ...`) instead of constructing HTML strings. This prevents the browser from parsing malicious strings as executable code.
