## 2023-10-27 - Markdown Profile Payload Optimization
**Learning:** For documentation-only profile repositories, the README/Markdown serves as the entire frontend payload. Redundant HTML boilerplate comments and multi-byte curly apostrophes add unnecessary bytes. Stripping them out reduces the payload from 395 to 198 bytes (~50% savings), directly improving load performance for profile visitors.
**Action:** Always inspect raw Markdown files for boilerplate HTML comments and convert multi-byte curly quotes to standard characters to optimize static profile delivery.
