import streamlit as st
import numpy as np
import joblib
from tensorflow.keras.applications import MobileNetV2
from PIL import Image
import pandas as pd
from style import load_css
load_css()

# ===============================
# Page Config
# ===============================
st.set_page_config(
    page_title="Garbage Classification",
    page_icon="♻️",
    layout="wide"
)

# ===============================
# Custom CSS (with !important)
# ===============================


# ===============================
# Header
# ===============================
st.title("Garbage Classification ♻️")
st.write("AI-based Waste Image Classification using Ensemble Machine Learning")

# ===============================
# Load Models
# ===============================
@st.cache_resource
def load_models():
    ensemble_model = joblib.load("models/garbage_ensemble_model.pkl")

    feature_extractor = MobileNetV2(
        weights="imagenet",
        include_top=False,
        pooling="avg",
        input_shape=(224,224,3)
    )

    return ensemble_model, feature_extractor

ensemble, base_model = load_models()

class_names = ["cardboard","glass","metal","paper","plastic","trash"]

# ===============================
# Upload Section
# ===============================
st.markdown("<div class='card'>", unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "Upload a garbage image",
    type=["jpg","jpeg","png"]
)

st.markdown("</div>", unsafe_allow_html=True)

# ===============================
# Prediction
# ===============================
if uploaded_file is not None:

    col1, col2 = st.columns([1,1])

    # ===============================
    # Image
    # ===============================
    with col1:

        st.markdown("<div class='card'>", unsafe_allow_html=True)

        img = Image.open(uploaded_file).convert("RGB")

        st.image(
            img,
            caption="Uploaded Image",
            use_container_width=True
        )

        st.markdown("</div>", unsafe_allow_html=True)

    # ===============================
    # Prediction Result
    # ===============================
    with col2:

        st.markdown("<div class='card'>", unsafe_allow_html=True)

        img_resized = img.resize((224,224))
        img_array = np.array(img_resized)/255.0
        img_array = np.expand_dims(img_array, axis=0)

        # Feature extraction
        feature = base_model.predict(img_array)

        # Model prediction
        prediction = ensemble.predict(feature)
        probabilities = ensemble.predict_proba(feature)

        pred_class = class_names[prediction[0]]
        confidence = float(np.max(probabilities))

        st.markdown(
            f"<div class='prediction'>Prediction: {pred_class.capitalize()} ♻️</div>",
            unsafe_allow_html=True
        )

        st.markdown(
            f"<div class='confidence'>Confidence: {round(confidence*100,2)}%</div>",
            unsafe_allow_html=True
        )

        st.progress(int(confidence*100))

        st.markdown("</div>", unsafe_allow_html=True)

    # ===============================
    # Probability Chart
    # ===============================
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.subheader("📊 Probability Breakdown")

    df = pd.DataFrame({
        "Class": class_names,
        "Probability": probabilities[0]
    })

    st.bar_chart(df.set_index("Class"))

    st.markdown("</div>", unsafe_allow_html=True)