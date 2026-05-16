## 2024-05-24 - encodeURIComponent does not escape single quotes
**Vulnerability:** XSS vulnerability found in `loadHistory()` due to `encodeURIComponent` not escaping single quotes (`'`). This allows an attacker to break out of single-quoted HTML attributes like `onclick='viewImage('${item.url}')'`.
**Learning:** Standard JavaScript `encodeURIComponent` does not encode single quotes (`'`). If these unescaped components are interpolated into single-quoted HTML attributes, it creates an XSS vector.
**Prevention:** Always rely on DOM API methods like `document.createElement()`, `.setAttribute()`, and `.appendChild()` instead of `.innerHTML` for rendering user-generated content to prevent XSS.
