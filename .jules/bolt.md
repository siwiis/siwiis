## 2024-06-07 - [Micro-optimization of Static Profile Content]
**Learning:** For high-traffic static files like a GitHub Profile README, every byte counts. Template comments and multi-byte characters (like curly apostrophes) add unnecessary weight. Renaming to standard filenames (README.md) also avoids potential backend lookup overhead or fallback logic.
**Action:** Always strip template boilerplates and optimize character encoding in static documentation to minimize transfer size.
