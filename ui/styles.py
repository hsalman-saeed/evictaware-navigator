"""
Custom CSS for EvictAware — Light theme with premium design.
Injected via st.markdown() with unsafe_allow_html=True.
Uses Inter font, teal accents, and tier-specific colors.
"""


def inject_custom_css():
    """Inject the complete CSS stylesheet into the Streamlit app."""
    import streamlit as st

    css = """
    <style>
    /* ===== Google Font ===== */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    /* ===== Global ===== */
    html, body, [class*="css"], .stApp {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
    }

    .stApp {
        background: linear-gradient(180deg, #FFFFFF 0%, #F8FAFC 100%);
    }

    /* ===== Hide default Streamlit elements ===== */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* ===== Data Freshness Banner ===== */
    .freshness-banner {
        background: linear-gradient(90deg, #F0FDFA 0%, #CCFBF1 50%, #F0FDFA 100%);
        border-bottom: 1px solid #99F6E4;
        padding: 8px 16px;
        text-align: center;
        font-size: 12px;
        color: #115E59;
        font-weight: 500;
        letter-spacing: 0.3px;
        animation: fadeIn 0.5s ease-in;
    }

    /* ===== App Header ===== */
    .app-header {
        text-align: center;
        padding: 32px 16px 24px;
        animation: slideDown 0.6s ease-out;
    }
    .app-header h1 {
        font-size: 2.2rem;
        font-weight: 800;
        background: linear-gradient(135deg, #0D9488 0%, #0F766E 50%, #115E59 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 4px;
        letter-spacing: -0.5px;
    }
    .app-header .subtitle {
        font-size: 1rem;
        color: #475569;
        font-weight: 400;
        max-width: 520px;
        margin: 0 auto;
        line-height: 1.5;
    }

    /* ===== Card Base ===== */
    .ea-card {
        background: #FFFFFF;
        border-radius: 16px;
        padding: 24px;
        margin: 16px 0;
        box-shadow: 0 1px 3px rgba(0,0,0,0.06), 0 4px 12px rgba(0,0,0,0.04);
        border: 1px solid #E2E8F0;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        animation: fadeIn 0.4s ease-in;
    }
    .ea-card:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 16px rgba(0,0,0,0.08);
    }

    /* ===== Bold Statement Card ===== */
    .bold-statement-card {
        background: linear-gradient(135deg, #F0FDFA 0%, #CCFBF1 100%);
        border-left: 6px solid #0D9488;
        border-radius: 12px;
        padding: 28px 24px;
        margin: 24px 0;
        animation: slideIn 0.5s ease-out;
    }
    .bold-statement-card .bold-text {
        font-size: 1.25rem;
        font-weight: 700;
        color: #0F172A;
        line-height: 1.5;
        margin-bottom: 12px;
    }
    .bold-statement-card .legal-basis {
        font-size: 0.9rem;
        color: #475569;
        line-height: 1.5;
        font-style: italic;
    }

    /* ===== Tier Cards ===== */
    .tier-card {
        border-radius: 16px;
        padding: 24px;
        margin: 20px 0;
        animation: fadeIn 0.5s ease-in;
    }
    .tier-header {
        display: flex;
        align-items: center;
        gap: 10px;
        margin-bottom: 16px;
    }
    .tier-badge {
        padding: 6px 14px;
        border-radius: 8px;
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 0.8px;
        text-transform: uppercase;
    }
    .tier-reason {
        font-size: 0.9rem;
        color: #475569;
        margin-bottom: 16px;
        line-height: 1.5;
    }

    /* Tier 1 - Red */
    .tier-1 {
        background: linear-gradient(135deg, #FEF2F2 0%, #FEE2E2 100%);
        border: 1px solid #FECACA;
        border-left: 5px solid #EF4444;
    }
    .tier-1 .tier-badge {
        background: #EF4444;
        color: white;
    }

    /* Tier 2 - Orange */
    .tier-2 {
        background: linear-gradient(135deg, #FFF7ED 0%, #FFEDD5 100%);
        border: 1px solid #FED7AA;
        border-left: 5px solid #F97316;
    }
    .tier-2 .tier-badge {
        background: #F97316;
        color: white;
    }

    /* Tier 3 - Yellow */
    .tier-3 {
        background: linear-gradient(135deg, #FEFCE8 0%, #FEF9C3 100%);
        border: 1px solid #FDE68A;
        border-left: 5px solid #EAB308;
    }
    .tier-3 .tier-badge {
        background: #EAB308;
        color: white;
    }

    /* ===== Action Item ===== */
    .action-item {
        background: rgba(255,255,255,0.7);
        border-radius: 12px;
        padding: 16px;
        margin: 12px 0;
        border: 1px solid rgba(0,0,0,0.06);
    }
    .action-deadline {
        font-weight: 700;
        color: #0F172A;
        font-size: 0.95rem;
        margin-bottom: 6px;
    }
    .action-text {
        color: #1E293B;
        font-size: 0.9rem;
        line-height: 1.5;
        margin-bottom: 6px;
    }
    .action-why {
        color: #64748B;
        font-size: 0.82rem;
        line-height: 1.4;
        font-style: italic;
    }
    .action-how {
        color: #0D9488;
        font-size: 0.82rem;
        line-height: 1.4;
        font-weight: 500;
        margin-top: 4px;
    }

    /* ===== Prohibition Module ===== */
    .prohibition-card {
        background: #FFFFFF;
        border-radius: 16px;
        padding: 24px;
        margin: 20px 0;
        border: 1px solid #E2E8F0;
        box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    }
    .prohibition-title {
        font-size: 1.15rem;
        font-weight: 700;
        color: #0F172A;
        margin-bottom: 16px;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .prohibition-item {
        background: #FEF2F2;
        border-radius: 10px;
        padding: 14px 16px;
        margin: 10px 0;
        border-left: 4px solid #EF4444;
    }
    .prohibition-item .action-name {
        font-weight: 600;
        color: #991B1B;
        font-size: 0.9rem;
        margin-bottom: 4px;
    }
    .prohibition-item .explanation {
        color: #475569;
        font-size: 0.85rem;
        line-height: 1.4;
    }
    .prohibition-item .if-happens {
        color: #0D9488;
        font-size: 0.82rem;
        font-weight: 500;
        margin-top: 6px;
    }

    /* ===== Legal Aid Connector ===== */
    .legal-aid-card {
        background: linear-gradient(135deg, #F0FDFA 0%, #CCFBF1 100%);
        border-radius: 16px;
        padding: 24px;
        margin: 20px 0;
        border: 2px solid #14B8A6;
        animation: pulse-subtle 2s ease-in-out infinite;
    }
    .legal-aid-card .org-name {
        font-size: 1.1rem;
        font-weight: 700;
        color: #0F766E;
        margin-bottom: 8px;
    }
    .legal-aid-card .phone {
        font-size: 1.3rem;
        font-weight: 800;
        color: #0D9488;
        margin: 8px 0;
        letter-spacing: 0.5px;
    }
    .legal-aid-card .hours {
        font-size: 0.85rem;
        color: #475569;
        margin-bottom: 8px;
    }
    .legal-aid-card .what-to-say {
        background: rgba(255,255,255,0.6);
        border-radius: 10px;
        padding: 12px;
        margin-top: 12px;
        font-size: 0.85rem;
        color: #334155;
        line-height: 1.5;
    }
    .legal-aid-card .what-to-say strong {
        color: #0D9488;
    }

    /* ===== Rental Assistance ===== */
    .rental-assist-card {
        background: linear-gradient(135deg, #EFF6FF 0%, #DBEAFE 100%);
        border-radius: 16px;
        padding: 24px;
        margin: 20px 0;
        border: 1px solid #93C5FD;
    }
    .rental-assist-card .title {
        font-size: 1rem;
        font-weight: 700;
        color: #1E40AF;
        margin-bottom: 8px;
    }

    /* ===== Disclaimer ===== */
    .disclaimer-box {
        background: #F8FAFC;
        border: 1px solid #E2E8F0;
        border-radius: 10px;
        padding: 16px;
        margin: 24px 0;
        font-size: 0.8rem;
        color: #64748B;
        line-height: 1.5;
        text-align: center;
    }

    /* ===== Gate / CTA Buttons ===== */
    .gate-container {
        background: #FFFFFF;
        border-radius: 16px;
        padding: 32px 24px;
        margin: 24px 0;
        text-align: center;
        box-shadow: 0 2px 8px rgba(0,0,0,0.06);
        border: 1px solid #E2E8F0;
    }
    .gate-container .gate-text {
        font-size: 1rem;
        color: #334155;
        line-height: 1.6;
        margin-bottom: 24px;
        max-width: 540px;
        margin-left: auto;
        margin-right: auto;
    }

    /* ===== Emergency Banner ===== */
    .emergency-banner {
        background: linear-gradient(135deg, #FEF2F2 0%, #FEE2E2 100%);
        border: 2px solid #EF4444;
        border-radius: 16px;
        padding: 24px;
        margin: 20px 0;
        animation: pulse-red 1.5s ease-in-out infinite;
    }
    .emergency-banner h3 {
        color: #991B1B;
        font-weight: 700;
        margin-bottom: 12px;
    }

    /* ===== Hard Stop Banner ===== */
    .hard-stop-banner {
        background: linear-gradient(135deg, #FFF7ED 0%, #FFEDD5 100%);
        border: 2px solid #F97316;
        border-radius: 16px;
        padding: 24px;
        margin: 20px 0;
    }
    .hard-stop-banner h3 {
        color: #9A3412;
        font-weight: 700;
        margin-bottom: 12px;
    }

    /* ===== Notice Summary ===== */
    .notice-summary {
        background: #FFFFFF;
        border-radius: 16px;
        padding: 24px;
        margin: 20px 0;
        border: 1px solid #E2E8F0;
        box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    }
    .notice-type-label {
        font-size: 0.75rem;
        font-weight: 600;
        color: #0D9488;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 4px;
    }
    .notice-type-name {
        font-size: 1.15rem;
        font-weight: 700;
        color: #0F172A;
        margin-bottom: 12px;
    }
    .deadline-box {
        background: linear-gradient(135deg, #FEF2F2 0%, #FEE2E2 100%);
        border: 2px solid #EF4444;
        border-radius: 12px;
        padding: 16px;
        margin: 16px 0;
        text-align: center;
    }
    .deadline-label {
        font-size: 0.85rem;
        color: #475569;
        margin-bottom: 4px;
    }
    .deadline-date {
        font-size: 1.2rem;
        font-weight: 800;
        color: #DC2626;
    }

    /* ===== Acknowledgment Gate ===== */
    .ack-gate {
        background: linear-gradient(135deg, #FFF7ED 0%, #FFEDD5 100%);
        border: 2px solid #F97316;
        border-radius: 16px;
        padding: 28px 24px;
        margin: 24px 0;
        text-align: center;
    }
    .ack-gate p {
        font-size: 0.95rem;
        color: #431407;
        line-height: 1.6;
        margin-bottom: 20px;
    }

    /* ===== Demo Mode Badge ===== */
    .demo-badge {
        display: inline-block;
        background: #DBEAFE;
        color: #1E40AF;
        padding: 4px 12px;
        border-radius: 999px;
        font-size: 0.75rem;
        font-weight: 600;
        letter-spacing: 0.5px;
    }

    /* ===== Source Badge ===== */
    .source-badge {
        display: inline-block;
        background: #F1F5F9;
        color: #64748B;
        padding: 3px 10px;
        border-radius: 999px;
        font-size: 0.7rem;
        font-weight: 500;
        margin-top: 8px;
    }

    /* ===== Animations ===== */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(8px); }
        to { opacity: 1; transform: translateY(0); }
    }
    @keyframes slideDown {
        from { opacity: 0; transform: translateY(-20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    @keyframes slideIn {
        from { opacity: 0; transform: translateX(-20px); }
        to { opacity: 1; transform: translateX(0); }
    }
    @keyframes pulse-subtle {
        0%, 100% { box-shadow: 0 0 0 0 rgba(13,148,136,0.1); }
        50% { box-shadow: 0 0 0 6px rgba(13,148,136,0.05); }
    }
    @keyframes pulse-red {
        0%, 100% { box-shadow: 0 0 0 0 rgba(239,68,68,0.15); }
        50% { box-shadow: 0 0 0 6px rgba(239,68,68,0.08); }
    }

    /* ===== Responsive ===== */
    @media (max-width: 640px) {
        .app-header h1 { font-size: 1.6rem; }
        .bold-statement-card { padding: 20px 16px; }
        .bold-statement-card .bold-text { font-size: 1.1rem; }
        .tier-card { padding: 16px; }
        .legal-aid-card .phone { font-size: 1.1rem; }
    }

    /* ===== Streamlit Button Overrides ===== */
    .stButton > button {
        border-radius: 12px !important;
        font-weight: 600 !important;
        font-family: 'Inter', sans-serif !important;
        padding: 10px 24px !important;
        transition: all 0.2s ease !important;
    }
    .stButton > button:hover {
        transform: translateY(-1px) !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1) !important;
    }

    /* ===== Sidebar Styling ===== */
    [data-testid="stSidebar"] {
        background: #F8FAFC;
        border-right: 1px solid #E2E8F0;
    }
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] {
        font-family: 'Inter', sans-serif;
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)
