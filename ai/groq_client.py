"""
Groq API client for EvictAware.
Backup AI layer — Layer 2 of the three-layer fallback.
Uses Groq SDK with Llama 3.3 70B Versatile.
Only called when Gemini (Layer 1) fails.
"""
import time
from config.settings import get_api_key

GROQ_MODEL = "llama-3.3-70b-versatile"

_groq_client = None


def get_groq_client():
    """Initialize and return the Groq client."""
    global _groq_client
    if _groq_client is None:
        api_key = get_api_key("GROQ_API_KEY")
        if not api_key or api_key.startswith("replace_"):
            return None
        try:
            from groq import Groq
            _groq_client = Groq(api_key=api_key)
        except Exception:
            return None
    return _groq_client


def call_groq(
    system_instruction: str,
    contents: list,
    generation_config: dict,
    max_retries: int = 1,
) -> tuple:
    """
    Call the Groq API with Llama 3.3 70B.
    Returns (response_text: str, source: str).
    Returns (None, None) on failure — caller should use Layer 3 (cache).
    """
    client = get_groq_client()
    if not client:
        return None, None

    # Convert Gemini contents format to OpenAI-compatible messages
    messages = [{"role": "system", "content": system_instruction}]
    for content in contents:
        role = content.get("role", "user")
        parts = content.get("parts", [])
        text = " ".join(
            p.get("text", "") for p in parts if isinstance(p, dict)
        )
        if text:
            # Groq uses "assistant" not "model"
            groq_role = "assistant" if role == "model" else role
            messages.append({"role": groq_role, "content": text})

    for attempt in range(max_retries + 1):
        try:
            response = client.chat.completions.create(
                model=GROQ_MODEL,
                messages=messages,
                temperature=generation_config.get("temperature", 0.2),
                max_tokens=generation_config.get("max_output_tokens", 2048),
            )

            text = response.choices[0].message.content
            if text:
                return text, f"groq:{GROQ_MODEL}"

        except Exception as e:
            if attempt < max_retries:
                time.sleep(1)

    return None, None
