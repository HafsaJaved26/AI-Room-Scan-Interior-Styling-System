"""Module 3 - Member 6
Prompt-Based Implementation
Eman Afzal
"""
# USER INPUT FUNCTION

def get_user_prompt():
    """Get prompt from user."""
    return input("Enter your interior design style prompt: ").strip()

# VALIDATION FUNCTION

def validate_prompt(prompt):
    """Validate user input prompt."""
    if not prompt:
        raise ValueError("Prompt cannot be empty.")

    if len(prompt.split()) < 3:
        raise ValueError("Prompt too short. Please provide a more descriptive style.")

    return prompt

# PROMPT ENHANCEMENT FUNCTION

def enhance_prompt(prompt):
    """
    Enhance prompt by:
    - Adding interior design context
    - Adding quality keywords
    - Keeping original user intent
    """

    # Add interior context if missing
    if "interior" not in prompt.lower():
        prompt = "interior design of a room, " + prompt

    # Quality keywords for better diffusion output
    quality_keywords = (
        ", professional photography, 4k resolution, "
        "highly detailed, realistic lighting, sharp focus"
    )

    return prompt + quality_keywords



# MAIN PROCESS FUNCTION


def process_prompt(user_prompt=None):
    """
    Full pipeline for Prompt-Based Mode.
    Can accept external prompt for integration.
    """

    try:
        # Allow integration from main.py
        if user_prompt is None:
            user_prompt = get_user_prompt()

        validated = validate_prompt(user_prompt)
        final_prompt = enhance_prompt(validated)

        return final_prompt

    except ValueError as e:
        print(f"Error: {e}")
        return None


# ----------------------------
# TESTING BLOCK
# ----------------------------

if __name__ == "__main__":
    result = process_prompt()

    if result:
        print("\nFinal Prompt Sent To Image Generator:\n")
        print(result)
