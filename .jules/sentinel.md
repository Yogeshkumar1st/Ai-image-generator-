## 2024-05-16 - XSS in Image Gallery innerHTML
**Vulnerability:** A Cross-Site Scripting (XSS) vulnerability exists when generating image tags using innerHTML with unescaped URL values from localStorage.
**Learning:** Using innerHTML with interpolated strings, even from local storage (which can be manipulated by an attacker), is inherently unsafe because unescaped single quotes can break out of attributes.
**Prevention:** Always use secure DOM API methods like document.createElement, element.src, element.onclick, and element.appendChild instead of innerHTML for dynamic content.
