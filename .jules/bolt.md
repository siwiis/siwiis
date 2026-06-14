# Bolt's Journal - Critical Learnings

## 2024-06-14 - Optimized Image-to-FBX Pipeline
**Learning:** Returning large intermediate arrays like BGRA images when only the alpha mask is needed incurs unnecessary memory allocation and copy overhead. Early contour filtering with `cv2.contourArea` and geometry simplification with `cv2.approxPolyDP` significantly reduces both CPU time in mesh generation and the final file size.
**Action:** Always minimize intermediate data structures and simplify geometry as early as possible in 3D processing pipelines.
