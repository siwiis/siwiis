## 2023-11-20 - README Payload Optimization
**Learning:** Stripping HTML comments and replacing multi-byte curly characters with standard single-byte ASCII characters in a profile repository's main markdown file results in a ~50% payload reduction (from 395 to 198 bytes). This reduces the initial load size for profile visitors.
**Action:** Always identify multi-byte characters and redundant boilerplate comments to optimize documentation payloads when no backend/frontend code is present in the main branch.
