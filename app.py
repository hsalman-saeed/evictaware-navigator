"""
EvictAware — California Tenant Rights Navigator
Main Streamlit Entry Point

USAII Global AI Hackathon 2026 | Team Vision Forge | Challenge Brief 4

Three-layer AI fallback:
  Layer 1: Gemini API (google-generativeai)
  Layer 2: Groq API (llama-3.3-70b-versatile)
  Layer 3: demo_cache_priya_nt001.json (guaranteed)

10 Absolute Constraints enforced:
  1. NO hardcoded AI responses
  2. NO hardcoded dates
  3. NO hardcoded legal content
  4. NO hardcoded phone numbers or contacts
  5. NO hardcoded county/state logic
  6. NO API keys in Python code
  7. Confirmation Gate MANDATORY
  8. Acknowledgment Button MANDATORY
  9. Mandatory disclaimer on EVERY output
  10. All dates read from JSON metadata
"""
import streamlit as st
from config.settings import APP_NAME, APP_SUBTITLE, DEMO_MODE_DEFAULT
from data.loader import (
    load_all_data,
    get_data_freshness_date,
    get_notice_type_by_id,
    get_mandatory_disclaimer,
)
from core.state_manager import EvictAwareStateManager
from ui.styles import inject_custom_css
from ui.welcome_screen import render_welcome_screen, render_non_california_stop
from ui.intake_screen import render_intake_screen, render_emergency_screen
from ui.confirmation_screen import (
    render_confirmation_screen,
    render_reclassification_screen,
    render_notice_selection_screen,
    render_acknowledgment_screen,
)
from ui.action_plan_screen import render_action_plan_screen
from ai.fallback import load_demo_cache

# ── PAGE CONFIG ──────────────────────────────────────────────
st.set_page_config(
    page_title=f"{APP_NAME} — {APP_SUBTITLE}",
    page_icon="🏠",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items={
        "About": (
            f"**{APP_NAME}** — {APP_SUBTITLE}\n\n"
            "Built by Team Vision Forge for the "
            "USAII Global AI Hackathon 2026.\n\n"
            "This tool provides legal information, not legal advice."
        ),
    },
)


# ── INJECT CSS ────────────────────────────────────────────────
inject_custom_css()


# ── LOAD DATA ─────────────────────────────────────────────────
data = load_all_data()


# ── INITIALIZE SESSION STATE ──────────────────────────────────
if "state_manager" not in st.session_state:
    st.session_state["state_manager"] = EvictAwareStateManager()

if "current_screen" not in st.session_state:
    st.session_state["current_screen"] = "welcome"

if "demo_mode" not in st.session_state:
    st.session_state["demo_mode"] = DEMO_MODE_DEFAULT

if "action_plan" not in st.session_state:
    st.session_state["action_plan"] = {}

if "ai_confirmation_text" not in st.session_state:
    st.session_state["ai_confirmation_text"] = ""

if "ai_clarification" not in st.session_state:
    st.session_state["ai_clarification"] = ""

if "needs_clarification" not in st.session_state:
    st.session_state["needs_clarification"] = False

if "clarification_attempt" not in st.session_state:
    st.session_state["clarification_attempt"] = 0


