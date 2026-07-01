## 2025-07-01 - Optimized profile README payload size
**Learning:** Stripping boilerplate HTML comments and replacing multi-byte characters (like curly apostrophes) can significantly reduce the payload size of static Markdown files (e.g., from 395B to 198B, a ~50% reduction).
**Action:** Always check for redundant comments and non-ASCII characters in documentation-only repositories to improve initial load performance.
