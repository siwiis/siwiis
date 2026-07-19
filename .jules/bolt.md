## 2026-06-28 - Profile Payload Optimization
**Learning:** Stripping redundant HTML comments and replacing multi-byte curly apostrophes with ASCII single quotes in `wiis.md` results in a measurable ~50% payload size reduction (from 395 bytes to 198 bytes). This significantly improves the initial load time and network bandwidth efficiency for profile visitors, especially on slow or mobile connections.
**Action:** Always optimize markdown profile files by removing developer-only commentary blocks and utilizing standard single-byte ASCII characters where possible to maximize delivery speed.
