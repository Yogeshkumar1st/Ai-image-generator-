## 2024-05-24 - [encodeURIComponent single quote bypass]
**Vulnerability:** XSS via `encodeURIComponent` not escaping single quotes (`'`). When user input is encoded with `encodeURIComponent` and then placed into a single-quoted HTML attribute (e.g. `onclick="doSomething('...')"`), an attacker can break out of the string with a single quote and execute arbitrary JS.
**Learning:** Standard JS `encodeURIComponent` DOES NOT encode single quotes. This is a common footgun when trying to safely interpolate data into inline event handlers or other single-quoted attributes.
**Prevention:** Rely entirely on DOM API methods (`document.createElement`, `element.setAttribute`, `element.src`, etc.) instead of interpolating strings via `innerHTML` when handling user-provided data.
