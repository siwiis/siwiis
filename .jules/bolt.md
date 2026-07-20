## 2023-11-20 - Profile README Payload Size Optimization
**Learning:** Removing heavy HTML boilerplates (such as multi-line comment blocks) and replacing multi-byte characters (like curly apostrophes ’) with ASCII-equivalent single-byte characters (') can reduce markdown payload size by up to 50% (~395 bytes to 198 bytes). This directly improves initial load times for users visiting GitHub profiles.
**Action:** Always check profile and documentation READMEs for boilerplate comments and non-essential multi-byte symbols to minimize initial network payload.
