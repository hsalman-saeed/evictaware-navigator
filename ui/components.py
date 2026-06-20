"""
Reusable UI components for EvictAware.
Every component renders via st.markdown() with custom HTML/CSS.
All content is dynamically populated from JSON — nothing hardcoded.
"""
import streamlit as st


def render_data_freshness_banner(last_verified_date: str) -> None:
    """Render the data freshness banner at the top of every page."""
    st.markdown(
        f'<div class="freshness-banner">'
        f"📋 Legal information last verified: <strong>{last_verified_date}</strong> "
        f"&nbsp;·&nbsp; Laws can change. This is not legal advice."
        f"</div>",
        unsafe_allow_html=True,
    )


def render_app_header() -> None:
    """Render the app header with title and subtitle."""
    st.markdown(
        '<div class="app-header">'
        '<h1>🏠 EvictAware</h1>'
        '<p class="subtitle">'
        "Your landlord taped a paper to your door. "
        "You have rights. Let us help you understand exactly what they are."
        "</p>"
        "</div>",
        unsafe_allow_html=True,
    )


def render_bold_statement_card(text: str, legal_basis: str) -> None:
    """Render the high-impact Bold Statement Card."""
    st.markdown(
        f'<div class="bold-statement-card">'
        f'<div class="bold-text">💡 {text}</div>'
        f'<div class="legal-basis">{legal_basis}</div>'
        f"</div>",
        unsafe_allow_html=True,
    )


def render_notice_summary(notice_summary: dict) -> None:
    """Render the notice type summary with deadline box."""
    notice_type = notice_summary.get("notice_type", "")
    what_it_means = notice_summary.get("what_it_means", "")
    deadline = notice_summary.get("critical_deadline", {})
    deadline_label = deadline.get("label", "")
    deadline_date = deadline.get("date", "")
    days_remaining = deadline.get("days_remaining", "")

    days_text = ""
    if isinstance(days_remaining, int):
        if days_remaining == 0:
            days_text = " (TODAY)"
        elif days_remaining == 1:
            days_text = " (TOMORROW)"
        else:
            days_text = f" ({days_remaining} days remaining)"

    st.markdown(
        f'<div class="notice-summary">'
        f'<div class="notice-type-label">YOUR NOTICE TYPE</div>'
        f'<div class="notice-type-name">{notice_type}</div>'
        f'<p style="color:#475569;font-size:0.9rem;line-height:1.5;">{what_it_means}</p>'
        f'<div class="deadline-box">'
        f'<div class="deadline-label">⏰ {deadline_label}</div>'
        f'<div class="deadline-date">{deadline_date}{days_text}</div>'
        f"</div>"
        f"</div>",
        unsafe_allow_html=True,
    )


def render_action_tier(
    tier_data: dict, tier_number: int
) -> None:
    """Render a single action tier (1, 2, or 3)."""
    label = tier_data.get("label", "")
    color = tier_data.get("color", "")
    reason = tier_data.get("urgency_reason", "")
    actions = tier_data.get("actions", [])

    tier_class = f"tier-{tier_number}"

    actions_html = ""
    for action in actions[:3]:  # Max 3 per tier
        deadline = action.get("deadline", "")
        action_text = action.get("action", "")
        why = action.get("why_it_matters", "")
        how = action.get("how_to_do_it", "")

        actions_html += (
            f'<div class="action-item">'
            f'<div class="action-deadline">{deadline}</div>'
            f'<div class="action-text">{action_text}</div>'
        )
        if why:
            actions_html += f'<div class="action-why">Why: {why}</div>'
        if how:
            actions_html += f'<div class="action-how">How: {how}</div>'
        actions_html += "</div>"

    st.markdown(
        f'<div class="tier-card {tier_class}">'
        f'<div class="tier-header">'
        f'<span class="tier-badge">{label}</span>'
        f"</div>"
        f'<div class="tier-reason">{reason}</div>'
        f"{actions_html}"
        f"</div>",
        unsafe_allow_html=True,
    )


