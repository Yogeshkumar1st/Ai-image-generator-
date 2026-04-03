## 2024-05-24 - Cross-Site Scripting (XSS) in LocalStorage Rendering

**Vulnerability:** XSS via unescaped URL interpolation when rendering image history from `localStorage` using `innerHTML`. The code took JSON containing URLs and directly injected it into HTML string templates without escaping it (e.g. `div.innerHTML = "<img src='" + item.url + "'>"`). JavaScript's standard `encodeURIComponent` does not encode single quotes ('), meaning quotes could be injected to escape the attribute and add arbitrary event handlers (like `onload='...'`) if an attacker poisoned `localStorage` (or if it were ever synced from a vulnerable server).

**Learning:** When dynamic data is constructed into HTML using `innerHTML`, even seemingly safe functions like `encodeURIComponent` might leave specific characters unescaped (like `'`) that can break out of attributes.

**Prevention:** Never use `innerHTML` to render user-generated content or dynamically fetched data. Always use standard DOM API methods (`document.createElement`, `setAttribute`, `appendChild`) as they safely handle text rendering by design.