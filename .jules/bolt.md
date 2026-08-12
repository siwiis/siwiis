# Bolt's Performance Journal

## 2025-02-15 - Profile payload optimization
**Learning:** For documentation-only/profile repositories where the entry point is the main user interface, payload size optimization is a direct and impactful performance enhancement. Redundant multi-line HTML comments (which serve as instructions for repository creation) and multi-byte curly apostrophes are common sources of extra bytes. Stripping these reduces the document payload significantly.
**Action:** Identify and strip HTML boilerplate comments and replace multi-byte curly apostrophes in profile Markdown files to reduce delivery payload by ~50% (from 395 bytes to 198 bytes), speeding up initial profile load times for visitors.
