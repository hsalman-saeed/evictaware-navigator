"""
Seven-layer API fallback for EvictAware.

Layer order:
  1–4: OpenRouter (4 keys rotating) → Gemini 2.5 Flash
    5: Google Gemini direct API
    6: Groq (Llama 3.3 70B Versatile)
    7: Demo cache (with date update for cache_fallback)

Demo Mode bypasses all APIs and serves the pre-computed cache.
"""
import json
import re
from pathlib import Path
from config.settings import DATA_DIR, get_openrouter_api_keys
from ai.openrouter_client import call_openrouter
from ai.gemini_client import call_gemini
from ai.groq_client import call_groq
from ai.cache_date_updater import update_cache_dates


def load_demo_cache() -> dict:
    """
    Load the pre-computed Priya NT001 demo cache.
    This is the Layer 7 guarantee — always returns data.
    Serves the JSON exactly as written — no date rewriting for Demo Mode.
    """
    cache_file = DATA_DIR / "demo_cache_priya_nt001.json"
    try:
        with open(cache_file, "r", encoding="utf-8") as f:
            raw = f.read()

        # Extract JSON from markdown code fence if present
        match = re.search(r"```json\s*\n(.*?)\n\s*```", raw, re.DOTALL)
        if match:
            return json.loads(match.group(1))

        # Try parsing the whole text
        return json.loads(raw)
    except Exception:
        # Absolute minimum fallback if even the cache file fails
        return _emergency_fallback()


def call_ai_with_fallback(
    system_instruction: str,
    contents: list,
    generation_config: dict,
    stage: str = "",
    demo_mode: bool = False,
) -> tuple:
    """
    Seven-layer AI fallback.
    Returns (response_text, source) — guaranteed to return something.

    If demo_mode is True AND stage is action_plan:
        → serve demo cache as-is (judges know it's demo).
    Otherwise:
        → L1-4: OpenRouter keys → L5: Gemini → L6: Groq → L7: cache
    """
    # Demo Mode: serve cache directly without date update
    if demo_mode and "action_plan" in stage.lower():
        cache = load_demo_cache()
        return json.dumps(cache, ensure_ascii=False), "demo_cache"

    # Layer 1–4: OpenRouter (4 keys, auto-rotation)
    or_keys = get_openrouter_api_keys()
    if or_keys:
        response_text, source = call_openrouter(
            system_instruction, contents, generation_config, or_keys
        )
        if response_text:
            return response_text, source

    # Layer 5: Google Gemini direct
    response_text, source = call_gemini(
        system_instruction, contents, generation_config
    )
    if response_text:
        return response_text, source

    # Layer 6: Groq
    response_text, source = call_groq(
        system_instruction, contents, generation_config
    )
    if response_text:
        return response_text, source

    # Layer 7: Demo cache with date update (emergency fallback)
    cache = load_demo_cache()
    cache = update_cache_dates(cache)
    return json.dumps(cache, ensure_ascii=False), "cache_fallback"


def get_api_error_message(config_data: dict) -> str:
    """
    Return the hard stop message for API errors from ai_config.json.
    """
    hard_stops = config_data.get("hard_stop_config", {})
    api_stop = hard_stops.get("hard_stop_3_api_error", {})
    if isinstance(api_stop, dict):
        return api_stop.get(
            "message",
            "Something went wrong. Please call 211 for immediate help.",
        )
    return str(api_stop)


def _emergency_fallback() -> dict:
    """
    Hardcoded last-resort response if the cache file itself is corrupted.
    This is the ONLY place where response text exists in code,
    and it only fires if the JSON file is unreadable.
    """
    return {
        "bold_statement_card": {
            "text": (
                "This notice is NOT an order to leave. Only a judge "
                "can order your removal from your home."
            ),
            "legal_basis": (
                "California law requires a full court process before "
                "any tenant can be removed."
            ),
        },
        "notice_summary": {
            "notice_type": "3-Day Notice to Pay Rent or Quit",
            "what_it_means": (
                "Your landlord says you owe rent. You have a short "
                "window to pay or respond. This is not a court order."
            ),
            "does_tenant_have_to_leave_now": False,
            "critical_deadline": {
                "label": "Contact legal aid immediately",
                "date": "As soon as possible",
                "days_remaining": 0,
            },
        },
        "action_tiers": {
            "tier_1": {
                "label": "NEXT 24 HOURS",
                "color": "red",
                "urgency_reason": "Time-sensitive steps to protect your rights.",
                "actions": [
                    {
                        "deadline": "Today:",
                        "action": "Call 211 for free legal help in your county.",
                        "why_it_matters": "Legal aid can review your specific notice.",
                        "how_to_do_it": "Dial 211 from any phone — free, 24/7.",
                    }
                ],
            },
            "tier_2": {
                "label": "BEFORE YOUR NOTICE EXPIRES",
                "color": "orange",
                "urgency_reason": "Prepare for next steps if the deadline passes.",
                "actions": [
                    {
                        "deadline": "Before the deadline on your notice:",
                        "action": "Gather your notice and any messages from your landlord.",
                        "why_it_matters": "These documents help legal aid advise you.",
                        "how_to_do_it": "Keep everything in one safe place.",
                    }
                ],
            },
            "tier_3": {
                "label": "IF COURT PAPERS ARE FILED",
                "color": "yellow",
                "urgency_reason": "Steps if a court case begins.",
                "actions": [
                    {
                        "deadline": "If you receive court papers:",
                        "action": "Contact legal aid immediately about your response deadline.",
                        "why_it_matters": "Missing the response deadline MAY result in an automatic ruling.",
                        "how_to_do_it": "Bring the court papers to legal aid or call 211.",
                    }
                ],
            },
        },
        "landlord_cannot_do": {
            "module_title": "What Your Landlord CANNOT Do Right Now",
            "items": [
                {
                    "action": "Remove you without a court order",
                    "plain_language": (
                        "Only a judge and sheriff can remove you — "
                        "your landlord cannot do this alone."
                    ),
                    "legal_basis": "California Code of Civil Procedure Section 715.010",
                    "if_this_happens": "Call the police non-emergency line and legal aid.",
                }
            ],
            "most_relevant_to_user_situation": (
                "Your landlord must go through court to remove you."
            ),
        },
        "legal_aid_connector": {
            "intro_text": "Free legal help is available in your county.",
            "organization_name": "Call 211 for your local legal aid",
            "phone_number": "211",
            "hours": "24 hours a day, 7 days a week",
            "intake_link": "https://www.lawhelp.org/ca",
            "languages": ["English", "Spanish"],
            "what_to_say_when_you_call": (
                "Say: 'I received an eviction notice and need "
                "tenant rights legal help.'"
            ),
        },
        "rental_assistance": {
            "applicable": False,
            "resources": [],
            "important_note": "Ask legal aid about emergency rental assistance in your area.",
        },
        "disclaimer": (
            "EvictAware provides legal information only — not legal advice. "
            "This does not guarantee any outcome. Laws change; this may not "
            "reflect the most current California law. Always confirm your "
            "rights with a licensed attorney or legal aid organization "
            "before taking action. Call 211 or visit lawhelp.org/ca to "
            "find free legal help in your county."
        ),
        "stage": "action_plan",
        "notice_type_id": "NT001",
    }
