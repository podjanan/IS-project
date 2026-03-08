import streamlit as st
import numpy as np
import joblib
from tensorflow.keras.applications import MobileNetV2
from PIL import Image
import pandas as pd
from style import load_css
load_css()

st.set_page_config(page_title="Garbage Classification · NeuralVision", page_icon="♻️", layout="wide")

CARD  = "background:white; border:1px solid #ede9fe; border-radius:16px; padding:32px 36px; margin-bottom:22px; box-shadow:0 2px 16px rgba(124,58,237,0.06);"
TOP   = "border-top:3px solid #7c3aed;"
LABEL = "font-family:'Syne',sans-serif; font-size:0.7rem; font-weight:700; letter-spacing:0.15em; text-transform:uppercase; color:#7c3aed;"

# ── Hero ──────────────────────────────────────────────────────────────────
st.markdown(f"""
<div style="padding:48px 0 32px 0;">
    <span style="{LABEL}; background:#f5f3ff; padding:6px 16px; border-radius:50px; border:1px solid #ddd6fe;">Model 01 · Live Inference</span>
    <h1 style="font-family:'Syne',sans-serif; font-size:2.8rem; font-weight:800; color:#1e0a4a; margin:14px 0 14px 0; letter-spacing:-0.03em;">Garbage Classification</h1>
    <p style="font-size:1.05rem; color:#6b7280; max-width:560px; margin:0;">
        Upload a waste image and the ensemble model will classify it into one of six
        recyclable categories with full probability breakdown.
    </p>
</div>
""", unsafe_allow_html=True)

# ── Load Models ───────────────────────────────────────────────────────────
@st.cache_resource
def load_models():
    ensemble_model = joblib.load("models/garbage_ensemble_model.pkl")
    feature_extractor = MobileNetV2(weights="imagenet", include_top=False, pooling="avg", input_shape=(224,224,3))
    return ensemble_model, feature_extractor

ensemble, base_model = load_models()
class_names = ["cardboard","glass","metal","paper","plastic","trash"]
class_icons = {"cardboard":"📦","glass":"🫙","metal":"🥫","paper":"📰","plastic":"🧴","trash":"🗑️"}

# ── Upload ────────────────────────────────────────────────────────────────
st.markdown(f'<div style="{CARD} {TOP}">', unsafe_allow_html=True)
st.markdown(f'<span style="{LABEL}">Input</span>', unsafe_allow_html=True)
st.markdown('<h2 style="font-family:\'Syne\',sans-serif; color:#1e0a4a; margin:8px 0 16px 0;">Upload Waste Image</h2>', unsafe_allow_html=True)
uploaded_file = st.file_uploader("Drag & drop or browse — JPG, JPEG, PNG", type=["jpg","jpeg","png"], label_visibility="collapsed")
st.markdown("</div>", unsafe_allow_html=True)

# ── Prediction ────────────────────────────────────────────────────────────
if uploaded_file is not None:
    col1, col2 = st.columns([1,1], gap="large")

    with col1:
        st.markdown(f'<div style="{CARD} {TOP}">', unsafe_allow_html=True)
        st.markdown(f'<span style="{LABEL}">Input Image</span>', unsafe_allow_html=True)
        img = Image.open(uploaded_file).convert("RGB")
        st.image(img, caption="Uploaded Image", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown(f'<div style="{CARD} {TOP}">', unsafe_allow_html=True)
        st.markdown(f'<span style="{LABEL}">Result</span>', unsafe_allow_html=True)

        img_resized = img.resize((224,224))
        img_array   = np.array(img_resized)/255.0
        img_array   = np.expand_dims(img_array, axis=0)
        feature     = base_model.predict(img_array)
        prediction  = ensemble.predict(feature)
        probs       = ensemble.predict_proba(feature)
        pred_class  = class_names[prediction[0]]
        confidence  = float(np.max(probs))
        icon        = class_icons.get(pred_class, "♻️")

        st.markdown(f"""
        <div style="margin:16px 0 24px 0;">
            <div style="font-size:3rem; margin-bottom:12px;">{icon}</div>
            <div style="font-family:'Syne',sans-serif; font-size:1.8rem; font-weight:700; color:#1e0a4a;">{pred_class.capitalize()}</div>
            <div style="font-size:1.05rem; color:#7c3aed; font-weight:500; margin-top:6px;">Confidence: {round(confidence*100,2)}%</div>
        </div>
        """, unsafe_allow_html=True)

        st.progress(int(confidence*100))

        st.markdown(f'<div style="margin-top:22px;"><span style="{LABEL}">Top Predictions</span></div>', unsafe_allow_html=True)
        top3 = probs[0].argsort()[-3:][::-1]
        for idx in top3:
            pct = probs[0][idx]*100
            bar_color = "#7c3aed" if idx == prediction[0] else "#e9d5ff"
            txt_color = "#2d1167" if idx == prediction[0] else "#9ca3af"
            st.markdown(f"""
            <div style="display:flex; align-items:center; gap:12px; margin-bottom:10px;">
                <div style="width:110px; font-size:0.85rem; color:{txt_color};">
                    {class_icons.get(class_names[idx],'')} {class_names[idx].capitalize()}</div>
                <div style="flex:1; background:#f3f4f6; border-radius:99px; height:6px;">
                    <div style="width:{pct:.1f}%; background:{bar_color}; border-radius:99px; height:6px;"></div>
                </div>
                <div style="width:48px; text-align:right; font-size:0.82rem; color:#9ca3af;">{pct:.1f}%</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

    # ── Full Probability Chart ─────────────────────────────────────────────
    st.markdown(f'<div style="{CARD} {TOP}">', unsafe_allow_html=True)
    st.markdown(f'<span style="{LABEL}">Analysis</span>', unsafe_allow_html=True)
    st.markdown('<h2 style="font-family:\'Syne\',sans-serif; color:#1e0a4a; margin:8px 0 20px 0;">Full Probability Breakdown</h2>', unsafe_allow_html=True)

    df = pd.DataFrame({
        "Category": [f"{class_icons.get(c,'')} {c.capitalize()}" for c in class_names],
        "Probability": probs[0]
    })
    st.bar_chart(df.set_index("Category"), height=280, color="#7c3aed")
    st.markdown("</div>", unsafe_allow_html=True)

else:
    st.markdown(f"""
    <div style="{CARD} text-align:center; padding:64px 40px;">
        <div style="font-size:3rem; margin-bottom:16px; opacity:0.3;">♻️</div>
        <div style="font-family:'Syne',sans-serif; font-size:1.1rem; font-weight:700; color:#9ca3af; margin-bottom:8px;">No image uploaded yet</div>
        <p style="color:#d1d5db; margin:0; font-size:0.88rem;">Upload a JPG or PNG of any waste item above to get started.</p>
    </div>
    """, unsafe_allow_html=True)
