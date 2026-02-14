# visualize.py - Bounding boxes wali images banane ke liye
import cv2
import json
import os

# JSON file load karo
with open('detections.json', 'r') as f:
    detections = json.load(f)

# Output folder for visualized images
os.makedirs('visualized_output', exist_ok=True)

# Har image ke liye
for img_name, objects in detections.items():
    print(f"Processing {img_name}...")
    
    # Original image read karo
    img = cv2.imread(img_name)
    
    if img is None:
        print(f"❌ Cannot read {img_name}")
        continue
    
    # Har object ke liye box draw karo
    for obj in objects:
        class_name = obj['class']
        x, y, w, h = obj['bbox']
        conf = obj['confidence']
        
        # Different colors for different classes
        if class_name == 'bed':
            color = (0, 255, 0)  # Green
        elif class_name == 'couch' or class_name == 'sofa':
            color = (255, 0, 0)  # Blue
        elif class_name == 'chair':
            color = (0, 0, 255)  # Red
        else:
            color = (255, 255, 0)  # Yellow
        
        # Rectangle draw karo
        cv2.rectangle(img, (x, y), (x+w, y+h), color, 2)
        
        # Text draw karo
        text = f"{class_name} {conf:.2f}"
        cv2.putText(img, text, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 
                   0.5, color, 2)
    
    # Save image
    output_path = f"visualized_output/viz_{img_name}"
    cv2.imwrite(output_path, img)
    print(f"✅ Saved: {output_path}")

print("\n🎉 All visualized images saved in 'visualized_output/' folder!")