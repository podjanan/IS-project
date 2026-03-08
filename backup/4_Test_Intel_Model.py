import streamlit as st
import tensorflow as tf
import numpy as np
import cv2
from PIL import Image
from style import load_css
load_css()

# ===============================
# Page Config
# ===============================
st.set_page_config(
    page_title="Intel Scene Classification",
    page_icon="🌄",
    layout="wide"
)



# ===============================
# Title
# ===============================
st.title("Intel Natural Scene Classification 🌄")

st.write("""
Upload an image to test the trained neural network model.

The system will display:

• Prediction  
• Top 3 predictions  
• Grad-CAM visualization
""")

# ===============================
# Load Model
# ===============================
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model("models/intel_nn_model_93_9.h5")
    return model

model = load_model()

class_names = [
    "buildings",
    "forest",
    "glacier",
    "mountain",
    "sea",
    "street"
]

# ===============================
# Grad-CAM Function
# ===============================
def make_gradcam_heatmap(img_array, model, last_conv_layer_name="Conv_1"):

    base_model = model.get_layer("mobilenetv2_1.00_224")

    x = base_model.output
    x = model.layers[1](x)
    x = model.layers[2](x)
    x = model.layers[3](x)
    predictions = model.layers[4](x)

    grad_model = tf.keras.models.Model(
        inputs=base_model.input,
        outputs=[
            base_model.get_layer(last_conv_layer_name).output,
            predictions
        ]
    )

    with tf.GradientTape() as tape:

        conv_outputs, preds = grad_model(img_array)

        pred_index = tf.argmax(preds[0])

        class_channel = preds[:, pred_index]

    grads = tape.gradient(class_channel, conv_outputs)

    pooled_grads = tf.reduce_mean(grads, axis=(0,1,2))

    conv_outputs = conv_outputs[0]

    heatmap = conv_outputs @ pooled_grads[..., tf.newaxis]

    heatmap = tf.squeeze(heatmap)

    heatmap = tf.maximum(heatmap, 0) / tf.reduce_max(heatmap)

    return heatmap.numpy()

# ===============================
# Upload Section
# ===============================
st.markdown("<div class='card'>", unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "Upload Scene Image",
    type=["jpg","jpeg","png"]
)

st.markdown("</div>", unsafe_allow_html=True)

# ===============================
# Prediction
# ===============================
if uploaded_file:

    img = Image.open(uploaded_file).convert("RGB")
    img = img.resize((224,224))

    col1, col2 = st.columns(2)

    # -------------------------
    # Image
    # -------------------------
    with col1:

        st.markdown("<div class='card'>", unsafe_allow_html=True)

        st.image(
            img,
            caption="Uploaded Image",
            use_container_width=True
        )

        st.markdown("</div>", unsafe_allow_html=True)

    img_array = np.array(img)/255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)[0]

    top3 = prediction.argsort()[-3:][::-1]

    # -------------------------
    # Prediction Result
    # -------------------------
    with col2:

        st.markdown("<div class='card'>", unsafe_allow_html=True)

        st.markdown(
            f"<div class='prediction'>Prediction: {class_names[top3[0]].capitalize()}</div>",
            unsafe_allow_html=True
        )

        st.markdown(
            f"<div class='confidence'>Confidence: {prediction[top3[0]]*100:.2f}%</div>",
            unsafe_allow_html=True
        )

        st.progress(int(prediction[top3[0]]*100))

        st.subheader("Top 3 Predictions")

        for i in top3:

            st.write(
                f"{class_names[i]} : {prediction[i]*100:.2f}%"
            )

        st.markdown("</div>", unsafe_allow_html=True)

    # -------------------------
    # Grad-CAM
    # -------------------------
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.subheader("Grad-CAM Visualization")

    heatmap = make_gradcam_heatmap(img_array, model)

    img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

    heatmap = cv2.resize(heatmap,(224,224))
    heatmap = np.uint8(255 * heatmap)

    heatmap = cv2.applyColorMap(
        heatmap,
        cv2.COLORMAP_JET
    )

    superimposed_img = heatmap * 0.4 + img_cv

    st.image(
        cv2.cvtColor(
            superimposed_img.astype("uint8"),
            cv2.COLOR_BGR2RGB
        ),
        caption="Grad-CAM Heatmap",
        use_container_width=True
    )

    st.markdown("""
### Heatmap Explanation

Grad-CAM highlights image regions that influenced the model's decision.

Color meaning:

🔴 **Red / Yellow** → Most important regions  

🟢 **Green** → Moderately important  

🔵 **Blue** → Less important  

Examples:

• Buildings → focus on structures  

• Forest → focus on trees  

• Sea → focus on water areas  

This visualization helps interpret how the neural network makes predictions.
""")

    st.markdown("</div>", unsafe_allow_html=True)