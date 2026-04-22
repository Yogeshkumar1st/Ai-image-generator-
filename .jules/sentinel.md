## 2024-05-18 - [CRITICAL] Fix XSS Vulnerability in Gallery Tab

**Vulnerability:** Cross-Site Scripting (XSS) in `index.html` via the gallery view. User input (the image URL generated from the Pollinations API) was stored in `localStorage` and later embedded directly into an inline HTML event handler using `innerHTML` (`div.innerHTML = \`<img src="${item.url}" onclick="viewImage('${item.url}')">\``).

**Learning:** `encodeURIComponent()` (which was used on the user's prompt before querying the Pollinations API, making it part of the URL) does NOT encode single quotes (`'`). This allowed an attacker to inject single quotes into the URL, break out of the `viewImage('...')` argument string, and execute arbitrary JavaScript.

**Prevention:** Never use `innerHTML` or string interpolation to create DOM elements with user-controlled data, especially inside inline event handlers like `onclick`. Always use the DOM API (`document.createElement`, `element.setAttribute`, `element.addEventListener`) to ensure data is treated as data, not executable code.
