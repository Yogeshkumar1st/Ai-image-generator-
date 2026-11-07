## 2024-11-07 - Safe DOM Manipulation
**Vulnerability:** DOM-based XSS via `innerHTML` assignment using user-controlled data (`item.url`) from `localStorage`.
**Learning:** Even data loaded from `localStorage` can be dangerous if it originated from external sources or user input and is directly injected into the DOM via `innerHTML`.
**Prevention:** Use safe DOM manipulation APIs like `document.createElement`, `textContent`, and direct property assignment (e.g., `img.src = ...`, `img.onclick = ...`) instead of `innerHTML`.