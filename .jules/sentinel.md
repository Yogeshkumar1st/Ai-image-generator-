## 2024-07-13 - [DOM XSS]
**Vulnerability:** A DOM XSS vulnerability was found when adding images dynamically from `localStorage` where `innerHTML` interpolation was used with an attacker-controlled `item.url` input within an `onclick` attribute.
**Learning:** URL parameters or history items retrieved from `localStorage` may contain unsanitized characters like single quotes, which can break out of inline HTML attributes and execute malicious scripts.
**Prevention:** Avoid `innerHTML` combined with string interpolation for elements containing untrusted URLs. Instead, construct elements dynamically using safe DOM APIs like `document.createElement` and assign event listeners directly using `img.onclick`.
