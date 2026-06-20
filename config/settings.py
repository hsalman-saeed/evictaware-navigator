"""
EvictAware configuration — loads environment variables and constants.
All API keys come from .env (local) or st.secrets (Streamlit Cloud).
Nothing is hardcoded here.
"""
import os
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st

# Resolve paths
ROOT_DIR = Path(__file__).parent.parent
DATA_DIR = ROOT_DIR / "data"
ENV_FILE = ROOT_DIR / ".env"

# Load .env for local development
load_dotenv(ENV_FILE)


def get_api_key(key_name: str) -> str:
    """
    Retrieve an API key.
    Order: Streamlit secrets (cloud) → .env file (local) → empty string.
    Never hardcode keys in this function.
    """
    try:
        if hasattr(st, "secrets") and key_name in st.secrets:
            return st.secrets[key_name]
    except Exception:
        pass
    return os.getenv(key_name, "")


def get_openrouter_api_keys() -> list:
    """
    Return all four OpenRouter API keys as a list.
    Order: API1, API2, API3, API4.
    Skips any key that is empty or None.
    """
    key_names = [
        "USAII_Hackathon_API1",
        "USAII_Hackathon_API2",
        "USAII_Hackathon_API3",
        "USAII_Hackathon_API4",
    ]
    keys = []
    for name in key_names:
        val = get_api_key(name)
        if val and val.strip():
            keys.append(val.strip())
    return keys


# OpenRouter constants
OPENROUTER_MODEL = "google/gemini-2.5-flash"
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1/chat/completions"
OPENROUTER_APP_NAME = "EvictAware"
OPENROUTER_APP_URL = "https://evictaware.streamlit.app"

# App constants — never hardcode legal content here
APP_NAME = "EvictAware"
APP_SUBTITLE = "California Tenant Rights Navigator"
CALIFORNIA_ONLY_SCOPE = True
MAX_RECLASSIFICATION_ATTEMPTS = 2
MAX_TIER_ACTIONS = 3
MAX_SENTENCE_WORDS = 25
DEMO_MODE_DEFAULT = False
