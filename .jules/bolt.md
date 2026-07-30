## 2023-11-20 - Payload Size Optimization of GitHub Profile README
**Learning:** Redundant multi-byte curly apostrophes and multi-line HTML comments can significantly bloat minimal documents. Eliminating them yields ~50% payload size reduction, directly translating into faster initial load performance for visitors.
**Action:** Use regex patterns to safely remove HTML boilerplates and replace curly apostrophes with standard single-byte equivalents in profile README files to maximize byte savings without impacting standard Markdown readability or accessibility.
