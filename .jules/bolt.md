## 2025-01-24 - Profile Payload Optimization
**Learning:** Stripping redundant HTML boilerplate comments and replacing multi-byte curly apostrophes with standard single-byte apostrophes reduces the payload size of the profile readme from 395 bytes to 198 bytes, achieving a ~50% savings to improve initial load performance for profile visitors.
**Action:** Always identify and strip unused HTML boilerplate comments and multi-byte curly characters in profile README files for lightweight loading.
