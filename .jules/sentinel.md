## 2024-05-27 - InnerHTML Injection in Gallery History
**Vulnerability:** XSS vulnerability via innerHTML when rendering image history items from localStorage in `index.html`. Unsanitized URLs could break out of HTML attributes and execute arbitrary JS when clicked.
**Learning:** Building HTML dynamically via string interpolation and `innerHTML` is inherently unsafe, especially with user-controlled or external data, as it doesn't escape characters like single quotes.
**Prevention:** Always use safe DOM manipulation methods like `document.createElement` and direct property assignment (e.g., `img.src = item.url`, `img.onclick = () => viewImage(item.url)`) instead of `innerHTML`.
