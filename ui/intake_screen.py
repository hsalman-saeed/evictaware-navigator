"""
Intake screen — Free-text input and county selection.
User describes their notice and selects their county.
Emergency overrides and state detection happen here.

Clarifying question flow:
  - If local JSON confidence < 0.3 AND AI can't identify → show
    a clarifying question inline (same screen, no transition).
  - User provides more detail → combined text re-run.
  - If still unidentifiable → advance to manual notice selection.
"""
import streamlit as st
from ui.components import (
    render_app_header,
    render_data_freshness_banner,
    render_disclaimer,
    render_emergency_response,
    render_hard_stop,
    render_demo_badge,
)
from data.loader import (
    get_data_freshness_date,
    get_mandatory_disclaimer,
    get_all_county_names,
    get_all_notice_types,
    get_notice_type_by_id,
    get_county_legal_aid,
    get_all_prohibitions,
    get_hard_stop_message,
)
from core.prompt_library import get_prompt
from core.system_prompt import get_master_system_prompt
from core.context_injection import build_context_injection
from core.output_validator import EvictAwareOutputValidator
from ai.openrouter_client import call_openrouter
from ai.gemini_client import call_gemini
from ai.groq_client import call_groq
from config.settings import get_openrouter_api_keys


def render_intake_screen(data: dict) -> None:
    """
    Render the intake screen with text input and county selector.
    On submit: detect emergencies, detect state, classify notice.
    If classification fails: show clarifying question inline.
    """
    sm = st.session_state["state_manager"]
    freshness = get_data_freshness_date(data)
    disclaimer = get_mandatory_disclaimer(data)

    render_data_freshness_banner(freshness)

    if st.session_state.get("demo_mode"):
        render_demo_badge()

    render_app_header()

    # Help text
    st.markdown(
        '<div class="ea-card">'
        '<p style="font-size:1rem;color:#334155;line-height:1.6;">'
        "📝 <strong>Describe your notice</strong> in your own words. "
        "What does the paper say? It's okay if you don't know the "
        "legal terms — just tell us what you see."
        "</p>"
        '<p style="font-size:0.85rem;color:#64748B;font-style:italic;'
        'margin-top:8px;">'
        "Example: \"It says I have 3 days to pay rent or leave. "
        "My landlord also texted me that the sheriff is coming Friday.\""
        "</p>"
        "</div>",
        unsafe_allow_html=True,
    )

    # Text input
    user_input = st.text_area(
        "Describe your notice:",
        height=120,
        key="user_notice_input",
        placeholder=(
            "Type here... What does your notice say? "
            "Include any details about deadlines, amounts, or threats."
        ),
        label_visibility="collapsed",
    )

    # County selector — populated dynamically from JSON
    county_names = get_all_county_names(data)
    county_options = ["Select your county (optional)"] + county_names
    selected_county = st.selectbox(
        "What county are you in?",
        options=county_options,
        key="county_select",
        help="This helps us find the right legal aid office for you.",
    )

    # ── PRIMARY SUBMIT BUTTON ──────────────────────────────────
    if st.button(
        "🔍 Help me understand my notice",
        key="submit_notice",
        use_container_width=True,
        type="primary",
    ):
        if not user_input or len(user_input.strip()) < 10:
            st.warning(
                "Please describe your notice in a few more words "
                "so we can help you accurately."
            )
        else:
            # Save county
            county = (
                selected_county
                if selected_county != "Select your county (optional)"
                else ""
            )
            sm.user_county = county
            sm.user_input_text = user_input.strip()

            # Step 1: Check for non-California location in user input
            ca_status = sm.detect_california_state(user_input)
            if ca_status is False:
                st.session_state["current_screen"] = "hard_stop_non_ca"
                st.rerun()
                return

            # Step 2: Check for emergency overrides
            emergency = sm.detect_emergency_overrides(user_input)
            if emergency:
                sm.emergency_type = emergency
                st.session_state["current_screen"] = "emergency"
                st.rerun()
                return

            # Step 3: Attempt notice classification
            with st.spinner("🔍 Analyzing your notice..."):
                _process_intake(data, sm, user_input)
            # After _process_intake, if needs_clarification was set,
            # the rerun will show the clarification UI below.

    # ── CLARIFYING QUESTION (renders inline when needed) ───────
    if st.session_state.get("needs_clarification", False):
        _render_clarification_section(data, sm)

    render_disclaimer(disclaimer)


