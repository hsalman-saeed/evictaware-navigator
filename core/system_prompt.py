"""
Loads the master system prompt from ai_config.json.
NEVER stores the prompt as a hardcoded Python string.
The prompt is read from the JSON file at startup.
"""


def get_master_system_prompt(config_data: dict) -> str:
    """
    Return the master system prompt from ai_config.json.
    This is Component 1 of the Core AI Prompt System.
    Read from JSON — never hardcoded here.
    """
    prompt = config_data.get("system_prompt_base", "")
    if not prompt:
        raise ValueError(
            "system_prompt_base is missing from ai_config.json. "
            "Cannot start the AI system."
        )
    return prompt


def get_stage3_output_instruction(config_data: dict) -> str:
    """
    Return the Stage 3 JSON output format instruction.
    Appended to the system prompt for Stage 3 calls only.
    Read from JSON if available, otherwise use the standard instruction.
    """
    return config_data.get(
        "stage3_output_instruction",
        (
            "You must respond with ONLY valid JSON matching the "
            "EvictAware action plan schema. Do not include markdown "
            "code fences, preamble, explanation, or any text outside "
            "the JSON object. The first character of your response "
            "must be '{' and the last must be '}'."
        ),
    )
