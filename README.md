# Module 1 – Input & Depth Processing (Faraz Khan)

## Overview
This module handles the initial input processing and depth estimation
for the AI Room Scan & Interior Styling System.

It supports room images as input and generates depth maps using MiDaS
(CPU-only, open-source).

## Input
- 3 room images of the same room from different angles
- Format: JPG / PNG

Location:
inputs/images/

## Processing Steps
1. Images are resized to 512×512 for CPU efficiency
2. Images are saved as sequential frames
3. MiDaS (small model) is used to generate depth maps
4. Simple geometry information (floor/wall regions) is stored

## Folder Structure
inputs/images/
processed_frames/
depth_maps/
geometry_data/
scripts/


## How to Run

### 1. Preprocess Images
```bash
python scripts/preprocess_images.py

2. Generate Depth Maps
python scripts/depth_estimation_midas.py
3. Generate Geometry Data
python scripts/generate_geometry.py
Output

Resized room images

Depth map images (one per frame)

geometry.json with basic room structure info

Notes

CPU-only implementation

Uses free and open-source models

Output is passed to Object Detection & Segmentation modules


---

# 🎉 FINAL STATUS: FARAZ’S TASK = **COMPLETE**

Let’s tick **everything** from the task sheet:

| Requirement | Status |
|------------|--------|
| Input images | ✅ |
| Image preprocessing | ✅ |
| Frame organization | ✅ |
| MiDaS depth maps (CPU) | ✅ |
| Geometry data | ✅ |
| Clean directory structure | ✅ |
| README | ✅ |

✔ **You are DONE**  
✔ **Ready to submit / push / hand off**

---

## 📦 WHAT TO SEND TO YOUR TEAM LEAD / FARAZ

Just say:

> “Module 1 completed.  
> Processed frames, depth maps, geometry.json, and README are ready.”