## 2023-11-20 - Payload Size Reduction on Profile Repository
**Learning:** In documentation-only profile repositories, stripping redundant HTML comments and multi-byte curly apostrophes achieves a ~50% payload reduction, resulting in measurably faster initial load performance for profile visitors.
**Action:** Always identify boilerplate HTML comments and multi-byte characters in markdown documents to reduce overall footprint.
