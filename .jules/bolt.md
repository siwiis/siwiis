## 2026-06-28 - Profile README Payload Reduction
**Learning:** For static Markdown files like GitHub profile READMEs, payload size can be significantly reduced by stripping unused HTML template comments and using standard 1-byte ASCII characters instead of multi-byte equivalents (like curly apostrophes). This directly improves initial load performance for profile visitors.
**Action:** Always check for boilerplate comments and non-standard characters in profile READMEs to ensure minimal payload and faster rendering.
