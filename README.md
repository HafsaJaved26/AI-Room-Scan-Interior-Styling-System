# Module 3 – Prompt-Based Mode  
### Member 6 – Eman Afzal

## 📌 Overview

This module implements **Prompt-Based Mode** for the Interior Design AI system.

Its purpose is to:

- Accept a user-provided interior design style prompt
- Validate the input
- Enhance the prompt with context and quality keywords
- Return a structured prompt ready for image generation models (e.g., Stable Diffusion)

This module does **not generate images directly**.  
It prepares optimized prompts for the image generation pipeline.

---

## 🏗️ Module Structure

The implementation consists of the following functions:

### 1️⃣ `get_user_prompt()`
- Takes input from the user.
- Removes unnecessary whitespace.

### 2️⃣ `validate_prompt(prompt)`
- Ensures prompt is not empty.
- Ensures prompt has at least 3 words.
- Raises `ValueError` if validation fails.

### 3️⃣ `enhance_prompt(prompt)`
Enhances the user prompt by:
- Adding interior design context (if missing)
- Appending high-quality diffusion keywords:
  - professional photography
  - 4k resolution
  - highly detailed
  - realistic lighting
  - sharp focus

### 4️⃣ `process_prompt(user_prompt=None)`
Full processing pipeline:
- Accepts external prompt (for integration with main system)
- If no external prompt is given, requests user input
- Validates prompt
- Enhances prompt
- Returns final optimized prompt

---

## 🔄 How It Works

### Input Example:
modern luxury bedroom with warm tones

### Output Example:

---

## 🧪 Running the Module Independently

To test this module individually:

on terminal:
python prompt_mode.py