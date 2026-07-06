## 2026-07-06 - Image-to-FBX Pipeline Optimization
**Learning:** Returning a binary mask directly instead of a full BGRA image saves memory and avoids redundant conversions. Early contour filtering with `cv2.contourArea` and geometry simplification with `cv2.approxPolyDP` significantly reduces vertex count, which accelerates the subsequent heavy export phase.
**Action:** For computer vision pipelines, filter noise early and simplify geometry before mesh generation to ensure downstream operations remain efficient.
