## 2025-06-16 - Image to 3D pipeline optimization
**Learning:** Optimizing the image-to-mesh pipeline (specifically mask-only processing, early contour filtering, and vertex reduction via approxPolyDP) achieved a measurable ~16% execution time reduction (from ~1.82s to ~1.52s for high-resolution images).
**Action:** Always filter contours by area early using cv2.contourArea before performing expensive geometric operations. Simplify geometry as early as possible to reduce downstream computation.
