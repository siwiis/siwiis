## 2024-08-01 - README Payload Size Optimization
**Learning:** In a documentation-only profile repository, stripping redundant HTML boilerplate comments and replacing multi-byte curly apostrophes with standard single-byte straight apostrophes achieves a ~50% payload size reduction (from 395 to 198 bytes). This directly improves initial load performance for GitHub profile visitors.
**Action:** Always optimize static markdown payloads in documentation-only profiles by removing unnecessary HTML boilerplate comments and using standard ascii/single-byte alternatives where possible to save bytes.
