## 2024-06-28 - XSS via innerHTML and History Loading
**Vulnerability:** XSS vulnerability discovered in the loadHistory function due to using innerHTML to interpolate the URL component directly.
**Learning:** Even if URLs seem benign, injecting user-controlled data directly into HTML attributes using string interpolation can lead to XSS, particularly when quotes aren't properly escaped.
**Prevention:** Avoid innerHTML for dynamic content generation. Use document.createElement and direct property assignment (e.g., img.src = url, img.onclick = ...) to safely construct DOM elements.
