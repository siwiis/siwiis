## 2026-06-19 - Optimizing Image-to-Mesh Pipeline

**Learning:** Large vertex counts in generated meshes significantly slow down FBX export when using libraries like Aspose.3D. Simplification at the contour level (before mesh generation) is much more efficient than simplifying the resulting 3D mesh. Returning only the necessary binary mask from image processing instead of a full BGRA image saves memory and avoids redundant color space conversions.

**Action:** Use `cv2.approxPolyDP` to simplify contours based on arc length. Use `cv2.contourArea` for early filtering of insignificant shapes. Pass binary masks directly to mesh generation functions.
