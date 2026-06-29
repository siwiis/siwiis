## 2026-06-29 - Profile README Payload Optimization
**Learning:** For documentation-only repositories like GitHub profiles, the README payload size directly impacts the initial load performance and Time to Interactive (TTI) for visitors. Stripping invisible boilerplate comments and using standard 1-byte ASCII characters instead of multi-byte equivalents can significantly reduce the payload.
**Action:** Remove redundant HTML comments and replace multi-byte characters in profile READMEs to ensure minimal payload and faster rendering, especially for mobile users.
