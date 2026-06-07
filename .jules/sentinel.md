## 2024-06-07 - XSS in Local Storage History
**Vulnerability:** XSS vulnerability in local storage history rendering via innerHTML
**Learning:** Even internal app state like localStorage can contain malicious payloads if user input is reflected without sanitization. Dynamically building HTML strings with innerHTML and embedding URLs containing single quotes can break out of attributes and execute arbitrary code.
**Prevention:** Always use document.createElement and direct property assignment (like img.src) when rendering user-controlled data to the DOM, rather than string concatenation with innerHTML.
