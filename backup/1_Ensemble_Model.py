import streamlit as st
from style import load_css
load_css()


st.title("🤖 Machine Learning Ensemble Model")




# ---------------- INTRO ----------------

st.markdown("""
<div class="card">

## Garbage Classification using Ensemble Machine Learning

This project focuses on **automatic garbage classification using machine learning techniques**.

The system is designed to classify waste images into their correct categories.  
Accurate waste classification is essential for:

• recycling systems  
• waste management automation  
• environmental sustainability  

Traditional waste sorting relies heavily on **manual labor**. Machine learning helps automate this process by analyzing images and predicting the correct waste category.

</div>
""", unsafe_allow_html=True)


# ---------------- DATASET ----------------

st.markdown("""
<div class="card">

## Dataset

This project uses the **Garbage Classification Dataset**, which contains images of real-world waste materials.

This dataset is commonly used in **computer vision research for recycling and waste classification systems**.

Dataset source:

Kaggle – Garbage Classification Dataset  

https://www.kaggle.com/datasets/asdasdasasdas/garbage-classification

</div>
""", unsafe_allow_html=True)


# ---------------- CLASSES ----------------

st.markdown("""
<div class="card">

## Dataset Classes

The dataset contains **six categories of waste materials**:

<div class="highlight">

• **Cardboard** – cardboard boxes and packaging  

• **Glass** – glass bottles and containers  

• **Metal** – aluminum cans and metal objects  

• **Paper** – newspapers and paper sheets  

• **Plastic** – plastic bottles and packaging  

• **Trash** – mixed non-recyclable waste  

</div>

Each class contains images captured under different conditions such as lighting, orientation, and backgrounds.  
This diversity helps the model learn **robust visual features**.

</div>
""", unsafe_allow_html=True)


# ---------------- DATA PREPARATION ----------------

st.markdown("""
<div class="card">

## Data Preparation

Before training the machine learning models, the dataset undergoes a **data preprocessing pipeline**.

Raw images cannot be directly used because they may have different:

• sizes  
• pixel scales  
• visual structures  

The preprocessing pipeline ensures that the dataset becomes **consistent and suitable for machine learning algorithms**.

</div>
""", unsafe_allow_html=True)


# ---------------- IMAGE PROCESSING ----------------

st.markdown("""
<div class="card">

## Image Processing Steps

### Image Loading

Images are loaded from folder directories where each folder represents one class.

Example structure:

cardboard/  
glass/  
metal/  
paper/  
plastic/  
trash/

Each image is read from disk and converted into **numerical pixel data**.

---

### Image Resizing

All images are resized to:

**224 × 224 pixels**

This size is required because the feature extractor **MobileNetV2** expects this input resolution.

---

### Image Normalization

Original pixel values range from:

0 – 255

To improve model performance, pixel values are normalized to:

**0 – 1**

This is done by dividing pixel values by **255**.

Normalization improves:

• training stability  
• convergence speed  
• numerical stability

</div>
""", unsafe_allow_html=True)


# ---------------- FEATURE EXTRACTION ----------------

st.markdown("""
<div class="card">

## Feature Extraction using MobileNetV2

Instead of using raw image pixels directly, this project applies **feature extraction**.

The pretrained convolutional neural network **MobileNetV2** is used to extract high-level visual features.

MobileNetV2 was originally trained on the **ImageNet dataset**, which contains more than **1 million images across 1000 categories**.

The convolution layers automatically detect visual patterns such as:

• edges  
• shapes  
• textures  
• object contours  

The output is converted into a **feature vector representing the image**.

These feature vectors are then used as input for machine learning algorithms.

</div>
""", unsafe_allow_html=True)


# ---------------- TRAIN TEST ----------------

st.markdown("""
<div class="card">

## Train–Test Split

After feature extraction, the dataset is divided into two subsets:

• **Training Set** – used to train the models  

• **Testing Set** – used to evaluate performance  

The dataset is split using an **80 / 20 ratio**:

• 80% training data  
• 20% testing data  

This ensures that the model is evaluated on **unseen images**, providing a reliable measurement of performance.

</div>
""", unsafe_allow_html=True)


# ---------------- MODELS ----------------

st.markdown("""
<div class="card">

## Machine Learning Algorithms

Three machine learning algorithms are used:

<div class="highlight">

• Random Forest  

• Support Vector Machine (SVM)  

• XGBoost  

</div>

Each algorithm learns patterns from the extracted feature vectors and predicts the garbage category.

</div>
""", unsafe_allow_html=True)


# ---------------- ENSEMBLE ----------------

st.markdown("""
<div class="card">

## Ensemble Learning

Instead of using a single model, the system uses **Ensemble Learning**.

The ensemble method used is **Soft Voting**.

Soft voting combines predictions from multiple models by **averaging their predicted probabilities**.

The class with the highest average probability becomes the final prediction.

Benefits include:

• improved prediction accuracy  
• increased model stability  
• better generalization

</div>
""", unsafe_allow_html=True)


# ---------------- PERFORMANCE ----------------

st.markdown("""
<div class="card">

## Model Performance

After training and evaluation, the ensemble model achieved approximately:

<h2 style="color:#7c3aed;">82% Accuracy</h2>

This means the model correctly classifies about **82 out of every 100 garbage images**.

</div>
""", unsafe_allow_html=True)


# ---------------- SUMMARY ----------------

st.markdown("""
<div class="card">

## Project Summary

This project demonstrates how machine learning can be applied to **real-world environmental challenges**.

Key components include:

• image preprocessing and normalization  

• feature extraction using MobileNetV2  

• machine learning classification algorithms  

• ensemble learning with soft voting  

Such systems can support applications such as:

• automated recycling systems  
• smart waste sorting machines  
• environmental monitoring  
• sustainable waste management

</div>
""", unsafe_allow_html=True)