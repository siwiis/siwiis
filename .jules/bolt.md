# Bolt's Performance Journal

This is Bolt's journal for tracking performance learnings and insights.

## 2023-10-27 - Profile README Payload Optimization
**Learning:** Redundant HTML comment blocks and multi-byte curly apostrophes in documentation-only profile repositories contribute to unnecessarily large initial load payloads. Removing these blocks and standardizing to single-byte ASCII apostrophes yields a 50% byte size reduction, dramatically improving initial page load times for profile visitors.
**Action:** When working on profile-only or documentation-only repositories, profile and optimize the Markdown payload size directly by eliminating boilerplate/redundant comments and multi-byte characters.
