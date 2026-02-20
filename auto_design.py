import json
import os
import glob

SUMMARY_DIR = "summaries" 
OUTPUT_FILE = "auto_prompts.json"

def generate_prompt(summary_data):
    """Generates a text prompt based on room characteristics."""
    brightness = summary_data.get("brightness_level", "Medium")
    size = summary_data.get("room_size", "Medium")
    room_type = summary_data.get("room_type", "Unknown")
    objects = summary_data.get("objects_detected", [])

    unique_objects = list(set(objects))
    if not unique_objects:
        objects_str = "standard furniture"
    elif len(unique_objects) == 1:
        objects_str = f"a {unique_objects[0]}"
    else:
        objects_str = f"{', '.join(unique_objects[:-1])} and {unique_objects[-1]}"

    style = "contemporary interior design"
    if brightness == "Bright" and size == "Large":
        style = "Modern " + "luxury"
    elif brightness == "Dark" and size == "Small":
        style = "Warm " + "minimalist"
    elif size == "Small" or brightness == "Dark":
        style = "Warm " + "minimalist" 
    else:
        style = "Contemporary Scandinavian"

    atmosphere = "balanced and functional"
    if room_type == "Bedroom":
        atmosphere = "Calm, " + "restful, serene"
    elif room_type == "Living Room":
        atmosphere = "Social, " + "comfortable, inviting"

    prompt = f"{brightness.lower()} {size.lower()} {room_type.lower()} with {objects_str} in {style.lower()} style, {atmosphere.lower()} atmosphere, professional interior design, 8k resolution, highly detailed"
    
    return prompt

def main():
    if not os.path.exists(SUMMARY_DIR):
        print(f"Error: Directory '{SUMMARY_DIR}' not found. Please ensure Member 4's data is present.")
        return

    all_prompts = {}
    
    summary_files = glob.glob(os.path.join(SUMMARY_DIR, "*_summary.json"))
    
    if not summary_files:
        print(f"No summary files found in {SUMMARY_DIR}.")
        return

    for file_path in summary_files:
        try:
            with open(file_path, 'r') as f:
                summary_data = json.load(f)
            
            frame_name = summary_data.get("frame")
            if not frame_name:
                continue
                
            generated_prompt = generate_prompt(summary_data)
            all_prompts[frame_name] = generated_prompt
            
            print(f"Processed {frame_name} -> Prompt generated.")
            
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

    with open(OUTPUT_FILE, 'w') as f:
        json.dump(all_prompts, f, indent=4)
        
    print(f"\nSuccess! All prompts exported to {OUTPUT_FILE}")
    print("This file is ready for Member 8's image generation module.")

if __name__ == "__main__":
    main()