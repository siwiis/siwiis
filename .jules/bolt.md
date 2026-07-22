## 2025-01-20 - Markdown Payload Size Optimization
**Learning:** Redundant HTML boilerplate comments and multi-byte curly apostrophes in GitHub Profile Markdown files (`wiis.md`) add unnecessary overhead. Stripping them reduces the file size by ~50% (from 395 to 198 bytes), directly lowering network payload size and improving initial page load time for profile visitors.
**Action:** Always identify and strip multi-line comments and convert non-ASCII/multi-byte characters to single-byte equivalents to minimize transmission overhead for documentation-only profile repos.
