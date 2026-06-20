"""
Confirmation screen — Confirmation Gate + Acknowledgment Gate.
Implements the mandatory two-gate architecture:
1. Confirmation Gate: user confirms the notice type is correct
2. Acknowledgment Gate: user acknowledges this is info, not advice
The action plan CANNOT render without BOTH gates completed.
"""
import streamlit as st
from ui.components import (
    render_app_header,
    render_data_freshness_banner,
    render_disclaimer,
    render_demo_badge,
    render_source_badge,
)
from data.loader import (
    get_data_freshness_date,
    get_mandatory_disclaimer,
    get_notice_type_by_id,
    get_all_notice_types,
    get_county_legal_aid,
    get_all_prohibitions,
)
from core.system_prompt import get_master_system_prompt
from core.context_injection import build_context_injection
from core.output_validator import EvictAwareOutputValidator
from ai.fallback import call_ai_with_fallback, load_demo_cache


def render_confirmation_screen(data: dict) -> None:
    """
    Render the Confirmation Gate.
    User must confirm the AI's notice type classification before proceeding.
    """
    sm = st.session_state["state_manager"]
    freshness = get_data_freshness_date(data)
    disclaimer = get_mandatory_disclaimer(data)

    render_data_freshness_banner(freshness)

    if st.session_state.get("demo_mode"):
        render_demo_badge()

    render_app_header()

    # Show the AI's confirmation question
    ai_text = st.session_state.get("ai_confirmation_text", "")
    notice_data = get_notice_type_by_id(data, sm.identified_notice_type or "")

    # Build a clean confirmation display
    if notice_data:
        plain_name = notice_data.get("plain_language_name", "")
        legal_name = notice_data.get("legal_name", "")
        explanation = notice_data.get("what_it_means_plain_language", "")

        st.markdown(
            f'<div class="ea-card">'
            f'<p style="font-size:1rem;color:#334155;line-height:1.6;">'
            f"Based on what you described, it sounds like you received:</p>"
            f'<p style="font-size:1.15rem;font-weight:700;color:#0D9488;'
            f'margin:12px 0;">{legal_name}</p>'
            f'<p style="font-size:0.9rem;color:#475569;line-height:1.5;">'
            f"{explanation}</p>"
            f'<p style="font-size:0.95rem;color:#334155;margin-top:16px;'
            f'font-weight:500;">'
            f"Does that match what your notice says?</p>"
            f"</div>",
            unsafe_allow_html=True,
        )
    elif ai_text:
        st.markdown(ai_text)

    render_source_badge(sm.ai_response_source or "")

    # Confirmation buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button(
            "✅ Yes, that's right — show me what to do",
            key="confirm_yes",
            use_container_width=True,
            type="primary",
        ):
            sm.confirmation_gate_completed = True
            sm.confirmed_notice_type = sm.identified_notice_type
            st.session_state["current_screen"] = "acknowledgment"
            st.rerun()

    with col2:
        if st.button(
            "❌ No, it says something different",
            key="confirm_no",
            use_container_width=True,
        ):
            sm.reclassification_attempts += 1
            if sm.reclassification_attempts >= 2:
                st.session_state["current_screen"] = "notice_selection"
            else:
                st.session_state["current_screen"] = "reclassify"
            st.rerun()

    render_disclaimer(disclaimer)


