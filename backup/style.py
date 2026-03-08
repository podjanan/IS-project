import streamlit as st

def load_css():
    st.markdown("""
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap');
    
    /* font */
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }

    /* background */
    .stApp {
        background: linear-gradient(135deg,#f5f3ff,#ede9fe);
    }

    /* FIX TEXT COLOR */
    h1, h2, h3, h4, h5, h6 {
        color: #4c1d95 !important;
    }

    p, li, span, label {
        color: #1f2937 !important;
    }

    /* card */
    .card {
        background: white;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.08);
        margin-bottom: 25px;
    }

    /* metric box */
    .metric-box {
        background: #faf5ff;
        padding: 20px;
        border-radius: 12px;
        border-left: 6px solid #7c3aed;
        margin-bottom: 20px;
    }

    /* sidebar */
    section[data-testid="stSidebar"] {
        background: #1e1b4b;
    }

    section[data-testid="stSidebar"] * {
        color: white !important;
    }
    
    .prediction{
    font-size:28px !important;
    font-weight:bold !important;
    color:#111827 !important;
    }

    .confidence{
    font-size:20px !important;
    color:#374151 !important;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <style>

    /* Table style */
    table {
        width: 100%;
        border-collapse: collapse;
    }

    thead tr th {
        background-color: #7c3aed;
        color: white !important;
        padding: 10px;
    }

    tbody tr td {
        background-color: #ffffff;
        color: #111827 !important;
        padding: 10px;
        border-bottom: 1px solid #e5e7eb;
    }

    /* alternating row color */
    tbody tr:nth-child(even) {
        background-color: #f9fafb;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <style>

    /* File uploader container */
    [data-testid="stFileUploader"]{
        background:#ffffff !important;
        border:2px dashed #7c3aed !important;
        border-radius:12px !important;
        padding:20px !important;
    }

    /* Drag area */
    [data-testid="stFileUploaderDropzone"]{
        background:#f9fafb !important;
        border-radius:10px !important;
    }

    /* Upload text */
    [data-testid="stFileUploaderDropzone"] span{
        color:#374151 !important;
        font-weight:500 !important;
    }

    /* Browse button */
    [data-testid="stBaseButton-secondary"]{
        background:#7c3aed !important;
        color:white !important;
        border-radius:8px !important;
    }

    </style>
    """, unsafe_allow_html=True)