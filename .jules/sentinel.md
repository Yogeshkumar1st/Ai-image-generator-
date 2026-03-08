## 2024-05-20 - [XSS via unencoded single quotes]
**Vulnerability:** encodeURIComponent does not encode single quotes, leading to XSS when interpolated into single-quoted HTML attributes.
**Learning:** Even URL-encoded data can be dangerous if placed in single-quoted attributes, because encodeURIComponent ignores single quotes.
**Prevention:** Always use DOM API methods like document.createElement, setAttribute, or direct property assignment (e.g. img.src, img.onclick) instead of innerHTML when rendering user-generated content.