def render_reclassification_screen(data: dict) -> None:
    """
    Ask user for more details after a failed classification.
    Maximum 2 attempts before showing the full notice list.
    """
    sm = st.session_state["state_manager"]
    freshness = get_data_freshness_date(data)
    disclaimer = get_mandatory_disclaimer(data)

    render_data_freshness_banner(freshness)
    render_app_header()

    st.markdown(
        '<div class="ea-card">'
        '<p style="font-size:1rem;color:#334155;line-height:1.6;">'
        "No problem — let me try again. Can you describe what your "
        "notice says in a little more detail?"
        "</p>"
        '<p style="font-size:0.85rem;color:#64748B;font-style:italic;'
        'margin-top:8px;">'
        "For example, does it mention paying rent, fixing something "
        "in the apartment, or just leaving? Any words you can share "
        "from the notice will help."
        "</p>"
        "</div>",
        unsafe_allow_html=True,
    )

    user_input = st.text_area(
        "More details about your notice:",
        height=100,
        key="reclassify_input",
        placeholder="Tell us more about what the notice says...",
        label_visibility="collapsed",
    )

    if st.button(
        "🔍 Try again",
        key="reclassify_submit",
        use_container_width=True,
        type="primary",
    ):
        if user_input and len(user_input.strip()) > 5:
            all_notices = get_all_notice_types(data)
            combined_input = f"{sm.user_input_text} {user_input.strip()}"
            notice_id, confidence, signals = sm.identify_notice_type(
                combined_input, all_notices
            )

            if notice_id and confidence >= 0.2:
                sm.identified_notice_type = notice_id
                sm.advance_stage(sm.STAGE_2_CONFIRM)

                notice_data = get_notice_type_by_id(data, notice_id)
                plain_name = notice_data.get("plain_language_name", "")
                explanation = notice_data.get(
                    "what_it_means_plain_language", ""
                )
                st.session_state["ai_confirmation_text"] = (
                    f"Based on your additional details, it sounds like "
                    f"you received a **{plain_name}** — {explanation}\n\n"
                    f"Does that match what your notice says?"
                )
                st.session_state["current_screen"] = "confirmation"
            else:
                st.session_state["current_screen"] = "notice_selection"
            st.rerun()
        else:
            st.warning("Please provide a bit more detail about your notice.")

    render_disclaimer(disclaimer)


def render_notice_selection_screen(data: dict) -> None:
    """
    Full notice type selection list — fallback after 2 failed classifications.
    All notice types loaded from JSON — no hardcoded list.
    """
    sm = st.session_state["state_manager"]
    freshness = get_data_freshness_date(data)
    disclaimer = get_mandatory_disclaimer(data)

    render_data_freshness_banner(freshness)
    render_app_header()

    st.markdown(
        '<div class="ea-card">'
        '<p style="font-size:1rem;color:#334155;line-height:1.6;">'
        "I want to make sure I give you the right information. "
        "Here are the most common types of notices in California — "
        "can you tell me which one sounds closest to yours?"
        "</p>"
        "</div>",
        unsafe_allow_html=True,
    )

    # Build radio options from JSON
    all_notices = get_all_notice_types(data)
    options = {}
    for notice in all_notices:
        notice_id = notice.get("id", "")
        plain_name = notice.get("plain_language_name", "")
        short_label = notice.get("short_label", "")
        label = f"{short_label} — {plain_name}" if short_label else plain_name
        options[label] = notice_id

    selected = st.radio(
        "Select the notice type that matches yours:",
        options=list(options.keys()),
        key="notice_type_selection",
        label_visibility="collapsed",
    )

    if st.button(
        "✅ Select this notice type",
        key="select_notice_type",
        use_container_width=True,
        type="primary",
    ):
        notice_id = options.get(selected, "")
        if notice_id:
            sm.identified_notice_type = notice_id
            sm.confirmed_notice_type = notice_id
            sm.confirmation_gate_completed = True
            sm.advance_stage(sm.STAGE_2_CONFIRM, confirmed_type=notice_id)

            notice_data = get_notice_type_by_id(data, notice_id)
            plain_name = notice_data.get("plain_language_name", "")
            st.session_state["ai_confirmation_text"] = (
                f"You selected **{plain_name}**. If you are not sure this "
                f"is right, a legal aid attorney can confirm which type of "
                f"notice you received."
            )
            st.session_state["current_screen"] = "acknowledgment"
            st.rerun()

    render_disclaimer(disclaimer)


def render_acknowledgment_screen(data: dict) -> None:
    """
    Acknowledgment Gate — MANDATORY before action plan renders.
    User must actively click to confirm they understand this is
    legal information, not legal advice.
    """
    sm = st.session_state["state_manager"]
    freshness = get_data_freshness_date(data)
    disclaimer = get_mandatory_disclaimer(data)

    render_data_freshness_banner(freshness)

    if st.session_state.get("demo_mode"):
        render_demo_badge()

    render_app_header()

    st.markdown(
        '<div class="ack-gate">'
        "<p>EvictAware provides legal <strong>information</strong>, "
        "not legal advice. This information is based on California "
        "law as of its last update and may not reflect recent changes. "
        "Always verify with a legal aid attorney before acting.</p>"
        "</div>",
        unsafe_allow_html=True,
    )

    if st.button(
        "✅ I understand — show me my action plan",
        key="acknowledge_btn",
        use_container_width=True,
        type="primary",
    ):
        sm.acknowledgment_completed = True
        sm.advance_stage(sm.STAGE_3_ACTION_PLAN, sm.confirmed_notice_type)

        # Generate the action plan
        with st.spinner("📋 Building your personalized action plan..."):
            _generate_action_plan(data, sm)

    render_disclaimer(disclaimer)