# ── SIDEBAR ───────────────────────────────────────────────────
with st.sidebar:
    st.markdown(
        '<p style="font-size:1.1rem;font-weight:700;'
        'color:#0D9488;margin-bottom:4px;">🏠 EvictAware</p>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<p style="font-size:0.8rem;color:#64748B;margin-top:0;">'
        "California Tenant Rights Navigator</p>",
        unsafe_allow_html=True,
    )

    st.divider()

    # Data freshness — read from JSON, NEVER hardcoded
    freshness = get_data_freshness_date(data)
    st.markdown(
        f'<p style="font-size:0.75rem;color:#94A3B8;">'
        f"📋 Legal info verified: <strong>{freshness}</strong></p>",
        unsafe_allow_html=True,
    )

    st.divider()

    # Demo Mode toggle
    demo_mode = st.toggle(
        "🎬 Demo Mode (Priya's scenario)",
        value=st.session_state.get("demo_mode", False),
        key="demo_toggle",
        help=(
            "Runs the pre-verified Priya Sharma scenario using "
            "cached responses. Use this if the API is unavailable "
            "or for a guaranteed demo."
        ),
    )

    if demo_mode != st.session_state.get("demo_mode", False):
        st.session_state["demo_mode"] = demo_mode
        if demo_mode:
            # Activate demo mode — jump straight to action plan
            sm = st.session_state["state_manager"]
            sm.reset()
            sm.california_confirmed = True
            sm.identified_notice_type = "NT001"
            sm.confirmed_notice_type = "NT001"
            sm.confirmation_gate_completed = True
            sm.acknowledgment_completed = True
            sm.user_county = "Fresno"
            sm.ai_response_source = "demo:cache"
            sm.advance_stage(sm.STAGE_3_ACTION_PLAN, "NT001")

            action_plan = load_demo_cache()
            disclaimer = get_mandatory_disclaimer(data)
            if disclaimer:
                action_plan["disclaimer"] = action_plan.get(
                    "disclaimer", disclaimer
                )
            st.session_state["action_plan"] = action_plan
            st.session_state["current_screen"] = "action_plan"
            st.rerun()
        else:
            # Deactivate demo mode — reset
            st.session_state["state_manager"].reset()
            st.session_state["action_plan"] = {}
            st.session_state["current_screen"] = "welcome"
            st.rerun()

    st.divider()

    # Start Over button
    if st.button(
        "← Start Over",
        key="sidebar_start_over",
        use_container_width=True,
    ):
        st.session_state["state_manager"].reset()
        st.session_state["action_plan"] = {}
        st.session_state["ai_confirmation_text"] = ""
        st.session_state["ai_clarification"] = ""
        st.session_state["needs_clarification"] = False
        st.session_state["clarification_attempt"] = 0
        st.session_state["demo_mode"] = False
        st.session_state["current_screen"] = "welcome"
        st.rerun()

    # Current stage indicator
    sm = st.session_state["state_manager"]
    stage_labels = {
        sm.STAGE_1_IDENTIFY: "1️⃣ Identifying notice",
        sm.STAGE_2_CONFIRM: "2️⃣ Confirming type",
        sm.STAGE_3_ACTION_PLAN: "3️⃣ Action plan",
        sm.EMERGENCY_LOCKOUT: "🚨 Emergency",
        sm.EMERGENCY_DV: "💜 Safety first",
        sm.EMERGENCY_SHELTER: "🏠 Shelter needed",
        sm.HARD_STOP_STATE: "⚠️ Cannot proceed",
    }
    current_label = stage_labels.get(sm.current_stage, "")
    if current_label:
        st.markdown(
            f'<p style="font-size:0.75rem;color:#94A3B8;margin-top:8px;">'
            f"Stage: {current_label}</p>",
            unsafe_allow_html=True,
        )


# ── SCREEN ROUTER ─────────────────────────────────────────────
screen = st.session_state.get("current_screen", "welcome")

if screen == "welcome":
    render_welcome_screen(data)

elif screen == "intake":
    render_intake_screen(data)

elif screen == "confirmation":
    render_confirmation_screen(data)

elif screen == "reclassify":
    render_reclassification_screen(data)

elif screen == "notice_selection":
    render_notice_selection_screen(data)

elif screen == "acknowledgment":
    render_acknowledgment_screen(data)

elif screen == "action_plan":
    render_action_plan_screen(data)

elif screen == "emergency":
    render_emergency_screen(data)

elif screen == "hard_stop_non_ca":
    render_non_california_stop(data)

else:
    render_welcome_screen(data)