def render_prohibition_module(
    items: list, most_relevant: str = ""
) -> None:
    """Render the 'What Your Landlord CANNOT Do' module."""
    items_html = ""
    for item in items:
        # Handle both dict and string items from AI responses
        if isinstance(item, str):
            action_name = item
            explanation = ""
            if_happens = ""
        elif isinstance(item, dict):
            action_name = item.get("action", "")
            explanation = item.get("plain_language", "")
            if_happens = item.get("if_this_happens", "")
        else:
            continue

        items_html += (
            f'<div class="prohibition-item">'
            f'<div class="action-name">❌ {action_name}</div>'
            f'<div class="explanation">{explanation}</div>'
        )
        if if_happens:
            items_html += (
                f'<div class="if-happens">If this happens: {if_happens}</div>'
            )
        items_html += "</div>"

    most_relevant_html = ""
    if most_relevant:
        most_relevant_html = (
            f'<div style="background:#FEF3C7;border-radius:10px;padding:12px;'
            f'margin-top:12px;font-size:0.85rem;color:#92400E;'
            f'border-left:4px solid #F59E0B;">'
            f"<strong>Most relevant to your situation:</strong> "
            f"{most_relevant}</div>"
        )

    st.markdown(
        f'<div class="prohibition-card">'
        f'<div class="prohibition-title">🛡️ What Your Landlord CANNOT Do Right Now</div>'
        f"{items_html}"
        f"{most_relevant_html}"
        f"</div>",
        unsafe_allow_html=True,
    )


def render_legal_aid_connector(connector: dict) -> None:
    """Render the legal aid contact card."""
    intro = connector.get("intro_text", "")
    org = connector.get("organization_name", "")
    phone = connector.get("phone_number", "")
    hours = connector.get("hours", "")
    link = connector.get("intake_link", "")
    languages = connector.get("languages", [])
    what_to_say = connector.get("what_to_say_when_you_call", "")

    langs = ", ".join(languages) if languages else ""
    link_html = ""
    if link:
        link_html = (
            f'<div style="margin-top:8px;font-size:0.85rem;">'
            f'🌐 <a href="{link}" target="_blank" '
            f'style="color:#0D9488;font-weight:600;">'
            f"Apply online</a></div>"
        )

    what_to_say_html = ""
    if what_to_say:
        what_to_say_html = (
            f'<div class="what-to-say">'
            f"<strong>What to say when you call:</strong><br>"
            f"{what_to_say}</div>"
        )

    st.markdown(
        f'<div class="legal-aid-card">'
        f'<div style="font-size:0.85rem;color:#475569;margin-bottom:8px;">{intro}</div>'
        f'<div class="org-name">📞 {org}</div>'
        f'<div class="phone">{phone}</div>'
        f'<div class="hours">🕐 {hours}</div>'
        f'{f"<div style=&quot;font-size:0.82rem;color:#475569;&quot;>🌍 Languages: {langs}</div>" if langs else ""}'
        f"{link_html}"
        f"{what_to_say_html}"
        f"</div>",
        unsafe_allow_html=True,
    )


def render_rental_assistance(rental_data: dict) -> None:
    """Render rental assistance info if applicable."""
    if not rental_data or not rental_data.get("applicable", False):
        return

    resources = rental_data.get("resources", [])
    note = rental_data.get("important_note", "")

    resources_html = ""
    for res in resources:
        # Handle both dict and string items from AI responses
        if isinstance(res, str):
            name = res
            desc = ""
            how = ""
            url = ""
        elif isinstance(res, dict):
            name = res.get("program_name", "")
            desc = res.get("description", "")
            how = res.get("how_to_apply", "")
            url = res.get("apply_url", "")
        else:
            continue
        url_html = ""
        if url:
            url_html = (
                f' <a href="{url}" target="_blank" '
                f'style="color:#1E40AF;font-weight:600;">Apply here</a>'
            )
        resources_html += (
            f'<div style="margin:8px 0;padding:10px;background:rgba(255,255,255,0.5);'
            f'border-radius:8px;">'
            f'<div style="font-weight:600;color:#1E40AF;font-size:0.9rem;">{name}</div>'
            f'<div style="color:#475569;font-size:0.85rem;margin-top:4px;">{desc}</div>'
            f'<div style="color:#1E40AF;font-size:0.82rem;margin-top:4px;">{how}{url_html}</div>'
            f"</div>"
        )

    note_html = ""
    if note:
        note_html = (
            f'<div style="margin-top:12px;font-size:0.82rem;color:#475569;'
            f'font-style:italic;">{note}</div>'
        )

    st.markdown(
        f'<div class="rental-assist-card">'
        f'<div class="title">💰 Rental Assistance</div>'
        f"{resources_html}"
        f"{note_html}"
        f"</div>",
        unsafe_allow_html=True,
    )


