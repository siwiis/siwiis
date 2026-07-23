## 2023-10-27 - Markdown Payload Reduction
**Learning:** Stripping redundant HTML boilerplate comments and replacing multi-byte curly apostrophes with single-byte straight apostrophes in profile Markdown files achieves a ~50% payload reduction (from 395 to 198 bytes).
**Action:** Always identify and strip unused HTML comments or multi-byte characters in documentation-only profiles to optimize network payload size and improve initial load times for visitors.
