## 2025-01-20 - README Payload Optimization
**Learning:** In a documentation-only profile repository, payload size is the primary performance bottleneck. Stripping HTML comments and multi-byte characters like curly apostrophes can reduce file size by ~50%, improving page load speed.
**Action:** Use ASCII apostrophes and strip redundant boilerplate comments in profile files to minimize byte size.
