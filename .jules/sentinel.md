## 2024-05-30 - Prevent DOM-based XSS in Gallery
**Vulnerability:** A DOM-based XSS existed because an image URL containing single quotes could break out of an `onclick` attribute inside a template string assigned to `innerHTML`.
**Learning:** `encodeURIComponent()` does not escape single quotes, which can still lead to XSS if the value is injected directly into single-quoted HTML attributes via `innerHTML`.
**Prevention:** Always use safe DOM APIs (e.g., `document.createElement`, direct property assignment like `element.onclick`) when dealing with user-controlled data instead of `innerHTML` assignments.
