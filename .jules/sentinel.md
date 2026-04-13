## 2024-04-13 - encodeURIComponent XSS
**Vulnerability:** XSS via unescaped single quotes in encodeURIComponent output when interpolated into single-quoted HTML attributes.
**Learning:** Standard JS encodeURIComponent does not encode single quotes (').
**Prevention:** Use DOM API methods instead of innerHTML for rendering.
