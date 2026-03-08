import streamlit as st

st.set_page_config(page_title="Intelligent system - Project", page_icon="⬡", layout="wide")

from style import load_css
load_css()

# ── Reusable inline-style components ──────────────────────────────────────
CARD = "background:white; border:1px solid #ede9fe; border-radius:16px; padding:32px 36px; margin-bottom:22px; box-shadow:0 2px 16px rgba(124,58,237,0.06);"
CARD_TOP = "border-top:3px solid #7c3aed;"
LABEL = "font-family:'Syne',sans-serif; font-size:0.7rem; font-weight:700; letter-spacing:0.15em; text-transform:uppercase; color:#7c3aed; display:block; margin-bottom:8px;"
TAG_STYLE = "display:inline-block; background:#f5f3ff; border:1px solid #ddd6fe; color:#6d28d9; font-size:0.75rem; font-weight:600; padding:4px 12px; border-radius:50px; margin:3px 3px 3px 0; letter-spacing:0.04em; text-transform:uppercase;"
HIGHLIGHT = "background:#f5f3ff; border:1px solid #ddd6fe; border-left:3px solid #7c3aed; border-radius:10px; padding:18px 22px; margin:14px 0;"

# ── Hero ──────────────────────────────────────────────────────────────────
st.markdown(f"""
<div style="padding:60px 0 40px 0; text-align:center;">
    <span style="{LABEL}; display:inline-block; background:#f5f3ff; padding:6px 18px; border-radius:50px; border:1px solid #ddd6fe; margin-bottom:20px;">AI Research Platform</span>
    <h1 style="font-family:'Syne',sans-serif; font-size:3.4rem; font-weight:800; color:#1e0a4a; margin:0 0 18px 0; letter-spacing:-0.03em;">Intelligent system - Project</h1>
    <p style="font-size:1.15rem; color:#6b7280; max-width:540px; margin:0 auto 32px auto; line-height:1.7;">
        Enterprise-grade image classification powered by deep learning.<br>Two specialized models. One unified platform.
    </p>
    <div>
        <span style="{TAG_STYLE}">MobileNetV2</span>
        <span style="{TAG_STYLE}">Ensemble Learning</span>
        <span style="{TAG_STYLE}">Grad-CAM XAI</span>
        <span style="{TAG_STYLE}">Transfer Learning</span>
        <span style="{TAG_STYLE}">Real-time Inference</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Stats Row ─────────────────────────────────────────────────────────────
c1, c2, c3, c4 = st.columns(4)
for col, (num, lbl, color) in zip([c1,c2,c3,c4], [
    ("93.9%", "Neural Network Accuracy", "#7c3aed"),
    ("82%",   "Ensemble Model Accuracy",  "#6d28d9"),
    ("6",     "Waste Categories",          "#4f46e5"),
    ("6",     "Scene Categories",          "#7c3aed"),
]):
    with col:
        st.markdown(f"""
        <div style="{CARD} {CARD_TOP} text-align:center; padding:24px 16px;">
            <div style="font-family:'Syne',sans-serif; font-size:2.2rem; font-weight:800; color:{color}; letter-spacing:-0.03em;">{num}</div>
            <div style="font-size:0.75rem; color:#9ca3af; text-transform:uppercase; letter-spacing:0.08em; margin-top:4px;">{lbl}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Model Cards ───────────────────────────────────────────────────────────
col_a, col_b = st.columns(2, gap="large")

with col_a:
    st.markdown(f"""
    <div style="{CARD} border-top:3px solid #8b5cf6; min-height:300px;">
        <span style="{LABEL}">Model 01 · Ensemble Learning</span>
        <h2 style="font-family:'Syne',sans-serif; color:#1e0a4a; margin:6px 0 12px 0;">Garbage Classification</h2>
        <p style="color:#6b7280; margin-bottom:18px; font-size:0.95rem;">
            Classifies waste into 6 recyclable categories using an ensemble of Random Forest,
            SVM, and XGBoost with MobileNetV2 feature extraction.
        </p>
        <span style="{TAG_STYLE}">Random Forest</span>
        <span style="{TAG_STYLE}">SVM</span>
        <span style="{TAG_STYLE}">XGBoost</span>
        <span style="{TAG_STYLE}">Soft Voting</span>
        <div style="margin-top:22px; display:flex; align-items:center; gap:14px;">
            <div style="font-family:'Syne',sans-serif; font-size:2rem; font-weight:800; color:#7c3aed;">82%</div>
            <div style="font-size:0.78rem; color:#9ca3af; line-height:1.5;">Ensemble<br>Accuracy</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_b:
    st.markdown(f"""
    <div style="{CARD} border-top:3px solid #6d28d9; min-height:300px;">
        <span style="{LABEL}">Model 02 · Deep Learning</span>
        <h2 style="font-family:'Syne',sans-serif; color:#1e0a4a; margin:6px 0 12px 0;">Natural Scene Recognition</h2>
        <p style="color:#6b7280; margin-bottom:18px; font-size:0.95rem;">
            Recognizes 6 types of natural and urban environments using a fine-tuned
            MobileNetV2 neural network with Grad-CAM explainability.
        </p>
        <span style="{TAG_STYLE}">MobileNetV2</span>
        <span style="{TAG_STYLE}">Transfer Learning</span>
        <span style="{TAG_STYLE}">Grad-CAM</span>
        <span style="{TAG_STYLE}">Top-3 Predictions</span>
        <div style="margin-top:22px; display:flex; align-items:center; gap:14px;">
            <div style="font-family:'Syne',sans-serif; font-size:2rem; font-weight:800; color:#6d28d9;">93.9%</div>
            <div style="font-size:0.78rem; color:#9ca3af; line-height:1.5;">Neural Network<br>Accuracy</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ── Evaluation Metrics ────────────────────────────────────────────────────
st.markdown(f"""
<div style="{CARD} {CARD_TOP}">
    <span style="{LABEL}">Evaluation</span>
    <h2 style="font-family:'Syne',sans-serif; color:#1e0a4a; margin:6px 0 24px 0;">Performance Metrics</h2>
""", unsafe_allow_html=True)

m1, m2 = st.columns(2, gap="medium")
with m1:
    st.markdown(f"""
    <div style="{HIGHLIGHT}">
        <div style="font-family:'Syne',sans-serif; font-weight:700; color:#4c1d95; margin-bottom:8px; font-size:1rem;">📊 Accuracy</div>
        <p style="margin:0; font-size:0.92rem; color:#4b5563;">
            Percentage of images correctly classified by the model.<br><br>
            <code style="background:#ede9fe; color:#6d28d9; padding:3px 8px; border-radius:6px; font-size:0.85rem;">Accuracy = Correct Predictions ÷ Total</code><br><br>
            93 correct out of 100 → <strong style="color:#7c3aed;">93% accuracy</strong>
        </p>
    </div>
    """, unsafe_allow_html=True)

with m2:
    st.markdown(f"""
    <div style="{HIGHLIGHT}">
        <div style="font-family:'Syne',sans-serif; font-weight:700; color:#4c1d95; margin-bottom:8px; font-size:1rem;">📉 Loss Function</div>
        <p style="margin:0; font-size:0.92rem; color:#4b5563;">
            Measures the gap between predicted probabilities and true labels.<br><br>
            <code style="background:#ede9fe; color:#6d28d9; padding:3px 8px; border-radius:6px; font-size:0.85rem;">Categorical Crossentropy</code><br><br>
            Lower loss = better model. Optimizer minimizes this during training.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ── Confusion Matrix ──────────────────────────────────────────────────────
st.markdown(f"""
<div style="{CARD} {CARD_TOP}">
    <span style="{LABEL}">Diagnostics</span>
    <h2 style="font-family:'Syne',sans-serif; color:#1e0a4a; margin:6px 0 14px 0;">Confusion Matrix</h2>
    <p style="color:#6b7280; margin-bottom:20px;">
        Compares <strong style="color:#1e0a4a;">actual labels</strong> vs <strong style="color:#1e0a4a;">predicted labels</strong>
        to reveal classification errors across all classes.
    </p>
</div>
""", unsafe_allow_html=True)

import pandas as pd
df_cm = pd.DataFrame({
    "Glass (Pred)":   [50, 4, 1],
    "Paper (Pred)":   [3, 48, 2],
    "Plastic (Pred)": [2, 3, 52],
}, index=["Glass (Actual)", "Paper (Actual)", "Plastic (Actual)"])
st.dataframe(df_cm, use_container_width=True)

st.markdown(f"""
<div style="{HIGHLIGHT} margin-top:16px;">
    <p style="margin:0; font-size:0.9rem; color:#4b5563;">
        ✦ Identify classes frequently confused with each other &nbsp;·&nbsp;
        ✦ Pinpoint systematic errors &nbsp;·&nbsp;
        ✦ Assess prediction balance across all categories
    </p>
</div>
""", unsafe_allow_html=True)

# ── Grad-CAM ──────────────────────────────────────────────────────────────
st.markdown(f"""
<div style="{CARD} {CARD_TOP} margin-top:22px;">
    <span style="{LABEL}">Explainability</span>
    <h2 style="font-family:'Syne',sans-serif; color:#1e0a4a; margin:6px 0 14px 0;">Grad-CAM · Explainable AI</h2>
    <p style="color:#6b7280; margin-bottom:24px;">
        Deep learning models are often <strong style="color:#1e0a4a;">black-box systems</strong>.
        Gradient-weighted Class Activation Mapping makes predictions interpretable by highlighting
        the image regions that influenced the model's decision.
    </p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")
with col1:
    for n, title, desc in [
        ("01", "Forward Pass",         "Input image is passed through the full neural network to generate a prediction."),
        ("02", "Gradient Computation", "Gradients are computed with respect to the last convolutional feature maps."),
        ("03", "Heatmap Generation",   "Pooled gradients weight the feature maps to produce a spatial importance map."),
        ("04", "Overlay Visualization","Heatmap is upsampled and superimposed on the original image."),
    ]:
        st.markdown(f"""
        <div style="display:flex; gap:16px; align-items:flex-start; padding:16px 0; border-bottom:1px solid #f3f4f6;">
            <div style="font-family:'Syne',sans-serif; font-size:1.4rem; font-weight:800; color:#ddd6fe; min-width:36px; line-height:1;">{n}</div>
            <div>
                <div style="font-family:'Syne',sans-serif; font-weight:700; color:#2d1167; font-size:0.95rem; margin-bottom:4px;">{title}</div>
                <div style="font-size:0.87rem; color:#6b7280;">{desc}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

with col2:
    for bg, border, emoji, label, color, desc in [
        ("rgba(124,58,237,0.05)", "#ddd6fe", "🔴", "Red / Yellow", "#7c3aed", "Highest influence — model focuses most attention here"),
        ("rgba(124,58,237,0.03)", "#ede9fe", "🟢", "Green",        "#8b5cf6", "Moderate influence on the final prediction"),
        ("rgba(124,58,237,0.02)", "#f5f3ff", "🔵", "Blue",         "#a78bfa", "Minimal influence — background or irrelevant regions"),
    ]:
        st.markdown(f"""
        <div style="background:{bg}; border:1px solid {border}; border-radius:12px; padding:18px 22px; margin-bottom:12px;">
            <div style="font-family:'Syne',sans-serif; font-weight:700; color:{color}; margin-bottom:6px;">{emoji} {label}</div>
            <p style="margin:0; font-size:0.87rem; color:#6b7280;">{desc}</p>
        </div>
        """, unsafe_allow_html=True)

# ── Use Cases ─────────────────────────────────────────────────────────────
st.markdown(f"""
<div style="{CARD} {CARD_TOP} margin-top:22px;">
    <span style="{LABEL}">Applications</span>
    <h2 style="font-family:'Syne',sans-serif; color:#1e0a4a; margin:6px 0 24px 0;">Real-World Use Cases</h2>
</div>
""", unsafe_allow_html=True)

cases = [
    ("♻️", "Waste Management",         "#7c3aed", "Automated sorting lines for recycling facilities and smart bin systems."),
    ("🌍", "Environmental Monitoring",  "#6d28d9", "Scene classification for satellite imagery and geographic surveys."),
    ("🚗", "Autonomous Systems",        "#5b21b6", "Environment recognition for navigation in robotics and autonomous vehicles."),
    ("🏙️", "Smart City",               "#7c3aed", "Urban scene understanding for infrastructure planning and monitoring."),
    ("🏥", "Medical Imaging",           "#6d28d9", "Grad-CAM is widely applied to interpret diagnostic AI in radiology."),
    ("🔬", "CV Research",               "#5b21b6", "Benchmark platform for testing new architectures and explainability methods."),
]

row1 = st.columns(3, gap="medium")
row2 = st.columns(3, gap="medium")
for col, (icon, title, color, desc) in zip(list(row1)+list(row2), cases):
    with col:
        st.markdown(f"""
        <div style="background:#faf9ff; border:1px solid #ede9fe; border-top:3px solid {color}; border-radius:12px; padding:22px; margin-bottom:16px;">
            <div style="font-size:1.8rem; margin-bottom:10px;">{icon}</div>
            <div style="font-family:'Syne',sans-serif; font-weight:700; color:#2d1167; font-size:0.95rem; margin-bottom:6px;">{title}</div>
            <p style="margin:0; font-size:0.85rem; color:#6b7280;">{desc}</p>
        </div>
        """, unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────
st.markdown("""
<div style="text-align:center; padding:40px 0 20px 0; border-top:1px solid #f3f4f6; margin-top:20px;">
    <p style="font-size:0.78rem; color:#d1d5db; letter-spacing:0.06em; text-transform:uppercase;">
        NeuralVision AI Platform · Built with TensorFlow, Streamlit &amp; Scikit-learn
    </p>
</div>
""", unsafe_allow_html=True)
