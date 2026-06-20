"""
OpenRouter API client for EvictAware.
Layers 1–4 of the seven-layer fallback — rotates through 4 API keys.
Uses standard HTTP requests (no special SDK needed).
"""
import requests
from config.settings import (
    OPENROUTER_MODEL,
    OPENROUTER_BASE_URL,
    OPENROUTER_APP_URL,
    OPENROUTER_APP_NAME,
)


def call_openrouter(
    system_instruction: str,
    contents: list,
    generation_config: dict,
    api_keys: list,
) -> tuple:
    """
    Call the OpenRouter API, rotating through all provided keys.

    Args:
        system_instruction: The system prompt text.
        contents: Gemini-format contents list (role + parts).
        generation_config: Dict with temperature, max_output_tokens, etc.
        api_keys: List of OpenRouter API keys to try in order.

    Returns:
        (response_text, source) on success, (None, None) on total failure.
    """
    if not api_keys:
        return None, None

    # Convert Gemini-format contents to OpenAI-compatible messages
    messages = _convert_to_openai_messages(system_instruction, contents)

    # Build request body
    body = {
        "model": OPENROUTER_MODEL,
        "messages": messages,
        "temperature": generation_config.get("temperature", 0.2),
        "max_tokens": generation_config.get("max_output_tokens", 2048),
    }

    # Add response_format for JSON mode if requested
    mime_type = generation_config.get("response_mime_type", "")
    if mime_type == "application/json":
        body["response_format"] = {"type": "json_object"}

    # Try each key in order
    for idx, api_key in enumerate(api_keys):
        key_num = idx + 1
        try:
            print(f"Trying OpenRouter key {key_num}...")
            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
                "HTTP-Referer": OPENROUTER_APP_URL,
                "X-Title": OPENROUTER_APP_NAME,
            }

            response = requests.post(
                OPENROUTER_BASE_URL,
                headers=headers,
                json=body,
                timeout=20,
            )

            if response.status_code == 200:
                data = response.json()
                text = (
                    data.get("choices", [{}])[0]
                    .get("message", {})
                    .get("content", "")
                )
                if text:
                    print(f"OpenRouter key {key_num} succeeded.")
                    return text, f"openrouter:API{key_num}"

            # Non-200 or empty response — try next key
            print(
                f"OpenRouter key {key_num} failed: "
                f"HTTP {response.status_code}"
            )

        except requests.exceptions.Timeout:
            print(f"OpenRouter key {key_num} timed out.")
        except Exception as e:
            print(f"OpenRouter key {key_num} error: {e}")

    # All keys failed
    print("All OpenRouter keys exhausted.")
    return None, None


def _convert_to_openai_messages(
    system_instruction: str, contents: list
) -> list:
    """
    Convert Gemini-format contents to OpenAI-compatible messages.

    Gemini format:
        [{"role": "user", "parts": [{"text": "..."}]}, ...]

    OpenAI format:
        [{"role": "system", "content": "..."}, {"role": "user", "content": "..."}, ...]
    """
    messages = []

    # System instruction → system message
    if system_instruction:
        messages.append({
            "role": "system",
            "content": system_instruction,
        })

    # Convert each content item
    for item in contents:
        role = item.get("role", "user")
        parts = item.get("parts", [])

        # Extract text from parts
        text_parts = []
        for part in parts:
            if isinstance(part, dict) and "text" in part:
                text_parts.append(part["text"])
            elif isinstance(part, str):
                text_parts.append(part)

        text = " ".join(text_parts)
        if not text:
            continue

        # Map Gemini roles to OpenAI roles
        openai_role = "user"
        if role == "model":
            openai_role = "assistant"
        elif role == "user":
            openai_role = "user"

        messages.append({
            "role": openai_role,
            "content": text,
        })

    return messages
