import os
import cv2
import torch
import numpy as np

# ----------------------------
# Paths
# ----------------------------
IMAGE_DIR = "processed_frames"
DEPTH_DIR = "depth_maps"

os.makedirs(DEPTH_DIR, exist_ok=True)

# ----------------------------
# Load MiDaS model (CPU only)
# ----------------------------
model_type = "MiDaS_small"  # Fastest & safest for CPU
midas = torch.hub.load("intel-isl/MiDaS", model_type, trust_repo=True)
midas.eval()

# ----------------------------
# Load transforms
# ----------------------------
transforms = torch.hub.load("intel-isl/MiDaS", "transforms", trust_repo=True)
transform = transforms.small_transform

# ----------------------------
# Process images
# ----------------------------
for filename in sorted(os.listdir(IMAGE_DIR)):
    if filename.lower().endswith(".jpg"):
        img_path = os.path.join(IMAGE_DIR, filename)

        # Read image
        img = cv2.imread(img_path)
        if img is None:
            print(f"Skipping unreadable file: {filename}")
            continue

        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # IMPORTANT FIX:
        # small_transform ALREADY adds batch dimension
        input_batch = transform(img)   # ✅ NO unsqueeze()

        # Depth prediction
        with torch.no_grad():
            depth = midas(input_batch)

        # Convert to numpy
        depth = depth.squeeze().cpu().numpy()

        # Normalize depth for visualization
        depth_normalized = cv2.normalize(
            depth, None, 0, 255, cv2.NORM_MINMAX
        ).astype(np.uint8)

        # Save depth map
        depth_filename = filename.replace(".jpg", "_depth.png")
        depth_path = os.path.join(DEPTH_DIR, depth_filename)
        cv2.imwrite(depth_path, depth_normalized)

        print(f"Saved depth map: {depth_path}")

print("✅ Depth estimation completed successfully.")