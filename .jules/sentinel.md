## 2024-05-15 - Prevent DOM-based XSS in gallery history rendering
**Vulnerability:** DOM-based XSS when rendering user's image history by directly setting `innerHTML` with string concatenation. `encodeURIComponent` does not escape single quotes (`'`), so an attacker-controlled URL can break out of the `onclick='...'` attribute.
**Learning:** JavaScript's `encodeURIComponent` is not sufficient to prevent XSS in single-quoted HTML attributes. Using `innerHTML` with dynamic user content (like URLs stored in `localStorage`) is highly risky.
**Prevention:** Use safe DOM manipulation APIs like `document.createElement`, direct property assignment (`img.src = item.url`), and event listeners (`img.onclick = () => viewImage(item.url)`) instead of `innerHTML` assignments.
