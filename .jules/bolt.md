## 2026-06-28 - README Payload Optimization
**Learning:** For profile-only repositories, the README payload is the primary performance bottleneck for initial page load. Removing redundant HTML comments and multi-byte characters (like curly apostrophes) can reduce file size by ~50% without affecting visual fidelity.
**Action:** Always inspect documentation-heavy repositories for unnecessary boilerplate and multi-byte characters to minimize payload size and improve TTFB.
