## 2024-05-24 - encodeURIComponent does not encode single quotes
**Vulnerability:** XSS vulnerability in history gallery.
**Learning:** encodeURIComponent does not encode single quotes ('). When building inline event handlers like onclick="viewImage('${item.url}')", single quotes in the URL can break out of the string literal and execute arbitrary JavaScript.
**Prevention:** Avoid innerHTML with string interpolation for URLs in event handlers. Use DOM methods like document.createElement, setAttribute, and addEventListener.
