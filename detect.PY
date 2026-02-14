# detect.py - Super Simple Version
import os
import json
from ultralytics import YOLO

print("🚀 Starting object detection...")
print(f"📂 Current folder: {os.getcwd()}")

# Step 1: Images dhundho
images = []
for file in os.listdir('.'):
    if file.endswith('.jpg') or file.endswith('.png'):
        images.append(file)

print(f"\n📸 Found {len(images)} images:")
for img in images:
    print(f"   - {img}")

if len(images) == 0:
    print("\n❌ Koi image nahi mili!")
    exit()

# Step 2: Model load karo
print("\n📦 Loading YOLOv8 model... (pehli baar download hoga)")
model = YOLO('yolov8n.pt')
print("✅ Model loaded!")

# Step 3: Detection karo
all_results = {}

for img_name in images:
    print(f"\n🔍 Processing: {img_name}")
    
    # Run detection
    results = model(img_name)
    
    detections = []
    
    # Parse results
    for r in results:
        for box in r.boxes:
            class_id = int(box.cls[0])
            class_name = model.names[class_id]
            confidence = float(box.conf[0])
            
            # Bounding box coordinates
            x1, y1, x2, y2 = box.xyxy[0].tolist()
            bbox = [int(x1), int(y1), int(x2-x1), int(y2-y1)]
            
            detections.append({
                'class': class_name,
                'bbox': bbox,
                'confidence': round(confidence, 3)
            })
            
            print(f"   ✅ {class_name} ({confidence:.2f})")
    
    all_results[img_name] = detections

# Step 4: JSON save karo
with open('detections.json', 'w') as f:
    json.dump(all_results, f, indent=2)

print("\n" + "="*40)
print("✅ DONE! JSON file created:")
print("   detections.json")
print("="*40)

# Summary
total = 0
for img, dets in all_results.items():
    total += len(dets)
print(f"\n📊 Total objects detected: {total}")