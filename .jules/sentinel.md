## 2024-05-15 - Prevent XSS in loadHistory
**Vulnerability:** XSS vulnerability through `innerHTML` interpolation of user-controlled `url` from `localStorage`, where single quotes are not escaped by `encodeURIComponent`.
**Learning:** Standard JavaScript `encodeURIComponent` does not encode single quotes ('). This can create XSS vectors if these unescaped components are interpolated into single-quoted HTML attributes via `innerHTML`.
**Prevention:** Always rely on DOM API methods (`document.createElement`, `setAttribute`, `appendChild`) instead of `innerHTML` for rendering user-generated content to prevent XSS.
