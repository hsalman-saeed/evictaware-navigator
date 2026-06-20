"""
Gemini API client for EvictAware.
Primary AI layer — Layer 1 of the three-layer fallback.
Uses google-genai SDK (the current, supported Gemini SDK).
"""
import time
from config.settings import get_api_key

# Gemini models to try in order
GEMINI_MODELS = [
    "gemini-2.0-flash",
    "gemini-1.5-flash",
]

_client = None


def _get_client():
    """
    Lazily initialise and return the google.genai Client.
    Returns None if no valid API key is available.
    """
    global _client
    if _client is not None:
        return _client
    api_key = get_api_key("GEMINI_API_KEY")
    if not api_key or api_key.startswith("replace_"):
        return None
    try:
        from google import genai
        _client = genai.Client(api_key=api_key)
        return _client
    except Exception:
        return None


def configure_gemini() -> bool:
    """
    Configure the Gemini client with the API key.
    Returns True if successful, False if no key available.
    """
    return _get_client() is not None


def call_gemini(
    system_instruction: str,
    contents: list,
    generation_config: dict,
    max_retries: int = 1,
) -> tuple:
    """
    Call the Gemini API.
    Returns (response_text: str, source: str).
    Returns (None, None) on failure — caller should try Layer 2 (Groq).
    """
    client = _get_client()
    if client is None:
        return None, None

    from google.genai import types

    # Convert contents list to google-genai format
    genai_contents = []
    for msg in contents:
        role = msg.get("role", "user")
        parts = msg.get("parts", [])
        text = " ".join(
            p.get("text", "") for p in parts if isinstance(p, dict)
        )
        if text:
            genai_contents.append(
                types.Content(
                    role=role,
                    parts=[types.Part(text=text)],
                )
            )

    gen_config = types.GenerateContentConfig(
        system_instruction=system_instruction,
        temperature=generation_config.get("temperature", 0.2),
        max_output_tokens=generation_config.get("max_output_tokens", 2048),
    )

    for model_name in GEMINI_MODELS:
        for attempt in range(max_retries + 1):
            try:
                response = client.models.generate_content(
                    model=model_name,
                    contents=genai_contents,
                    config=gen_config,
                )

                if response and response.text:
                    return response.text, f"gemini:{model_name}"

            except Exception as e:
                if attempt < max_retries:
                    time.sleep(1)
                continue

        # If this model failed all retries, try next model

    return None, None
