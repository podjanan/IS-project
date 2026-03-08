import streamlit as st
import tensorflow as tf
import numpy as np
import cv2
from PIL import Image
from style import load_css
load_css()

st.set_page_config(page_title="Scene Classification · NeuralVision", page_icon="🌄", layout="wide")

CARD  = "background:white; border:1px solid #ede9fe; border-radius:16px; padding:32px 36px; margin-bottom:22px; box-shadow:0 2px 16px rgba(124,58,237,0.06);"
TOP   = "border-top:3px solid #7c3aed;"
LABEL = "font-family:'Syne',sans-serif; font-size:0.7rem; font-weight:700; letter-spacing:0.15em; text-transform:uppercase; color:#7c3aed;"

# ── Hero ──────────────────────────────────────────────────────────────────
st.markdown(f"""
<div style="padding:48px 0 32px 0;">
    <span style="{LABEL}; background:#f5f3ff; padding:6px 16px; border-radius:50px; border:1px solid #ddd6fe;">Model 02 · Live Inference</span>
    <h1 style="font-family:'Syne',sans-serif; font-size:2.8rem; font-weight:800; color:#1e0a4a; margin:14px 0 14px 0; letter-spacing:-0.03em;">Natural Scene Classification</h1>
    <p style="font-size:1.05rem; color:#6b7280; max-width:580px; margin:0;">
        Upload a scene image. The neural network will predict the environment type,
        show top-3 confidence scores, and generate a Grad-CAM explainability heatmap.
    </p>
</div>
""", unsafe_allow_html=True)

# ── Load Model ────────────────────────────────────────────────────────────
@st.cache_resource
def load_model():
    return tf.keras.models.load_model("models/intel_nn_model_93_9.h5")

model = load_model()
class_names = ["buildings","forest","glacier","mountain","sea","street"]
class_icons = {"buildings":"🏙️","forest":"🌲","glacier":"🏔️","mountain":"⛰️","sea":"🌊","street":"🛣️"}

# ── Grad-CAM ──────────────────────────────────────────────────────────────
def make_gradcam_heatmap(img_array, model, last_conv_layer_name="Conv_1"):
    base_model = model.get_layer("mobilenetv2_1.00_224")
    x = base_model.output
    x = model.layers[1](x)
    x = model.layers[2](x)
    x = model.layers[3](x)
    predictions = model.layers[4](x)
    grad_model = tf.keras.models.Model(
        inputs=base_model.input,
        outputs=[base_model.get_layer(last_conv_layer_name).output, predictions]
    )
    with tf.GradientTape() as tape:
        conv_outputs, preds = grad_model(img_array)
        pred_index    = tf.argmax(preds[0])
        class_channel = preds[:, pred_index]
    grads        = tape.gradient(class_channel, conv_outputs)
    pooled_grads = tf.reduce_mean(grads, axis=(0,1,2))
    conv_outputs = conv_outputs[0]
    heatmap      = conv_outputs @ pooled_grads[..., tf.newaxis]
    heatmap      = tf.squeeze(heatmap)
    heatmap      = tf.maximum(heatmap, 0) / tf.reduce_max(heatmap)
    return heatmap.numpy()

# ── Upload ────────────────────────────────────────────────────────────────
st.markdown(f'<div style="{CARD} {TOP}">', unsafe_allow_html=True)
st.markdown(f'<span style="{LABEL}">Input</span>', unsafe_allow_html=True)
st.markdown('<h2 style="font-family:\'Syne\',sans-serif; color:#1e0a4a; margin:8px 0 16px 0;">Upload Scene Image</h2>', unsafe_allow_html=True)
uploaded_file = st.file_uploader("Drag & drop or browse — JPG, JPEG, PNG", type=["jpg","jpeg","png"], label_visibility="collapsed")
st.markdown("</div>", unsafe_allow_html=True)

