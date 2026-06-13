## 2024-06-13 - XSS via Unescaped Single Quotes in encodeURIComponent
**Vulnerability:** Cross-Site Scripting (XSS) in `index.html` where user-provided prompts were used in a URL, escaped with `encodeURIComponent`, and then rendered via `innerHTML` into an `onclick` attribute.
**Learning:** `encodeURIComponent` does NOT escape single quotes (`'`). When interpolating URLs into HTML attributes enclosed in single quotes (like `onclick="viewImage('URL')"`), an attacker can inject a single quote to break out of the string and execute arbitrary JavaScript.
**Prevention:** Avoid using `innerHTML` to interpolate dynamic URLs. Instead, create elements using `document.createElement` and assign properties directly (e.g., `img.src = url; img.onclick = () => viewImage(url);`).
