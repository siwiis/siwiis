import cv2
import numpy as np
import trimesh
import os
import sys
from shapely.geometry import Polygon, MultiPolygon
from shapely.ops import unary_union

# Set environment variable for Aspose.3D to avoid ICU dependency issues
os.environ["DOTNET_SYSTEM_GLOBALIZATION_INVARIANT"] = "1"
from aspose.threed import Scene

def process_image(input_path, threshold=5):
    """Removes background and returns a binary mask."""
    img = cv2.imread(input_path)
    if img is None:
        raise ValueError(f"Could not load image from {input_path}")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)

    kernel = np.ones((3,3), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    return mask

def generate_mesh(mask, thickness=10.0):
    """Generates an extruded 3D mesh from a binary mask."""
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    polygons = []
    for cnt in contours:
        # Early filtering of small shapes
        if cv2.contourArea(cnt) < 10:
            continue

        # Simplify contour to reduce vertex count and improve performance
        epsilon = 0.002 * cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, epsilon, True)

        if len(approx) < 3:
            continue

        pts = approx.reshape(-1, 2)
        poly = Polygon(pts)
        if poly.is_valid:
            polygons.append(poly)

    if not polygons:
        raise ValueError("No valid contours found in image")

    merged = unary_union(polygons)

    if isinstance(merged, Polygon):
        mesh = trimesh.creation.extrude_polygon(merged, height=thickness)
    elif isinstance(merged, MultiPolygon):
        meshes = [trimesh.creation.extrude_polygon(poly, height=thickness) for poly in merged.geoms]
        mesh = trimesh.util.concatenate(meshes)
    else:
        raise ValueError("Failed to create geometry")

    mesh.apply_translation(-mesh.centroid)
    return mesh

def convert_image_to_fbx(input_path, output_fbx, thickness=10.0):
    """Full pipeline to convert an image to an FBX 3D model."""
    print(f"Processing {input_path}...")
    mask = process_image(input_path)

    print("Generating 3D mesh...")
    mesh = generate_mesh(mask, thickness)

    temp_obj = "temp_mesh.obj"
    mesh.export(temp_obj)

    print(f"Converting to {output_fbx}...")
    scene = Scene.from_file(temp_obj)
    scene.save(output_fbx)

    if os.path.exists(temp_obj):
        os.remove(temp_obj)

    print(f"Done! Created {output_fbx}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python image_to_fbx.py <input_image> <output_fbx> [thickness]")
    else:
        input_img = sys.argv[1]
        output_file = sys.argv[2]
        thick = float(sys.argv[3]) if len(sys.argv) > 3 else 10.0
        convert_image_to_fbx(input_img, output_file, thick)
