## 2024-09-24 - DOM XSS in Image Gallery History
**Vulnerability:** DOM-based Cross-Site Scripting (XSS) in `index.html` via `loadHistory()`.
**Learning:** Using `innerHTML` with string interpolation for URLs (`<img src="${item.url}" ...>`) from `localStorage` allows execution of arbitrary JavaScript if the URL contains quotes and malicious payloads (e.g., `x'); alert(1); //`).
**Prevention:** Prefer using safe DOM manipulation APIs (e.g., `document.createElement`, `img.src = ...`, and `img.onclick = ...`) over `innerHTML` assignments when handling untrusted or stored data.