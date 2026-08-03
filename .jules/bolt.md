## 2023-11-23 - Markdown Payload Optimization
**Learning:** Stripping redundant HTML comments and multi-byte curly apostrophes from documentation-only markdown files reduces payload size by ~50% (from 395 to 198 bytes), directly improving the initial page load performance of the profile.
**Action:** Always identify and strip unused HTML boilerplates and convert multi-byte characters to single-byte equivalents in static documentation files.