def _render_clarification_section(data: dict, sm) -> None:
    """
    Render the clarifying question box, second input, and
    re-submit button inline on the same intake screen.
    """
    # Styled clarification box
    st.markdown(
        '<div style="background:linear-gradient(135deg,#EFF6FF,#DBEAFE);'
        "border:1px solid #93C5FD;border-radius:12px;padding:20px;"
        'margin:16px 0;">'
        '<p style="font-size:1rem;color:#1E40AF;font-weight:600;'
        'margin-bottom:8px;">💬 Can you tell me a little more?</p>'
        '<p style="font-size:0.92rem;color:#334155;line-height:1.6;'
        'margin:0;">'
        "Can you tell me more about what the notice says? "
        "For example: How many days does it mention? "
        "Does it say you can pay to stay, or that you must leave "
        "no matter what?"
        "</p>"
        "</div>",
        unsafe_allow_html=True,
    )

    # Second text input for additional detail
    additional_detail = st.text_area(
        "Add more detail about your notice:",
        height=100,
        key="clarification_input",
        placeholder=(
            "For example: 'It says 3 days' or 'It mentions paying rent' "
            "or 'It says I have to fix something in the apartment'..."
        ),
        label_visibility="collapsed",
    )

    # Second submit button
    if st.button(
        "➕ Add more detail and continue",
        key="clarification_submit",
        use_container_width=True,
        type="primary",
    ):
        if not additional_detail or len(additional_detail.strip()) < 3:
            st.warning("Please provide a few more words about your notice.")
            return

        combined_text = (
            f"{sm.user_input_text} {additional_detail.strip()}"
        )

        with st.spinner("🔍 Re-analyzing with your additional details..."):
            _process_clarification(data, sm, combined_text)


def _process_intake(data: dict, sm, user_input: str) -> None:
    """Process the user's intake text through the AI pipeline."""
    # First, try local identification from JSON signals
    all_notices = get_all_notice_types(data)
    notice_id, confidence, signals = sm.identify_notice_type(
        user_input, all_notices
    )

    if notice_id and confidence >= 0.3:
        # High enough confidence — go to confirmation gate
        _advance_to_confirmation(data, sm, user_input, notice_id, all_notices)
    else:
        # Low confidence — try AI identification
        _try_ai_identification(data, sm, user_input, all_notices)


def _advance_to_confirmation(
    data: dict, sm, user_input: str, notice_id: str, all_notices: list
) -> None:
    """Advance to confirmation gate with identified notice type."""
    sm.identified_notice_type = notice_id
    notice_data = get_notice_type_by_id(data, notice_id)
    sm.advance_stage(sm.STAGE_2_CONFIRM)

    # Call AI for a natural-language confirmation message
    system_prompt = get_master_system_prompt(data["config"])
    context = build_context_injection(
        notice_type_data=notice_data,
        county_legal_aid={},
        landlord_prohibitions=[],
        current_stage=sm.STAGE_2_CONFIRM,
        user_county=sm.user_county,
        all_notice_types=all_notices,
    )
    payload = sm.build_full_api_payload(user_input, system_prompt, context)

    # Seven-layer API fallback (OpenRouter x4 → Gemini → Groq)
    or_keys = get_openrouter_api_keys()
    response_text, source = None, None
    if or_keys:
        response_text, source = call_openrouter(
            payload["system_instruction"],
            payload["contents"],
            payload["generation_config"],
            or_keys,
        )
    if not response_text:
        response_text, source = call_gemini(
            payload["system_instruction"],
            payload["contents"],
            payload["generation_config"],
        )
    if not response_text:
        response_text, source = call_groq(
            payload["system_instruction"],
            payload["contents"],
            payload["generation_config"],
        )

    if response_text:
        sm.ai_response_source = source
        sm.add_to_history("user", user_input)
        sm.add_to_history("model", response_text)
        st.session_state["ai_confirmation_text"] = response_text
    else:
        # Use the notice data for a programmatic confirmation
        plain_name = notice_data.get("plain_language_name", "")
        explanation = notice_data.get("what_it_means_plain_language", "")
        st.session_state["ai_confirmation_text"] = (
            f"Based on what you described, it sounds like you received "
            f"a **{plain_name}** — {explanation}\n\n"
            f"Does that match what your notice says?"
        )
        sm.ai_response_source = "local:json"

    # Clear any previous clarification state
    st.session_state["needs_clarification"] = False
    st.session_state["current_screen"] = "confirmation"
    st.rerun()


def _try_ai_identification(
    data: dict, sm, user_input: str, all_notices: list
) -> None:
    """
    Try AI-based identification. If AI can identify → confirmation.
    If AI can't identify → show clarifying question inline.
    If both APIs fail → show clarifying question inline.
    """
    system_prompt = get_master_system_prompt(data["config"])
    context = build_context_injection(
        notice_type_data={},
        county_legal_aid={},
        landlord_prohibitions=[],
        current_stage=sm.STAGE_1_IDENTIFY,
        user_county=sm.user_county,
        all_notice_types=all_notices,
    )
    payload = sm.build_full_api_payload(user_input, system_prompt, context)

    or_keys = get_openrouter_api_keys()
    response_text, source = None, None
    if or_keys:
        response_text, source = call_openrouter(
            payload["system_instruction"],
            payload["contents"],
            payload["generation_config"],
            or_keys,
        )
    if not response_text:
        response_text, source = call_gemini(
            payload["system_instruction"],
            payload["contents"],
            payload["generation_config"],
        )
    if not response_text:
        response_text, source = call_groq(
            payload["system_instruction"],
            payload["contents"],
            payload["generation_config"],
        )

    if response_text:
        sm.ai_response_source = source
        sm.add_to_history("user", user_input)
        sm.add_to_history("model", response_text)

        # Try to detect if the AI identified a notice type
        identified = _extract_notice_id_from_response(
            response_text, all_notices
        )
        if identified:
            sm.identified_notice_type = identified
            sm.advance_stage(sm.STAGE_2_CONFIRM)
            st.session_state["ai_confirmation_text"] = response_text
            st.session_state["needs_clarification"] = False
            st.session_state["current_screen"] = "confirmation"
            st.rerun()
            return

    # AI couldn't identify either, or both APIs failed.
    # Set the flag so the clarification UI renders inline.
    st.session_state["needs_clarification"] = True
    st.session_state["clarification_attempt"] = 1
    st.rerun()


