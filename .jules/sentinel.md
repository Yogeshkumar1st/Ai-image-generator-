## 2024-08-16 - Prevent DOM-based XSS with document.createElement

**Vulnerability:** A DOM-based XSS vulnerability existed in the gallery history generation where user-controlled URLs (from localStorage) were injected directly into HTML attributes using string interpolation (`innerHTML = \`<img src="\${item.url}" onclick="viewImage('\${item.url}')">\``). An attacker could break out of the single quotes in the `onclick` attribute to execute arbitrary JavaScript (e.g., `test');alert(1);//`).
**Learning:** `encodeURIComponent` does not encode single quotes (`'`). As a result, when user input (even if partially URL-encoded) is placed inside single-quoted HTML attributes, it can still break out and lead to XSS. String interpolation for HTML attributes is extremely risky.
**Prevention:** Prefer safe DOM manipulation APIs (like `document.createElement()`, `element.src = ...`, `element.onclick = ...`) over `innerHTML` assignments when building UI elements with user-controlled data.
