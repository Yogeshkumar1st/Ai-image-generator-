## 2024-05-24 - encodeURIComponent does not encode single quotes
**Vulnerability:** XSS via URL injected into single-quoted HTML attributes.
**Learning:** standard JavaScript encodeURIComponent does not encode single quotes ('), creating XSS vectors if these unescaped components are interpolated into single-quoted HTML attributes using innerHTML.
**Prevention:** Always rely on DOM API methods (e.g., document.createElement, setAttribute, appendChild) instead of innerHTML for rendering user-generated content.
