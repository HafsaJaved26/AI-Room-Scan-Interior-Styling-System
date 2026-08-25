# AI Room Scan & Interior Styling System

This project automates the process of redesigning room interiors using generative AI. It preserves the original structure of the room while applying modern aesthetic styles like **Scandinavian Minimalist** and **Modern Luxury**.

##  Key Features
- **Structural Integrity:** Uses ControlNet (Depth and Segmentation) to ensure walls and furniture placement stay realistic.
- **High-Quality Rendering:** Optimized Stable Diffusion v1.5 with 40 inference steps for sharp, blur-free outputs.
- **Side-by-Side Presentation:** Automated video generator that shows "Before" (Raw Layout) vs "After" (AI Redesign).

##  Tech Stack
- **AI Model:** Stable Diffusion v1.5
- **Control Models:** lllyasviel/sd-controlnet-depth & lllyasviel/sd-controlnet-seg
- **Programming:** Python 3.9+
- **Libraries:** Diffusers, OpenCV, PyTorch, PIL
- **Scheduler:** UniPCMultistepScheduler

##  Project Structure
- `depth_maps/`: Input structural frames 
- `object_masks/`: Segmented masks for furniture placement
- `redesigned_images/`: Final AI-generated high-resolution images 
- `final_outputs/`: Professional showcase video 
