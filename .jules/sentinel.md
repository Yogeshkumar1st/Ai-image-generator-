## 2024-05-18 - [XSS Fix in loadHistory via DOM APIs]
**Vulnerability:** XSS in image gallery because URL from localStorage is interpolated into HTML strings via innerHTML and is executed via onclick attribute without proper sanitization.
**Learning:** Using document.createElement and setting properties like src or setting up EventListeners prevents executing unintended scripts because DOM APIs inherently handle string data without executing it.
**Prevention:** Always use DOM manipulation and elements instead of innerHTML when dealing with dynamic and potentially untrusted content such as items stored from external API outputs or local storage.
