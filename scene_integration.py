import os
import cv2
import json
import shutil
import numpy as np

FRAMES_DIR = "processed_frames"
DEPTH_DIR = "depth_maps"
MASKS_DIR = "masks"
DETECTION_FILE = "detections.json"
SCENE_DIR = "scene_packages"
SUMMARY_DIR = "summaries"

os.makedirs(SCENE_DIR, exist_ok=True)
os.makedirs(SUMMARY_DIR, exist_ok=True)

def calculate_brightness(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    brightness = np.mean(gray)

    if brightness < 80:
        level = "Dark"
    elif brightness < 150:
        level = "Medium"
    else:
        level = "Bright"

    return brightness, level

def estimate_room_size(depth):
    avg_depth = np.mean(depth)

    if avg_depth < 85:
        size = "Small"
    elif avg_depth < 170:
        size = "Medium"
    else:
        size = "Large"

    return avg_depth, size

def analyze_objects(detection_data):
    object_count = len(detection_data)
    classes = [obj["class"] for obj in detection_data]
    return object_count, classes

def identify_room_type(classes):
    if "bed" in classes:
        return "Bedroom"
    elif "sofa" in classes or "couch" in classes:
        return "Living Room"
    elif "table" in classes and "chair" in classes:
        return "Dining Room"
    else:
        return "Unknown"

def process_frame(frame_filename, detections):
    frame_name = os.path.splitext(frame_filename)[0]

    image_path = os.path.join(FRAMES_DIR, frame_filename)
    depth_path = os.path.join(DEPTH_DIR, frame_name + "_depth.png")

    if not os.path.exists(depth_path):
        print(f"Skipping {frame_name} (No depth map found)")
        return

    image = cv2.imread(image_path)
    depth = cv2.imread(depth_path, cv2.IMREAD_GRAYSCALE)

    height, width = image.shape[:2]
    depth = cv2.resize(depth, (width, height))

    detection_data = detections.get(frame_filename, [])

    brightness_value, brightness_level = calculate_brightness(image)
    avg_depth, room_size = estimate_room_size(depth)
    object_count, classes = analyze_objects(detection_data)
    room_type = identify_room_type(classes)

    frame_scene_dir = os.path.join(SCENE_DIR, frame_name)
    os.makedirs(frame_scene_dir, exist_ok=True)

    shutil.copy(image_path, os.path.join(frame_scene_dir, "original.jpg"))
    cv2.imwrite(os.path.join(frame_scene_dir, "depth.png"), depth)

    for mask_file in os.listdir(MASKS_DIR):
        if frame_name in mask_file:
            mask_path = os.path.join(MASKS_DIR, mask_file)
            mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)
            mask = cv2.resize(mask, (width, height))
            cv2.imwrite(os.path.join(frame_scene_dir, mask_file), mask)

    with open(os.path.join(frame_scene_dir, "detections.json"), "w") as f:
        json.dump(detection_data, f, indent=4)

    summary = {
        "frame": frame_name,
        "brightness_value": float(brightness_value),
        "brightness_level": brightness_level,
        "average_depth": float(avg_depth),
        "room_size": room_size,
        "object_count": object_count,
        "objects_detected": classes,
        "room_type": room_type
    }

    with open(os.path.join(SUMMARY_DIR, frame_name + "_summary.json"), "w") as f:
        json.dump(summary, f, indent=4)

    print(f"Processed {frame_name} successfully.")

def main():
    with open(DETECTION_FILE, "r") as f:
        detections = json.load(f)

    frames = [f for f in os.listdir(FRAMES_DIR) if f.endswith(".jpg")]

    for frame in frames:
        process_frame(frame, detections)

    print("\nAll frames processed successfully.")

if __name__ == "__main__":
    main()
