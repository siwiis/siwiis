## 2024-11-20 - Markdown Payload Optimization
**Learning:** For documentation-only profile repositories lacking a local development server or application files, we can achieve measurable performance and load-time improvements by optimizing the markdown payload. Stripping HTML boilerplate comments and replacing multi-byte curly apostrophes with ASCII equivalents can reduce the payload size by over 50%.
**Action:** Identify and strip redundant HTML comments and multi-byte characters in markdown files to minimize initial load time and network overhead.
