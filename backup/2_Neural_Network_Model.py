import streamlit as st
from style import load_css
load_css()

st.title("🧠 Neural Network Model")




# ---------------- INTRO ----------------

st.markdown("""
<div class="card">

## Natural Scene Classification using Convolutional Neural Networks

This part of the project focuses on **image classification of natural scenes using deep learning techniques**.

The goal of the system is to automatically recognize different types of environments from images.

In computer vision, image classification is a fundamental task where a model learns patterns from visual data and assigns an image to a predefined category.

This project uses **Convolutional Neural Networks (CNNs)**, which automatically learn hierarchical visual features such as:

• edges  
• textures  
• shapes  
• object structures  

The neural network architecture used is **MobileNetV2**, a lightweight yet powerful model designed for efficient image recognition.

</div>
""", unsafe_allow_html=True)


# ---------------- DATASET ----------------

st.markdown("""
<div class="card">

## Dataset

This model uses the **Intel Natural Scene Dataset**.

The dataset contains thousands of images representing natural and urban environments.

Dataset source:

Kaggle – Intel Image Classification Dataset  

https://www.kaggle.com/datasets/puneet6060/intel-image-classification

</div>
""", unsafe_allow_html=True)


# ---------------- CLASSES ----------------

st.markdown("""
<div class="card">

## Dataset Classes

The dataset contains **six scene categories**.

<div class="highlight">

• **Buildings** – urban environments and architecture  

• **Forest** – trees and natural vegetation  

• **Glacier** – icy mountains and snow landscapes  

• **Mountain** – rocky mountainous terrain  

• **Sea** – oceans and beaches  

• **Street** – roads and urban transportation environments  

</div>

These images contain variations in lighting, angles, and environments which helps improve model robustness.

</div>
""", unsafe_allow_html=True)


# ---------------- DATA PREPARATION ----------------

st.markdown("""
<div class="card">

## Data Preparation

Before training the neural network, images go through a **data preprocessing pipeline**.

Raw images cannot be directly used because they may differ in:

• resolution  
• pixel distribution  
• visual structure  

Preprocessing ensures the dataset becomes **consistent and suitable for deep learning**.

</div>
""", unsafe_allow_html=True)


# ---------------- IMAGE PROCESSING ----------------

st.markdown("""
<div class="card">

## Image Processing Steps

### Image Loading

Images are loaded using image generators.

Each image is:

• read from disk  
• converted into pixel arrays  
• automatically labeled based on folder names

---

### Image Resizing

All images are resized to:

**224 × 224 pixels**

This resolution is required because **MobileNetV2 expects this input size**.

---

### Image Normalization

Original pixel values range from:

0 – 255

All pixel values are normalized to:

**0 – 1**

This is done by dividing each pixel value by **255**.

Normalization improves:

• gradient stability  
• faster convergence  
• numerical stability

</div>
""", unsafe_allow_html=True)


# ---------------- TRAIN VALIDATION ----------------

st.markdown("""
<div class="card">

## Train–Validation Split

The dataset is divided into two subsets.

<div class="highlight">

**Training Set**

Used to train the neural network and update model weights.

**Validation Set**

Used to evaluate model performance during training.

</div>

The split ratio is approximately:

• **80% Training Data**  
• **20% Validation Data**

This ensures the model is tested on **unseen images**.

</div>
""", unsafe_allow_html=True)


# ---------------- DATA AUGMENTATION ----------------

st.markdown("""
<div class="card">

## Data Augmentation

Data augmentation increases the diversity of the training dataset by generating modified versions of existing images.

This helps the model generalize better and prevents **overfitting**.

Augmentation techniques used:

<div class="highlight">

**Rotation** – random small rotations  

**Zoom** – simulate objects appearing closer or further  

**Horizontal Flip** – mirror images horizontally

</div>

These transformations allow the model to learn more **robust visual features**.

</div>
""", unsafe_allow_html=True)


# ---------------- MODEL ARCHITECTURE ----------------

st.markdown("""
<div class="card">

## Model Architecture

The architecture used in this project is based on **MobileNetV2**.

<div class="model-box">

MobileNetV2 (Pretrained CNN)  
↓  
GlobalAveragePooling Layer  
↓  
Dense Layer  
↓  
Dropout Layer  
↓  
Softmax Output Layer

</div>

</div>
""", unsafe_allow_html=True)


# ---------------- TRANSFER LEARNING ----------------

st.markdown("""
<div class="card">

## Transfer Learning

Training deep neural networks from scratch requires very large datasets.

Therefore this project uses **Transfer Learning**.

MobileNetV2 was pretrained on the **ImageNet dataset**, which contains more than **1 million images across 1000 classes**.

Benefits of transfer learning include:

• faster training  
• improved accuracy  
• reduced computational cost  
• better generalization

</div>
""", unsafe_allow_html=True)


# ---------------- PERFORMANCE ----------------

st.markdown("""
<div class="card">

## Model Performance

After training and validation, the neural network achieved approximately:

<h2 style="color:#7c3aed !important;">93% Accuracy</h2>

This means the model correctly classifies around **93 out of every 100 images**.

</div>
""", unsafe_allow_html=True)


# ---------------- SUMMARY ----------------

st.markdown("""
<div class="card">

## Project Summary

This project demonstrates how **deep learning techniques** can classify natural environments automatically.

Key components include:

• dataset preprocessing  
• image normalization  
• data augmentation  
• MobileNetV2 feature extraction  
• transfer learning  
• neural network classification  

Such systems can be applied in:

• environmental monitoring  
• autonomous vehicles  
• geographic scene recognition  
• smart city systems

</div>
""", unsafe_allow_html=True)