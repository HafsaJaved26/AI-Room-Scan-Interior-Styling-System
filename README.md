
# Module 4 – Scene Integration & Understanding
Member: Ghazal Hafeez

## Overview
This module integrates outputs from:
- Member 1: Processed images and depth maps
- Member 2: Object detection JSON
- Member 3: Segmentation masks

It aligns all data and generates structured scene packages and analytical summaries
to support the styling modules (Module 5, 6, and 7).

---

## Folder Structure Required

AI_Room_Project/
│
├── processed_frames/
├── depth_maps/
├── masks/
├── detections.json
├── scene_packages/
├── summaries/
├── scene_integration.py

---

## Functional Workflow

1. Align depth maps with original images
2. Resize masks to match frame dimensions
3. Read detection data for each frame
4. Calculate brightness using grayscale mean
5. Estimate room size using average depth
6. Count detected objects
7. Identify room type using rule-based logic
8. Create structured scene package per frame
9. Save analysis summary as JSON

---

## Output Structure

scene_packages/frame_xxx/
    original.jpg
    depth.png
    masks...
    detections.json

summaries/
    frame_xxx_summary.json

---

## Room Analysis Logic

Brightness Classification:
- Dark (<80)
- Medium (80–150)
- Bright (>150)

Room Size Estimation (based on average depth):
- Small
- Medium
- Large

Room Type Identification:
- Bed → Bedroom
- Sofa/Couch → Living Room
- Table + Chair → Dining Room

---

## How To Run

Install dependencies:
    pip install opencv-python numpy

Run the module:
    python scene_integration.py

---
This module ensures proper scene understanding before AI-based redesign.
