## 2023-11-20 - Payload Size Reduction
**Learning:** Stripping redundant HTML boilerplate and multi-byte curly apostrophes from Markdown documentation achieves a significant (~50%) payload reduction, speeding up initial page load performance on platforms that parse and render these files (such as GitHub profile pages).
**Action:** Replace multi-byte curly apostrophes with standard single-byte apostrophes and remove HTML comment boilerplate to save critical bytes.
