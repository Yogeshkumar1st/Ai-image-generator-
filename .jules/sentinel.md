## 2024-11-04 - DOM-based XSS via encodeURIComponent
**Vulnerability:** XSS payload can be injected through `encodeURIComponent` because it leaves single quotes (`'`) unescaped, allowing breakout of single-quoted HTML attributes like `onclick='...'`.
**Learning:** `encodeURIComponent()` does not escape single quotes, which can lead to XSS when the output is placed inside a single-quoted HTML attribute via `innerHTML`.
**Prevention:** Use safe DOM manipulation APIs (e.g., `document.createElement`, direct property assignment like `img.onclick = ...`) over `innerHTML` string interpolation when handling user-influenced data.