def _process_clarification(data: dict, sm, combined_text: str) -> None:
    """
    Process the second attempt with combined text.
    If identification succeeds → confirmation gate.
    If fails again → manual notice type selection list.
    """
    all_notices = get_all_notice_types(data)

    # Try local identification with combined text
    notice_id, confidence, signals = sm.identify_notice_type(
        combined_text, all_notices
    )

    if notice_id and confidence >= 0.2:
        # Lower threshold on second attempt since user added detail
        sm.user_input_text = combined_text
        st.session_state["needs_clarification"] = False
        _advance_to_confirmation(
            data, sm, combined_text, notice_id, all_notices
        )
        return

    # Try AI identification with combined text
    system_prompt = get_master_system_prompt(data["config"])
    context = build_context_injection(
        notice_type_data={},
        county_legal_aid={},
        landlord_prohibitions=[],
        current_stage=sm.STAGE_1_IDENTIFY,
        user_county=sm.user_county,
        all_notice_types=all_notices,
    )
    payload = sm.build_full_api_payload(
        combined_text, system_prompt, context
    )

    or_keys = get_openrouter_api_keys()
    response_text, source = None, None
    if or_keys:
        response_text, source = call_openrouter(
            payload["system_instruction"],
            payload["contents"],
            payload["generation_config"],
            or_keys,
        )
    if not response_text:
        response_text, source = call_gemini(
            payload["system_instruction"],
            payload["contents"],
            payload["generation_config"],
        )
    if not response_text:
        response_text, source = call_groq(
            payload["system_instruction"],
            payload["contents"],
            payload["generation_config"],
        )

    if response_text:
        sm.ai_response_source = source
        sm.add_to_history("user", combined_text)
        sm.add_to_history("model", response_text)

        identified = _extract_notice_id_from_response(
            response_text, all_notices
        )
        if identified:
            sm.identified_notice_type = identified
            sm.advance_stage(sm.STAGE_2_CONFIRM)
            sm.user_input_text = combined_text
            st.session_state["ai_confirmation_text"] = response_text
            st.session_state["needs_clarification"] = False
            st.session_state["current_screen"] = "confirmation"
            st.rerun()
            return

    # Second attempt also failed → go to manual notice selection
    st.session_state["needs_clarification"] = False
    st.session_state["current_screen"] = "notice_selection"
    st.rerun()


def _extract_notice_id_from_response(
    response_text: str, all_notices: list
) -> str:
    """
    Try to detect which notice type the AI identified from its response.
    Checks if any notice type name appears in the response.
    """
    text_lower = response_text.lower()
    for notice in all_notices:
        legal_name = notice.get("legal_name", "").lower()
        plain_name = notice.get("plain_language_name", "").lower()
        short_label = notice.get("short_label", "").lower()
        if (
            (legal_name and legal_name in text_lower)
            or (plain_name and plain_name in text_lower)
            or (short_label and short_label in text_lower)
        ):
            return notice.get("id")
    return ""


def render_emergency_screen(data: dict) -> None:
    """Render emergency response (lockout, DV, shelter)."""
    sm = st.session_state["state_manager"]
    freshness = get_data_freshness_date(data)
    disclaimer = get_mandatory_disclaimer(data)

    render_data_freshness_banner(freshness)
    render_app_header()

    # Get the appropriate emergency prompt
    prompt_map = {
        sm.EMERGENCY_LOCKOUT: "PE-A",
        sm.EMERGENCY_DV: "PE-B",
        sm.EMERGENCY_SHELTER: "PE-C",
    }
    prompt_id = prompt_map.get(sm.emergency_type, "PE-A")
    message = get_prompt(prompt_id)

    render_emergency_response(sm.emergency_type, message, disclaimer)

    # Offer to continue with notice analysis
    st.markdown("---")
    st.markdown(
        '<p style="text-align:center;color:#475569;font-size:0.9rem;">'
        "Once your immediate safety needs are addressed, you can also "
        "analyze your eviction notice below."
        "</p>",
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)
    with col1:
        if st.button(
            "📝 Analyze my notice too",
            key="continue_after_emergency",
            use_container_width=True,
            type="primary",
        ):
            sm.emergency_type = None
            st.session_state["current_screen"] = "intake"
            st.rerun()
    with col2:
        if st.button(
            "← Start Over",
            key="start_over_emergency",
            use_container_width=True,
        ):
            sm.reset()
            st.session_state["current_screen"] = "welcome"
            st.rerun()
