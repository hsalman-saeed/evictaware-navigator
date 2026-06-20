"""
Loads and validates all runtime JSON data files.
Cached with st.cache_data so files load once per session.
All legal content, contacts, and configuration come from here.
Nothing is hardcoded in app logic.
"""
import json
import streamlit as st
from pathlib import Path
from config.settings import DATA_DIR


@st.cache_data
def load_all_data() -> dict:
    """
    Load all 5 runtime JSON files.
    Returns a dict with keys: eviction_data, legal_aid,
    prohibitions, config, demo_cache.
    Raises RuntimeError with clear message if any file fails.
    """
    files = {
        "eviction_data": "california_eviction_data.json",
        "legal_aid": "legal_aid_contacts.json",
        "prohibitions": "landlord_prohibitions.json",
        "config": "ai_config.json",
        "demo_cache": "demo_cache_priya_nt001.json",
    }

    data = {}
    for key, filename in files.items():
        filepath = DATA_DIR / filename
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                if key == "demo_cache":
                    # demo_cache file has markdown wrapper — extract JSON
                    raw = f.read()
                    data[key] = _extract_json_from_cache(raw)
                else:
                    data[key] = json.load(f)
        except FileNotFoundError:
            st.error(
                f"Required data file not found: {filename}. "
                f"Please ensure all files are in the data/ folder."
            )
            st.stop()
        except json.JSONDecodeError as e:
            st.error(
                f"Data file {filename} contains invalid JSON: {e}. "
                f"Please check the file and try again."
            )
            st.stop()

    # Validate required keys exist
    _validate_data_structure(data)
    return data


def _extract_json_from_cache(raw_text: str) -> dict:
    """
    Extract JSON from the demo cache file, which may have
    a markdown wrapper (```json ... ```).
    """
    import re
    # Try to find JSON block in markdown code fence
    match = re.search(r'```json\s*\n(.*?)\n\s*```', raw_text, re.DOTALL)
    if match:
        return json.loads(match.group(1))
    # If no code fence, try parsing the whole text as JSON
    try:
        return json.loads(raw_text)
    except json.JSONDecodeError:
        # Return a minimal valid structure
        return {"error": "Could not parse demo cache"}


def _validate_data_structure(data: dict) -> None:
    """Validate that all required fields are present in loaded data."""
    required = {
        "eviction_data": ["notice_types", "metadata"],
        "legal_aid": ["county_contacts", "statewide_resources", "default_fallback"],
        "prohibitions": ["prohibitions"],
        "config": [
            "system_prompt_base",
            "prohibited_output_phrases",
            "mandatory_disclaimer_text",
            "hard_stop_config",
            "required_uncertainty_templates",
        ],
    }
    for key, fields in required.items():
        if key not in data:
            continue
        for field in fields:
            if field not in data[key]:
                st.error(
                    f"Missing required field '{field}' in {key} data. "
                    f"Please check your data files."
                )
                st.stop()


def get_data_freshness_date(data: dict) -> str:
    """
    Returns the last verified date from JSON metadata.
    NEVER hardcode a date. Always read from JSON.
    """
    return data["eviction_data"].get("metadata", {}).get(
        "last_verified_date", "date unknown"
    )


def get_notice_type_by_id(data: dict, notice_id: str) -> dict:
    """Return notice type dict for a given ID (e.g. 'NT001')."""
    for notice in data["eviction_data"]["notice_types"]:
        if notice.get("id") == notice_id:
            return notice
    return {}


def get_all_notice_types(data: dict) -> list:
    """Return list of all notice types from the eviction data."""
    return data["eviction_data"].get("notice_types", [])


def get_county_legal_aid(data: dict, county_name: str) -> dict:
    """
    Return legal aid contact for a specific county.
    Falls back to default_fallback if county not found.
    No hardcoded county logic — pure JSON lookup.
    """
    if not county_name:
        return data["legal_aid"].get("default_fallback", {})

    county_key = (
        county_name.lower()
        .replace(" county", "")
        .replace("county", "")
        .strip()
        .replace(" ", "_")
    )
    contacts = data["legal_aid"].get("county_contacts", {})

    # Try exact match first
    if county_key in contacts and contacts[county_key]:
        return contacts[county_key]

    # Try to find a key that contains the county name
    for key, contact in contacts.items():
        if county_key in key or key in county_key:
            if contact:
                return contact

    return data["legal_aid"].get("default_fallback", {})


def get_all_prohibitions(data: dict) -> list:
    """Return all landlord prohibitions from JSON."""
    return data["prohibitions"].get("prohibitions", [])


def get_mandatory_disclaimer(data: dict) -> str:
    """Return the mandatory disclaimer text from ai_config.json."""
    return data["config"].get("mandatory_disclaimer_text", "")


def get_hard_stop_message(data: dict, stop_type: str) -> str:
    """Return a hard stop message by type key from ai_config.json."""
    hard_stops = data["config"].get("hard_stop_config", {})
    stop_data = hard_stops.get(stop_type, {})
    if isinstance(stop_data, dict):
        return stop_data.get(
            "message",
            "This tool is unable to help with your current request. "
            "Please call 211 for assistance.",
        )
    return str(stop_data)


def get_all_county_names(data: dict) -> list:
    """Return sorted list of county names for the dropdown."""
    counties = data["legal_aid"].get("county_contacts", {})
    names = []
    for key in counties.keys():
        # Convert key format to display name
        display = key.replace("_", " ").title()
        names.append(display)
    return sorted(names)
