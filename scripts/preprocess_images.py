import os
import cv2

# Paths
INPUT_DIR = "inputs/images"
OUTPUT_DIR = "processed_frames"

# Create output folder if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Target size (CPU friendly)
TARGET_SIZE = (512, 512)

# Process images
for idx, filename in enumerate(sorted(os.listdir(INPUT_DIR))):
    if filename.lower().endswith((".jpg", ".png", ".jpeg")):
        img_path = os.path.join(INPUT_DIR, filename)
        img = cv2.imread(img_path)

        if img is None:
            print(f"Skipping unreadable file: {filename}")
            continue

        resized = cv2.resize(img, TARGET_SIZE)

        out_name = f"frame_{idx+1:03d}.jpg"
        out_path = os.path.join(OUTPUT_DIR, out_name)

        cv2.imwrite(out_path, resized)
        print(f"Saved: {out_path}")

print("✅ Image preprocessing completed.")