## 2023-10-25 - XSS via encodeURIComponent in HTML Attributes
**Vulnerability:** User input sanitized via encodeURIComponent was injected into an onclick attribute inside single quotes. encodeURIComponent does not escape single quotes, allowing breakout and XSS execution.
**Learning:** encodeURIComponent is insufficient for preventing XSS in single-quoted context attributes.
**Prevention:** Use safe DOM assignment properties (e.g., element.src, element.onclick) instead of string interpolation for innerHTML.
