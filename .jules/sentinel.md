## 2024-05-24 - [Fix XSS in loadHistory]
**Vulnerability:** XSS vulnerability in loadHistory due to using innerHTML with unescaped single quotes from encodeURIComponent.
**Learning:** encodeURIComponent does not escape single quotes, making innerHTML interpolation vulnerable when attribute values are enclosed in single quotes.
**Prevention:** Always use document.createElement and direct property assignment instead of innerHTML for dynamic content.
