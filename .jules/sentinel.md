## 2024-08-13 - Stored XSS via innerHTML and DOM Clobbering
**Vulnerability:** A stored XSS vulnerability existed in `index.html` where user input from `localStorage` (`item.url`) was injected directly into the DOM using `div.innerHTML = \`<img src="${item.url}" onclick="viewImage('${item.url}')">\`;`.
**Learning:** Even if the input is URL encoded, JavaScript's `encodeURIComponent()` does not escape single quotes (`'`). This allows an attacker to break out of single-quoted HTML attributes like `onclick='...'` or inject new attributes when injecting via `innerHTML`.
**Prevention:** Always use safe DOM manipulation methods like `document.createElement()` and assign properties (e.g., `img.src = value`) rather than using `innerHTML` with unsanitized user input.
