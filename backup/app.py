import streamlit as st

# Page config
st.set_page_config(
    page_title="AI Image Classification",
    page_icon="🧠",
    layout="wide"
)

# ---------- CSS STYLE ----------
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


# ---------- TITLE ----------
st.title("🧠 AI Image Classification System")

# ---------- INTRO CARD ----------
st.markdown("""
<div class="card">

## Model Evaluation and Explainability

To better understand the performance and behavior of AI models, this system includes **evaluation metrics** and **Explainable AI techniques**.

These tools help measure how well the models perform and provide insights into how predictions are made.

</div>
""", unsafe_allow_html=True)

# ---------- EVALUATION METRICS ----------
st.markdown("""
<div class="card">

<h2>Evaluation Metrics</h2>

<div class="metric-box">

<h3>Accuracy</h3>

Accuracy measures the percentage of correct predictions made by the model.

<b>Accuracy = Correct Predictions / Total Predictions</b>

Example:

If the model correctly classifies <b>93 images out of 100</b>

Accuracy = <b>93%</b>

</div>

<div class="metric-box">

<h3>Loss Function</h3>

During training, the neural network optimizes a <b>loss function</b>.

In this project, the model uses:

<b>Categorical Crossentropy</b>

Lower loss values indicate better model predictions.

The goal during training is to <b>minimize the loss value</b>.

</div>

</div>
""", unsafe_allow_html=True)

# ---------- CONFUSION MATRIX ----------
st.markdown("""
<div class="card">

<h2>Confusion Matrix</h2>

A confusion matrix provides a detailed view of classification performance.

It compares:

<b>Actual Labels vs Predicted Labels</b>

Example:

| Actual / Predicted | Glass | Paper | Plastic |
|-------------------|------|------|------|
| Glass | 50 | 3 | 2 |
| Paper | 4 | 48 | 3 |
| Plastic | 1 | 2 | 52 |

From the confusion matrix we can identify:

• which classes are frequently confused  
• where the model makes mistakes  
• how balanced the predictions are  

Confusion matrices are especially useful for <b>multi-class classification</b>.

</div>
""", unsafe_allow_html=True)

# ---------- GRAD CAM ----------
st.markdown("""
<div class="card">

<h2>Explainable AI (Grad-CAM)</h2>

Deep learning models are often considered <b>black-box systems</b>.

To improve transparency, this project uses an Explainable AI technique called:

<h3>Grad-CAM (Gradient-weighted Class Activation Mapping)</h3>

Grad-CAM visualizes <b>which regions of an image influenced the model's prediction</b>.

</div>
""", unsafe_allow_html=True)

# ---------- HOW IT WORKS ----------
st.markdown("""
<div class="card">

<h2>How Grad-CAM Works</h2>

1. Pass the input image through the neural network  
2. Identify the predicted class  
3. Compute gradients with respect to feature maps  
4. Generate a heatmap highlighting important regions  

The heatmap is then overlaid on the original image.

</div>
""", unsafe_allow_html=True)

# ---------- VISUALIZATION ----------
st.markdown("""
<div class="card">

<h2>Grad-CAM Visualization</h2>

In Grad-CAM results:

• <b>Red / Yellow areas</b> indicate strong attention from the model  
• <b>Blue areas</b> indicate low influence  

This helps explain:

• why the model made a prediction  
• which visual features were important  
• whether the model focuses on meaningful regions

</div>
""", unsafe_allow_html=True)

# ---------- IMPORTANCE ----------
st.markdown("""
<div class="card">

<h2>Importance of Explainable AI</h2>

Explainable AI improves the transparency and reliability of AI systems.

Benefits include:

• increased trust in AI predictions  
• easier debugging of model errors  
• better understanding of model behavior  

Grad-CAM is widely used in:

• medical imaging  
• autonomous driving  
• computer vision research

</div>
""", unsafe_allow_html=True)