# ── Prediction ────────────────────────────────────────────────────────────
if uploaded_file:
    img = Image.open(uploaded_file).convert("RGB").resize((224,224))

    col1, col2 = st.columns([1,1], gap="large")

    with col1:
        st.markdown(f'<div style="{CARD} {TOP}">', unsafe_allow_html=True)
        st.markdown(f'<span style="{LABEL}">Input Image</span>', unsafe_allow_html=True)
        st.image(img, caption="Uploaded Image", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    img_array  = np.array(img)/255.0
    img_array  = np.expand_dims(img_array, axis=0)
    prediction = model.predict(img_array)[0]
    top3       = prediction.argsort()[-3:][::-1]
    pred_name  = class_names[top3[0]]
    icon       = class_icons.get(pred_name, "🌄")

    with col2:
        st.markdown(f'<div style="{CARD} {TOP}">', unsafe_allow_html=True)
        st.markdown(f'<span style="{LABEL}">Result</span>', unsafe_allow_html=True)
        st.markdown(f"""
        <div style="margin:16px 0 24px 0;">
            <div style="font-size:3rem; margin-bottom:12px;">{icon}</div>
            <div style="font-family:'Syne',sans-serif; font-size:1.8rem; font-weight:700; color:#1e0a4a;">{pred_name.capitalize()}</div>
            <div style="font-size:1.05rem; color:#7c3aed; font-weight:500; margin-top:6px;">Confidence: {prediction[top3[0]]*100:.2f}%</div>
        </div>
        """, unsafe_allow_html=True)

        st.progress(int(prediction[top3[0]]*100))

        st.markdown(f'<div style="margin-top:22px;"><span style="{LABEL}">Top 3 Predictions</span></div>', unsafe_allow_html=True)
        for rank, idx in enumerate(top3):
            pct = prediction[idx]*100
            bar_color = "#7c3aed" if rank == 0 else "#e9d5ff"
            txt_color = "#2d1167" if rank == 0 else "#9ca3af"
            st.markdown(f"""
            <div style="display:flex; align-items:center; gap:12px; margin-bottom:10px;">
                <div style="width:114px; font-size:0.85rem; color:{txt_color};">
                    {class_icons.get(class_names[idx],'')} {class_names[idx].capitalize()}</div>
                <div style="flex:1; background:#f3f4f6; border-radius:99px; height:6px;">
                    <div style="width:{pct:.1f}%; background:{bar_color}; border-radius:99px; height:6px;"></div>
                </div>
                <div style="width:52px; text-align:right; font-size:0.82rem; color:#9ca3af;">{pct:.1f}%</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

    # ── Grad-CAM ──────────────────────────────────────────────────────────
    st.markdown(f'<div style="{CARD} {TOP}">', unsafe_allow_html=True)
    st.markdown(f'<span style="{LABEL}">Explainability</span>', unsafe_allow_html=True)
    st.markdown('<h2 style="font-family:\'Syne\',sans-serif; color:#1e0a4a; margin:8px 0 20px 0;">Grad-CAM Heatmap</h2>', unsafe_allow_html=True)

    heatmap = make_gradcam_heatmap(img_array, model)
    img_cv  = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    heatmap = cv2.resize(heatmap,(224,224))
    heatmap = np.uint8(255*heatmap)
    heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)
    overlay = heatmap*0.4 + img_cv
    result  = cv2.cvtColor(overlay.astype("uint8"), cv2.COLOR_BGR2RGB)

    gc1, gc2 = st.columns([1.4, 1], gap="large")

    with gc1:
        st.image(result, caption="Grad-CAM Visualization", use_container_width=True)

    with gc2:
        st.markdown('<div style="font-family:\'Syne\',sans-serif; font-weight:700; color:#2d1167; font-size:1rem; margin-bottom:16px;">Heatmap Legend</div>', unsafe_allow_html=True)
        for bg, border, color, emoji, label, desc in [
            ("#fef2f2","#fecaca","#dc2626","🔴","Red / Yellow","Highest influence — the model's attention is focused here. These regions most strongly drove the final prediction."),
            ("#f0fdf4","#bbf7d0","#16a34a","🟢","Green","Moderate influence on the prediction output."),
            ("#eff6ff","#bfdbfe","#2563eb","🔵","Blue","Minimal contribution — background or irrelevant areas."),
        ]:
            st.markdown(f"""
            <div style="background:{bg}; border:1px solid {border}; border-radius:12px; padding:16px 20px; margin-bottom:12px;">
                <div style="font-family:'Syne',sans-serif; font-weight:700; color:{color}; margin-bottom:6px;">{emoji} {label}</div>
                <p style="margin:0; font-size:0.85rem; color:#6b7280;">{desc}</p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown(f"""
    <div style="background:#f5f3ff; border:1px solid #ddd6fe; border-left:3px solid #7c3aed; border-radius:10px; padding:18px 22px; margin-top:16px;">
        <p style="margin:0; font-size:0.88rem; color:#4b5563;">
            <strong style="color:#2d1167;">Scene examples:</strong><br>
            🏙️ Buildings → attention on structures and facades &nbsp;·&nbsp;
            🌲 Forest → attention on tree canopy &nbsp;·&nbsp;
            🌊 Sea → attention on water surface
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

else:
    st.markdown(f"""
    <div style="{CARD} text-align:center; padding:64px 40px;">
        <div style="font-size:3rem; margin-bottom:16px; opacity:0.3;">🌄</div>
        <div style="font-family:'Syne',sans-serif; font-size:1.1rem; font-weight:700; color:#9ca3af; margin-bottom:8px;">No image uploaded yet</div>
        <p style="color:#d1d5db; margin:0; font-size:0.88rem;">Upload a JPG or PNG of any natural or urban scene above to run inference.</p>
    </div>
    """, unsafe_allow_html=True)
