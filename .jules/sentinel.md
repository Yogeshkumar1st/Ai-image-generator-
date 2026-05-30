## 2024-05-30 - XSS via encodeURIComponent and single-quoted HTML attributes
**Vulnerability:** XSS vulnerability in `loadHistory` where user-controlled input (`item.url`) was interpolated into a single-quoted HTML attribute (`onclick`) via `innerHTML`.
**Learning:** `encodeURIComponent` does NOT escape single quotes (`'`). This allows an attacker to break out of single-quoted attributes and execute arbitrary JavaScript.
**Prevention:** Always use standard DOM API methods (e.g., `document.createElement`, setting properties directly) instead of `innerHTML` for dynamic content to avoid XSS vectors, or properly sanitize/escape input specifically for HTML attribute contexts.
