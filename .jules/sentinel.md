## 2024-06-22 - Fix XSS in loadHistory
**Vulnerability:** A Cross-Site Scripting (XSS) vulnerability existed in `loadHistory` where user-controlled input (`item.url`) was passed into `innerHTML` to dynamically generate HTML for the gallery grid.
**Learning:** Even when interpolating variables into template literals, if the data eventually lands in `innerHTML` without robust escaping, XSS is highly likely, especially when single quotes aren't escaped or when URLs are used in attributes.
**Prevention:** Avoid `innerHTML` for dynamically creating elements with user input. Instead, use standard DOM methods like `document.createElement` and assign data to element properties like `.src` or `.onclick`.
