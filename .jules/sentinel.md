## 2024-05-15 - [XSS via localStorage History]
**Vulnerability:** DOM-based XSS vulnerability in `loadHistory()` caused by injecting `item.url` unsafely into `div.innerHTML`. The `item.url` comes from `localStorage`, which could be manipulated (e.g. `a')-alert('XSS`).
**Learning:** Using `innerHTML` with string interpolation that contains user-controlled input, even partially trusted ones like local storage data, can lead to XSS. Single quotes within `innerHTML` attributes are not automatically escaped by `encodeURIComponent`.
**Prevention:** Avoid `innerHTML` for DOM construction when dealing with user or external data. Use `document.createElement()` and assign values directly to node properties (e.g., `img.src` and `img.onclick`).
