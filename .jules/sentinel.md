## 2025-02-18 - XSS in Local Storage
**Vulnerability:** Found a DOM XSS vulnerability in `loadHistory` where user-controlled data from `localStorage` was interpolated into `innerHTML`.
**Learning:** Even "trusted" local storage can be a vector if it's manipulated or if the application assumes data integrity without validation.
**Prevention:** Always use `document.createElement` and set properties directly instead of building HTML strings with `innerHTML`, especially for dynamic content.