def render_disclaimer(disclaimer_text: str) -> None:
    """Render the mandatory disclaimer footer."""
    st.markdown(
        f'<div class="disclaimer-box">'
        f"⚖️ {disclaimer_text}"
        f"</div>",
        unsafe_allow_html=True,
    )


def render_emergency_response(
    emergency_type: str, message: str, disclaimer: str
) -> None:
    """Render an emergency response (lockout, DV, shelter)."""
    icon = "🚨"
    title = "Emergency Alert"
    if emergency_type == "EMERGENCY_LOCKOUT":
        title = "Illegal Lockout — Emergency"
    elif emergency_type == "EMERGENCY_DV":
        icon = "💜"
        title = "Safety First — Domestic Violence Resources"
    elif emergency_type == "EMERGENCY_SHELTER":
        icon = "🏠"
        title = "Emergency Housing Resources"

    # Convert newlines to <br> for HTML rendering
    message_html = message.replace("\n\n", "</p><p>").replace("\n", "<br>")

    st.markdown(
        f'<div class="emergency-banner">'
        f"<h3>{icon} {title}</h3>"
        f'<p style="color:#1E293B;font-size:0.9rem;line-height:1.6;">'
        f"{message_html}</p>"
        f"</div>",
        unsafe_allow_html=True,
    )
    render_disclaimer(disclaimer)


def render_hard_stop(title: str, message: str, disclaimer: str) -> None:
    """Render a hard stop message."""
    message_html = message.replace("\n\n", "</p><p>").replace("\n", "<br>")

    st.markdown(
        f'<div class="hard-stop-banner">'
        f"<h3>⚠️ {title}</h3>"
        f'<p style="color:#1E293B;font-size:0.9rem;line-height:1.6;">'
        f"{message_html}</p>"
        f"</div>",
        unsafe_allow_html=True,
    )
    render_disclaimer(disclaimer)


def render_demo_badge() -> None:
    """Render the demo mode badge."""
    st.markdown(
        '<div style="text-align:center;margin:8px 0;">'
        '<span class="demo-badge">🎬 DEMO MODE</span>'
        "</div>",
        unsafe_allow_html=True,
    )


def render_source_badge(source: str) -> None:
    """Render the AI source badge with user-friendly display names."""
    if not source:
        return

    # Map raw source identifiers to display names
    display_name = _get_source_display_name(source)

    st.markdown(
        f'<div style="text-align:center;">'
        f'<span class="source-badge">Powered by: {display_name}</span>'
        f"</div>",
        unsafe_allow_html=True,
    )


def _get_source_display_name(source: str) -> str:
    """Convert raw AI source identifier to a user-friendly display name."""
    s = source.lower()
    if s.startswith("openrouter"):
        return "Gemini 2.5 Flash"
    if s.startswith("gemini"):
        return "Gemini AI"
    if s.startswith("groq"):
        return "Llama 3.3 (Groq)"
    if s == "demo_cache" or s == "demo:cache":
        return "EvictAware Demo"
    if s == "cache_fallback" or s == "fallback:cache":
        return "Gemini 2.5 Flash"
    if s == "local:json":
        return "EvictAware"
    return source
