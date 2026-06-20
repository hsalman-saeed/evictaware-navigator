"""
Builds the dynamic context injection block for each API call.
Implements Component 2 from EvictAware_Core_AI_Prompt_System.md.
All content injected here comes from JSON files — nothing hardcoded.
"""
import json
from datetime import date
from typing import Optional


def build_context_injection(
    notice_type_data: dict,
    county_legal_aid: dict,
    landlord_prohibitions: list,
    current_stage: str,
    user_county: str,
    confirmed_notice_type: Optional[str] = None,
    all_notice_types: Optional[list] = None,
) -> str:
    """
    Build the context block injected into every API call.
    Stage-appropriate: Stage 1 is lightweight, Stage 3 is full.
    """
    if current_stage == "STAGE_1_IDENTIFY":
        return _build_stage1_context(all_notice_types or [])

    elif current_stage == "STAGE_2_CONFIRM":
        return _build_stage2_context(notice_type_data)

    elif current_stage == "STAGE_3_ACTION_PLAN":
        return _build_stage3_context(
            notice_type_data,
            county_legal_aid,
            landlord_prohibitions,
            user_county,
        )

    return ""


def _build_stage1_context(all_notice_types: list) -> str:
    """Stage 1: Only trigger phrases and identification signals."""
    lines = ["=== NOTICE TYPE IDENTIFICATION REFERENCE ==="]
    for notice in all_notice_types:
        lines.append(f"\nNotice ID: {notice.get('id')}")
        lines.append(f"Legal Name: {notice.get('legal_name')}")
        lines.append(f"Plain Name: {notice.get('plain_language_name')}")
        signals = notice.get("ai_identification_signals", [])
        if signals:
            lines.append(f"Identification signals: {', '.join(signals[:8])}")
        phrases = notice.get("common_trigger_phrases", [])
        if phrases:
            lines.append(f"Trigger phrases: {', '.join(phrases[:8])}")
    return "\n".join(lines)


def _build_stage2_context(notice_type_data: dict) -> str:
    """Stage 2: Candidate notice type details for confirmation."""
    if not notice_type_data:
        return "=== NO NOTICE TYPE DATA AVAILABLE ==="
    lines = [
        "=== CANDIDATE NOTICE TYPE FOR CONFIRMATION ===",
        f"ID: {notice_type_data.get('id')}",
        f"Legal name: {notice_type_data.get('legal_name')}",
        f"Plain language name: {notice_type_data.get('plain_language_name')}",
        f"What it means: {notice_type_data.get('what_it_means_plain_language')}",
        f"Payment option exists: {notice_type_data.get('payment_option_exists')}",
        f"Urgency level: {notice_type_data.get('urgency_level')}",
    ]
    return "\n".join(lines)


def _build_stage3_context(
    notice_type_data: dict,
    county_legal_aid: dict,
    landlord_prohibitions: list,
    user_county: str,
) -> str:
    """Stage 3: Full context including notice data, prohibitions, legal aid."""
    today = date.today().strftime("%A, %B %d, %Y")

    lines = [
        "=== STAGE 3 FULL CONTEXT ===",
        f"CURRENT DATE FOR ALL CALCULATIONS: {today}",
        f"User county: {user_county or 'Not specified'}",
        "",
        "=== NOTICE TYPE DATA ===",
        json.dumps(notice_type_data, indent=2),
        "",
        "=== LANDLORD PROHIBITIONS (all apply) ===",
    ]

    for prob in landlord_prohibitions[:7]:
        lines.append(
            f"- {prob.get('prohibited_action')}: "
            f"{prob.get('plain_language_explanation', '')[:200]}"
        )

    lines += [
        "",
        "=== COUNTY LEGAL AID CONTACT ===",
        json.dumps(county_legal_aid, indent=2),
    ]

    return "\n".join(lines)
