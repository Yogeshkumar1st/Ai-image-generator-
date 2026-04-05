## 2025-04-05 - encodeURIComponent single-quote vulnerability
**Vulnerability:** XSS via `encodeURIComponent` single-quote interpolation in HTML attributes.
**Learning:** `encodeURIComponent` does NOT escape single quotes (`'`). When rendering URLs built with this function into single-quoted HTML attributes using `innerHTML` (e.g., `innerHTML = "<img src='...' onclick='viewImage(\\'" + url + "\\')'>" `), a user can break out of the attribute using a single quote in their input, leading to XSS.
**Prevention:** Avoid interpolating user-controlled data into HTML strings via `innerHTML`. Always use safe DOM API methods (`document.createElement`, `element.setAttribute`, `element.src`, `element.onclick`) where the browser naturally handles context-aware escaping.