def _generate_action_plan(data: dict, sm) -> None:
    """
    Generate the Stage 3 action plan via the seven-layer API fallback.
    Layers 1-4: OpenRouter → 5: Gemini → 6: Groq → 7: Demo cache.
    """
    # If demo mode, use cache directly
    if st.session_state.get("demo_mode"):
        action_plan = load_demo_cache()
        st.session_state["action_plan"] = action_plan
        sm.ai_response_source = "demo:cache"
        st.session_state["current_screen"] = "action_plan"
        st.rerun()
        return

    # Build context for Stage 3
    notice_data = get_notice_type_by_id(data, sm.confirmed_notice_type or "")
    county_aid = get_county_legal_aid(data, sm.user_county or "")
    prohibitions = get_all_prohibitions(data)

    system_prompt = get_master_system_prompt(data["config"])
    context = build_context_injection(
        notice_type_data=notice_data,
        county_legal_aid=county_aid,
        landlord_prohibitions=prohibitions,
        current_stage=sm.STAGE_3_ACTION_PLAN,
        user_county=sm.user_county or "",
        confirmed_notice_type=sm.confirmed_notice_type,
    )
    payload = sm.build_full_api_payload(
        sm.user_input_text, system_prompt, context
    )

    # Seven-layer fallback
    response_text, source = call_ai_with_fallback(
        payload["system_instruction"],
        payload["contents"],
        payload["generation_config"],
        stage="STAGE_3_ACTION_PLAN",
        demo_mode=False,
    )

    # Validate if we got a response
    if response_text:
        validator = EvictAwareOutputValidator(data["config"])
        result = validator.run_full_validation(
            response_text, "STAGE_3_ACTION_PLAN"
        )

        if result["is_valid"] and result["json_parsed"]:
            # Ensure disclaimer is present
            parsed = result["json_parsed"]
            if "disclaimer" not in parsed or not parsed["disclaimer"]:
                parsed["disclaimer"] = get_mandatory_disclaimer(data)
            st.session_state["action_plan"] = parsed
            sm.ai_response_source = source
            st.session_state["current_screen"] = "action_plan"
            st.rerun()
            return
        elif result["action"] == "re_prompt" and result["re_prompt_instruction"]:
            # Try re-prompt once via the same fallback
            reprompt_msg = result["re_prompt_instruction"]
            payload2 = sm.build_full_api_payload(
                reprompt_msg, system_prompt, context
            )
            response2, source2 = call_ai_with_fallback(
                payload2["system_instruction"],
                payload2["contents"],
                payload2["generation_config"],
                stage="STAGE_3_ACTION_PLAN",
                demo_mode=False,
            )

            if response2:
                result2 = validator.run_full_validation(
                    response2, "STAGE_3_ACTION_PLAN"
                )
                if result2["is_valid"] and result2["json_parsed"]:
                    parsed2 = result2["json_parsed"]
                    if "disclaimer" not in parsed2 or not parsed2["disclaimer"]:
                        parsed2["disclaimer"] = get_mandatory_disclaimer(data)
                    st.session_state["action_plan"] = parsed2
                    sm.ai_response_source = source2
                    st.session_state["current_screen"] = "action_plan"
                    st.rerun()
                    return

        # If validation failed but we have cache source, render it
        if source and ("cache" in source):
            import json as _json
            try:
                parsed_cache = _json.loads(response_text)
                parsed_cache["disclaimer"] = get_mandatory_disclaimer(data)
                st.session_state["action_plan"] = parsed_cache
                sm.ai_response_source = source
                st.session_state["current_screen"] = "action_plan"
                st.rerun()
                return
            except Exception:
                pass

    # Final fallback: demo cache with date update
    from ai.cache_date_updater import update_cache_dates
    action_plan = load_demo_cache()
    action_plan = update_cache_dates(action_plan)
    action_plan["disclaimer"] = get_mandatory_disclaimer(data)
    st.session_state["action_plan"] = action_plan
    sm.ai_response_source = "cache_fallback"
    st.session_state["current_screen"] = "action_plan"
    st.rerun()

