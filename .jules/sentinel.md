## 2024-06-25 - Fix XSS in Image Gallery
**Vulnerability:** DOM-based Cross-Site Scripting (XSS) via `innerHTML` template string interpolation in the `loadHistory` function (`<img src="${item.url}" ...>`).
**Learning:** Using `innerHTML` with unsanitized dynamic data (like URLs from localStorage) is dangerous. Even simple string interpolation allows attackers to break out of attributes and inject malicious scripts.
**Prevention:** Always use `document.createElement` and set properties (like `src` and `onclick`) directly instead of building HTML strings. This forces the browser to treat the input as pure data, preventing execution of injected payloads.
