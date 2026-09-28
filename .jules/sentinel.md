## 2024-05-15 - DOM-based XSS in Gallery
**Vulnerability:** A DOM-based Cross-Site Scripting (XSS) vulnerability was found in the gallery loading logic due to string interpolation of URLs into the `innerHTML` of the gallery grid.
**Learning:** `encodeURIComponent()` does not escape single quotes (`'`). As a result, user inputs embedded within single-quoted HTML attributes (e.g., `onclick='...'`) can still break out of the attribute and execute arbitrary JavaScript.
**Prevention:** Prefer using safe DOM manipulation APIs (e.g., `document.createElement`, direct property assignment) over `innerHTML` assignments when dealing with user-controlled data or URLs.
