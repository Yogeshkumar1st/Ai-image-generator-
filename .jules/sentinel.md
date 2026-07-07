## 2024-05-24 - [Fix DOM XSS in Gallery History]
**Vulnerability:** DOM XSS via unescaped single quotes in URLs loaded into `innerHTML` using string interpolation in the `loadHistory` function.
**Learning:** `encodeURIComponent` does not escape single quotes, making HTML string interpolation with single quotes vulnerable even when input is technically URL encoded.
**Prevention:** Use DOM native APIs (`document.createElement`, direct property assignments like `img.src`) instead of `innerHTML` and string interpolation when handling dynamic user data.
