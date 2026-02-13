import os
import json
import cv2

DEPTH_DIR = "depth_maps"
OUTPUT_DIR = "geometry_data"
OUTPUT_FILE = "geometry.json"

os.makedirs(OUTPUT_DIR, exist_ok=True)

geometry_info = {}

for file in sorted(os.listdir(DEPTH_DIR)):
    if file.endswith("_depth.png"):
        path = os.path.join(DEPTH_DIR, file)
        depth_img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

        if depth_img is None:
            continue

        h, w = depth_img.shape

        geometry_info[file.replace("_depth.png", "")] = {
            "image_size": {"width": w, "height": h},
            "floor_region": "lower_half",
            "wall_region": "upper_half",
            "depth_description": "brighter = closer, darker = farther"
        }

output_path = os.path.join(OUTPUT_DIR, OUTPUT_FILE)
with open(output_path, "w") as f:
    json.dump(geometry_info, f, indent=4)

print("✅ geometry.json created successfully.")