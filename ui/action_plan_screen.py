"""
Action Plan screen — renders the complete Stage 3 output.
This is the final screen users see after both gates are completed.
All content is dynamically rendered from the validated JSON response.
Nothing is hardcoded — every field comes from the AI or the demo cache.
"""
import streamlit as st
from ui.components import (
    render_app_header,
    render_data_freshness_banner,
    render_bold_statement_card,
    render_notice_summary,
    render_action_tier,
    render_prohibition_module,
    render_legal_aid_connector,
    render_rental_assistance,
    render_disclaimer,
    render_demo_badge,
    render_source_badge,
)
from data.loader import get_data_freshness_date, get_mandatory_disclaimer


def render_action_plan_screen(data: dict) -> None:
    """
    Render the complete action plan from the validated JSON.
    Enforces: Confirmation Gate + Acknowledgment Gate must both be True.
    Order: Bold Card → Notice Summary → Tiers 1/2/3 →
           Prohibitions → Legal Aid → Rental Assistance → Disclaimer.
    """
    sm = st.session_state["state_manager"]

    # ── GATE ENFORCEMENT ────────────────────────────────────
    # Action plan CANNOT render without both gates completed.
    if not sm.confirmation_gate_completed:
        st.error("Confirmation gate not completed. Returning to confirmation.")
        st.session_state["current_screen"] = "confirmation"
        st.rerun()
        return

    if not sm.acknowledgment_completed:
        st.error("Acknowledgment not completed. Returning to acknowledgment.")
        st.session_state["current_screen"] = "acknowledgment"
        st.rerun()
        return

    # ── LOAD ACTION PLAN DATA ────────────────────────────────
    action_plan = st.session_state.get("action_plan", {})
    if not action_plan:
        st.error("No action plan data available.")
        return

    freshness = get_data_freshness_date(data)
    disclaimer_from_config = get_mandatory_disclaimer(data)

    # ── RENDER ────────────────────────────────────────────────
    render_data_freshness_banner(freshness)

    if st.session_state.get("demo_mode"):
        render_demo_badge()

    render_app_header()

    # 1. Bold Statement Card
    bold_card = action_plan.get("bold_statement_card", {})
    if bold_card:
        render_bold_statement_card(
            text=bold_card.get("text", ""),
            legal_basis=bold_card.get("legal_basis", ""),
        )

    # 2. Notice Summary with Deadline Box
    notice_summary = action_plan.get("notice_summary", {})
    if notice_summary:
        render_notice_summary(notice_summary)

    # 3. Action Tiers (1, 2, 3)
    tiers = action_plan.get("action_tiers", {})

    tier_1 = tiers.get("tier_1", {})
    if tier_1:
        render_action_tier(tier_1, 1)

    tier_2 = tiers.get("tier_2", {})
    if tier_2:
        render_action_tier(tier_2, 2)

    tier_3 = tiers.get("tier_3", {})
    if tier_3:
        render_action_tier(tier_3, 3)

    # 4. Landlord Cannot Do Module
    landlord_module = action_plan.get("landlord_cannot_do", {})
    if landlord_module:
        items = landlord_module.get("items", [])
        most_relevant = landlord_module.get(
            "most_relevant_to_user_situation", ""
        )
        if items:
            render_prohibition_module(items, most_relevant)

    # 5. Legal Aid Connector
    legal_aid = action_plan.get("legal_aid_connector", {})
    if legal_aid:
        render_legal_aid_connector(legal_aid)

    # 6. Rental Assistance (conditional)
    rental = action_plan.get("rental_assistance", {})
    if rental:
        render_rental_assistance(rental)

    # 7. AI Source Badge
    render_source_badge(sm.ai_response_source or "")

    # 8. Mandatory Disclaimer — ALWAYS rendered, EVERY time
    disclaimer_text = action_plan.get("disclaimer", "") or disclaimer_from_config
    render_disclaimer(disclaimer_text)

    # ── NAVIGATION ────────────────────────────────────────────
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        if st.button(
            "🔄 Analyze another notice",
            key="new_notice_btn",
            use_container_width=True,
        ):
            sm.reset()
            sm.california_confirmed = True  # Don't re-ask CA gate
            st.session_state["action_plan"] = {}
            st.session_state["ai_confirmation_text"] = ""
            st.session_state["current_screen"] = "intake"
            st.rerun()
    with col2:
        if st.button(
            "🏠 Start Over",
            key="start_over_btn",
            use_container_width=True,
        ):
            sm.reset()
            st.session_state["action_plan"] = {}
            st.session_state["ai_confirmation_text"] = ""
            st.session_state["demo_mode"] = False
            st.session_state["current_screen"] = "welcome"
            st.rerun()
