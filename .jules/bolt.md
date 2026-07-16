## 2025-05-14 - Payload optimization in Markdown-only profile repository
**Learning:** Stripping boilerplate HTML comments and replacing multi-byte punctuation (like curly apostrophes) in profile READMEs can reduce payload size by ~50% (from 395 to 198 bytes in this case) without affecting visual fidelity for visitors.
**Action:** Always check for redundant HTML comments and non-ASCII characters in documentation-focused repositories to optimize initial load times.
