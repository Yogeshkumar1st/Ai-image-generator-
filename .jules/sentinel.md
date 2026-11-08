## 2024-05-18 - XSS via encodeURIComponent bypassing single quotes
**Vulnerability:** DOM-based XSS when user input encoded with encodeURIComponent is injected into single-quoted HTML attributes using innerHTML.
**Learning:** encodeURIComponent does not escape single quotes ('), allowing attackers to break out of single-quoted attributes like onclick='...'.
**Prevention:** Avoid innerHTML with dynamic attributes. Use safe DOM manipulation APIs like document.createElement, setAttribute, or direct property assignment.
