import streamlit as st

def load_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700;800&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,400&display=swap');

    html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }

    .stApp {
        background: #faf9ff;
        background-image: radial-gradient(ellipse 80% 50% at 50% -5%, rgba(124,58,237,0.07) 0%, transparent 65%);
    }

    h1,h2,h3,h4,h5,h6 { font-family:'Syne',sans-serif !important; letter-spacing:-0.02em !important; }
    h1 { color:#1e0a4a !important; font-weight:800 !important; }
    h2 { color:#2d1167 !important; font-weight:700 !important; }
    h3 { color:#4c1d95 !important; font-weight:600 !important; }
    p,li,span,label { color:#4b5563 !important; line-height:1.75 !important; }

    /* ── Sidebar: Dark Navy ── */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f0a1e 0%, #1a0d35 100%) !important;
        border-right: 1px solid rgba(124,58,237,0.2) !important;
        box-shadow: 4px 0 32px rgba(0,0,0,0.3) !important;
    }
    section[data-testid="stSidebar"] * { color: #c4b5fd !important; }
    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 { color: #ede9fe !important; }

    /* Nav links */
    section[data-testid="stSidebar"] a {
        color: #a78bfa !important;
        font-weight: 500 !important;
        border-radius: 8px !important;
        transition: all 0.15s ease !important;
        padding: 6px 12px !important;
    }
    section[data-testid="stSidebar"] a:hover {
        background: rgba(124,58,237,0.15) !important;
        color: #ede9fe !important;
    }
    /* Active page highlight */
    section[data-testid="stSidebar"] [aria-selected="true"],
    section[data-testid="stSidebar"] [aria-current="page"] {
        background: linear-gradient(135deg, rgba(124,58,237,0.35), rgba(109,40,217,0.25)) !important;
        border-left: 3px solid #a78bfa !important;
        border-radius: 0 8px 8px 0 !important;
        color: #ffffff !important;
        font-weight: 700 !important;
    }

    .stProgress > div > div { background:linear-gradient(90deg,#7c3aed,#a78bfa) !important; border-radius:99px !important; }
    .stProgress > div { background:#ede9fe !important; border-radius:99px !important; height:8px !important; }

    [data-testid="stFileUploader"],
    [data-testid="stFileUploader"] > div,
    [data-testid="stFileUploader"] section,
    [data-testid="stFileDropzone"],
    [data-testid="stFileDropzone"] > div { background: #ffffff !important; }
    [data-testid="stFileUploader"] section,
    [data-testid="stFileDropzone"] { border: 1.5px dashed #a78bfa !important; border-radius: 14px !important; padding: 20px !important; }
    [data-testid="stFileUploader"] span,
    [data-testid="stFileUploader"] p,
    [data-testid="stFileUploader"] small,
    [data-testid="stFileDropzone"] span,
    [data-testid="stFileDropzone"] p { color: #6b7280 !important; }
    [data-testid="stFileUploader"] svg { fill: #a78bfa !important; }
    /* Uploaded file name tag */
    [data-testid="stFileUploader"] [data-testid="stFileUploaderFile"],
    [data-testid="stFileUploader"] [data-testid="stFileUploaderFileName"],
    [data-testid="stFileUploader"] li,
    [data-testid="stFileUploader"] [class*="uploadedFile"] {
        background: #f5f3ff !important;
        border: 1px solid #ddd6fe !important;
        border-radius: 8px !important;
        color: #4c1d95 !important;
    }
    [data-testid="stFileUploader"] [class*="uploadedFileName"],
    [data-testid="stFileUploader"] li span,
    [data-testid="stFileUploader"] li p { color: #4c1d95 !important; }
    [data-testid="stBaseButton-secondary"] { background:linear-gradient(135deg,#7c3aed,#6d28d9) !important; color:white !important; border:none !important; border-radius:8px !important; }

    table { width:100%; border-collapse:collapse; }
    thead tr th { background:#7c3aed !important; color:white !important; padding:12px 16px !important; font-family:'Syne',sans-serif !important; font-size:0.8rem !important; text-transform:uppercase !important; letter-spacing:0.08em !important; }
    tbody tr td { background:#ffffff !important; color:#374151 !important; padding:12px 16px !important; border-bottom:1px solid #f3f4f6 !important; }
    tbody tr:nth-child(even) td { background:#faf9ff !important; }
    tbody tr:hover td { background:#f5f3ff !important; }

    .prediction { font-family:'Syne',sans-serif !important; font-size:1.8rem !important; font-weight:700 !important; color:#1e0a4a !important; }
    .confidence { font-size:1.05rem !important; color:#7c3aed !important; font-weight:500 !important; }

    code { background:#ede9fe !important; color:#6d28d9 !important; padding:2px 8px !important; border-radius:6px !important; font-size:0.88em !important; }
    </style>
    """, unsafe_allow_html=True)
