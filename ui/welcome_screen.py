"""
Welcome screen — State Scope Lock + Demo Mode toggle.
This is the first screen users see.
The California gate is mandatory before any legal content is shown.
"""
import streamlit as st
from ui.components import (
    render_app_header,
    render_data_freshness_banner,
    render_hard_stop,
    render_disclaimer,
)
from data.loader import get_data_freshness_date, get_mandatory_disclaimer


def render_welcome_screen(data: dict) -> None:
    """
    Render the welcome screen with California scope lock.
    No legal content is shown until user confirms California.
    """
    freshness = get_data_freshness_date(data)
    disclaimer = get_mandatory_disclaimer(data)

    render_data_freshness_banner(freshness)
    render_app_header()

    # State Scope Lock — California gate
    st.markdown(
        '<div class="gate-container">'
        '<div class="gate-text">'
        "EvictAware provides legal <strong>information</strong> "
        "(not legal advice) about California tenant rights only. "
        "Before we begin, we need to confirm:"
        "</div>"
        '<p style="font-size:1.1rem;font-weight:600;color:#0F172A;'
        'text-align:center;">'
        "Are you a renter in California?"
        "</p>"
        "</div>",
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)
    with col1:
        if st.button(
            "✅ Yes, I'm in California",
            key="ca_yes",
            use_container_width=True,
            type="primary",
        ):
            sm = st.session_state["state_manager"]
            sm.california_confirmed = True
            st.session_state["current_screen"] = "intake"
            st.rerun()

    with col2:
        if st.button(
            "❌ No, I'm in another state",
            key="ca_no",
            use_container_width=True,
        ):
            st.session_state["current_screen"] = "hard_stop_non_ca"
            st.rerun()

    render_disclaimer(disclaimer)


def render_non_california_stop(data: dict) -> None:
    """Render the non-California hard stop."""
    freshness = get_data_freshness_date(data)
    disclaimer = get_mandatory_disclaimer(data)

    render_data_freshness_banner(freshness)
    render_app_header()

    # Get the hard stop message from ai_config.json
    hard_stops = data["config"].get("hard_stop_config", {})
    non_ca = hard_stops.get("hard_stop_1_non_california", {})
    message = non_ca.get("message", "")

    render_hard_stop("California Only", message, disclaimer)

    if st.button(
        "← Start Over",
        key="start_over_non_ca",
        use_container_width=True,
    ):
        st.session_state["state_manager"].reset()
        st.session_state["current_screen"] = "welcome"
        st.rerun()
