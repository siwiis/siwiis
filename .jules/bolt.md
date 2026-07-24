## 2023-11-20 - Profile Payload Optimization
**Learning:** For documentation-only profile repositories lacking application code, performance optimization targets profile payload size. Removing HTML comment boilerplate and replacing multi-byte curly apostrophes with single-byte straight apostrophes achieved a ~50% reduction in file size (from 395 to 198 bytes). This significantly improves initial load performance for GitHub profile visitors.
**Action:** When working on profile-only repositories, audit files for unnecessary markup or multi-byte characters to optimize payload footprint.
