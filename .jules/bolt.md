## 2026-03-23 - Document payload optimization for profile markdown

**Learning:** In documentation-only profile repositories without backend/frontend application code, stripping unrendered HTML boilerplate comments and replacing multi-byte unicode characters (such as curly apostrophes `’`) with standard ASCII characters (`'`) reduces file payload size by over 50% (from 395 bytes to ~186 bytes), improving initial load performance for profile visitors.
**Action:** Identify redundant HTML comments and multi-byte characters in profile markdown files to maximize network transfer and parsing efficiency.
