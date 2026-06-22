## 2026-06-22 - Optimizing Image-to-Mesh Pipeline

**Learning:** In image-to-mesh workflows, large vertex counts significantly slow down FBX export. Simplifying contours with `cv2.approxPolyDP` and early area filtering reduces vertex count by >50% with minimal loss in fidelity. Returning a binary mask instead of BGRA avoids redundant color conversions and reduces memory overhead.

**Action:** Use `cv2.approxPolyDP` for shape simplification and pass binary masks directly to geometry functions. Use `tempfile` for safe intermediate asset conversion.
