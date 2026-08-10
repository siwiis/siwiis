## 2025-01-20 - Profile README Payload Size Optimization
**Learning:** For documentation-only profile repositories, payload size is a critical performance metric impacting initial load time. Removing redundant HTML comments and multi-byte curly apostrophes achieves a ~50% payload reduction (from 395 to 198 bytes).
**Action:** Use Python script or regular expressions to strip multi-line HTML comments (`re.sub(r'\n\n<!--[\s\S]*?-->', '', content)`) and normalize multi-byte characters to minimize network payload.
