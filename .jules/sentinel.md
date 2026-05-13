## 2024-05-24 - [DOM XSS via encodeURIComponent]
**Vulnerability:** [DOM XSS caused by single-quoted string interpolation after encodeURIComponent]
**Learning:** [encodeURIComponent does not escape single quotes, leading to XSS when inserted into single-quoted HTML attributes]
**Prevention:** [Always use DOM APIs like document.createElement instead of innerHTML for creating dynamic elements based on user input]
