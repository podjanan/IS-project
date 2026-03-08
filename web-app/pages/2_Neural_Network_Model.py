import streamlit as st
from style import load_css
load_css()

CARD  = "background:white; border:1px solid #ede9fe; border-radius:16px; padding:32px 36px; margin-bottom:22px; box-shadow:0 2px 16px rgba(124,58,237,0.06);"
TOP   = "border-top:3px solid #7c3aed;"
LABEL = "font-family:'Syne',sans-serif; font-size:0.7rem; font-weight:700; letter-spacing:0.15em; text-transform:uppercase; color:#7c3aed;"
HL    = "background:#f5f3ff; border:1px solid #ddd6fe; border-left:3px solid #7c3aed; border-radius:10px; padding:18px 22px; margin:12px 0;"
SUB   = "font-family:'Syne',sans-serif; font-weight:700; color:#4c1d95; margin:20px 0 4px 0; font-size:1rem; padding:10px 16px; background:#f5f3ff; border-left:3px solid #7c3aed; border-radius:0 8px 8px 0;"

DARK_CARD = "background:#0d1117; border:1px solid #30363d; border-radius:16px; padding:32px 36px; margin-bottom:22px; box-shadow:0 2px 16px rgba(0,0,0,0.3);"
DARK_LABEL = "font-family:'Syne',sans-serif; font-size:0.7rem; font-weight:700; letter-spacing:0.15em; text-transform:uppercase; color:#8b949e;"

def card_open(label, title):
    st.markdown(f'<div style="{CARD} {TOP}"><span style="{LABEL}">{label}</span><h2 style="font-family:\'Syne\',sans-serif; color:#1e0a4a; margin:8px 0 16px 0;">{title}</h2>', unsafe_allow_html=True)

def dark_card_open(label, title):
    st.markdown(f'<div style="{DARK_CARD}"><span style="{DARK_LABEL}">{label}</span><h2 style="font-family:\'Syne\',sans-serif; color:#e6edf3; margin:8px 0 16px 0;">{title}</h2>', unsafe_allow_html=True)

def card_close():
    st.markdown("</div>", unsafe_allow_html=True)

def subhead(text):
    st.markdown(f'<div style="{SUB}">{text}</div>', unsafe_allow_html=True)

def body(text):
    st.markdown(f'<p style="color:#6b7280; margin-bottom:14px; font-size:0.95rem;">{text}</p>', unsafe_allow_html=True)

def note(text):
    st.markdown(f'<div style="{HL}"><p style="margin:0; font-size:0.9rem; color:#4b5563;">{text}</p></div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════
# HERO
# ══════════════════════════════════════════════════════════════════════════
st.markdown(f"""
<div style="padding:48px 0 32px 0;">
    <span style="{LABEL}; background:#f5f3ff; padding:6px 16px; border-radius:50px; border:1px solid #ddd6fe;">Model 02 · Deep Learning</span>
    <h1 style="font-family:'Syne',sans-serif; font-size:2.8rem; font-weight:800; color:#1e0a4a; margin:14px 0 14px 0; letter-spacing:-0.03em;">Natural Scene Classification</h1>
    <p style="font-size:1.05rem; color:#6b7280; max-width:580px; margin:0;">
        Fine-tuned MobileNetV2 neural network with transfer learning for automatic recognition
        of 6 natural and urban scene categories.
    </p>
</div>
""", unsafe_allow_html=True)

s1,s2,s3 = st.columns(3)
for col,(num,lbl) in zip([s1,s2,s3],[("93.9%","Validation Accuracy"),("6","Scene Categories"),("224px","Input Resolution")]):
    with col:
        st.markdown(f'<div style="{CARD} {TOP} text-align:center; padding:22px 14px;"><div style="font-family:\'Syne\',sans-serif; font-size:2rem; font-weight:800; color:#7c3aed;">{num}</div><div style="font-size:0.74rem; color:#9ca3af; text-transform:uppercase; letter-spacing:0.08em; margin-top:4px;">{lbl}</div></div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════
# DATASET
# ══════════════════════════════════════════════════════════════════════════
st.markdown(f"""
<div style="{CARD} {TOP}">
    <span style="{LABEL}">Data</span>
    <h2 style="font-family:'Syne',sans-serif; color:#1e0a4a; margin:8px 0 14px 0;">Intel Natural Scene Dataset</h2>
    <p style="color:#6b7280; margin-bottom:16px;">
        A large collection of images representing natural and urban environments,
        widely used in computer vision scene-understanding research.
    </p>
    <div style="{HL}">
        <p style="margin:0; font-size:0.9rem; color:#4b5563;">
            📦 Source: <strong style="color:#2d1167;">Kaggle</strong> — Intel Image Classification Dataset<br>
            🔗 kaggle.com/datasets/puneet6060/intel-image-classification
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════
# CLASSES
# ══════════════════════════════════════════════════════════════════════════
st.markdown(f'<div style="{CARD} {TOP}"><span style="{LABEL}">Categories</span><h2 style="font-family:\'Syne\',sans-serif; color:#1e0a4a; margin:8px 0 20px 0;">Six Scene Classes</h2>', unsafe_allow_html=True)
scenes = [("🏙️","Buildings","Urban environments, cityscapes"),("🌲","Forest","Dense vegetation, trees"),("🏔️","Glacier","Icy mountains, snow"),("⛰️","Mountain","Rocky peaks, highlands"),("🌊","Sea","Oceans, beaches"),("🛣️","Street","Roads, urban transport")]
r1 = st.columns(3, gap="medium"); r2 = st.columns(3, gap="medium")
for col,(icon,name,desc) in zip(list(r1)+list(r2), scenes):
    with col:
        st.markdown(f'<div style="background:#faf9ff; border:1px solid #ede9fe; border-radius:12px; padding:18px 20px; margin-bottom:14px;"><div style="font-size:1.6rem; margin-bottom:8px;">{icon}</div><div style="font-family:\'Syne\',sans-serif; font-weight:700; color:#2d1167; font-size:0.95rem;">{name}</div><div style="font-size:0.82rem; color:#9ca3af; margin-top:4px;">{desc}</div></div>', unsafe_allow_html=True)
card_close()

# ══════════════════════════════════════════════════════════════════════════
# PREPROCESSING
# ══════════════════════════════════════════════════════════════════════════
st.markdown(f'<div style="{CARD} {TOP}"><span style="{LABEL}">Pipeline</span><h2 style="font-family:\'Syne\',sans-serif; color:#1e0a4a; margin:8px 0 6px 0;">Data Preparation</h2><p style="color:#6b7280; margin-bottom:8px;">Images pass through a standardized preprocessing pipeline before entering the network.</p>', unsafe_allow_html=True)
steps = [
    ("01","Image Loading via Generator","Keras ImageDataGenerator โหลดภาพจาก directory. Class labels จากชื่อ folder อัตโนมัติ"),
    ("02","Resizing → 224 × 224 px","Resize ทุกภาพเป็น 224×224 ตาม MobileNetV2 input shape"),
    ("03","Normalization → [0, 1]","pixel / 255. Stabilizes gradients and accelerates convergence."),
    ("04","Train / Validation Split — 80 / 20","80% Train, 20% Validation เพื่อ monitor generalization ทุก epoch"),
]
for i,(num,title,desc) in enumerate(steps):
    border = "1px solid #f3f4f6" if i < len(steps)-1 else "none"
    st.markdown(f'<div style="display:flex; gap:18px; align-items:flex-start; padding:18px 0; border-bottom:{border};"><div style="font-family:\'Syne\',sans-serif; font-size:1.5rem; font-weight:800; color:#ddd6fe; min-width:38px; line-height:1;">{num}</div><div><div style="font-family:\'Syne\',sans-serif; font-weight:700; color:#2d1167; font-size:0.98rem; margin-bottom:5px;">{title}</div><div style="font-size:0.88rem; color:#6b7280;">{desc}</div></div></div>', unsafe_allow_html=True)
card_close()

# ══════════════════════════════════════════════════════════════════════════
# AUGMENTATION
# ══════════════════════════════════════════════════════════════════════════
st.markdown(f'<div style="{CARD} {TOP}"><span style="{LABEL}">Regularization</span><h2 style="font-family:\'Syne\',sans-serif; color:#1e0a4a; margin:8px 0 14px 0;">Data Augmentation</h2><p style="color:#6b7280; margin-bottom:20px;">Random visual transformations applied on-the-fly during training to prevent overfitting and increase diversity.</p>', unsafe_allow_html=True)
aug_cols = st.columns(3, gap="medium")
for col,(icon,title,desc) in zip(aug_cols,[("🔄","Rotation","random small-angle rotations"),("🔍","Zoom","simulate closer/further objects"),("↔️","Horizontal Flip","mirror images horizontally")]):
    with col:
        st.markdown(f'<div style="background:#f5f3ff; border:1px solid #ddd6fe; border-top:3px solid #7c3aed; border-radius:12px; padding:22px; text-align:center; margin-bottom:14px;"><div style="font-size:1.8rem; margin-bottom:10px;">{icon}</div><div style="font-family:\'Syne\',sans-serif; font-weight:700; color:#4c1d95; margin-bottom:6px;">{title}</div><p style="margin:0; font-size:0.85rem; color:#6b7280;">{desc}</p></div>', unsafe_allow_html=True)
card_close()

# ══════════════════════════════════════════════════════════════════════════
# ARCHITECTURE
# ══════════════════════════════════════════════════════════════════════════
st.markdown(f"""
<div style="{CARD} {TOP}">
    <span style="{LABEL}">Architecture</span>
    <h2 style="font-family:'Syne',sans-serif; color:#1e0a4a; margin:8px 0 20px 0;">Model Architecture</h2>
    <div style="background:#f5f3ff; border:1px solid #ddd6fe; border-radius:14px; padding:32px; text-align:center; font-family:'Syne',sans-serif; color:#4c1d95; font-size:1rem; line-height:2.6;">
        Input Image (224 × 224 × 3)<br>↓<br>
        MobileNetV2 — Pretrained Feature Extractor (Frozen)<br>↓<br>
        Global Average Pooling<br>↓<br>
        Dense (256, ReLU)<br>↓<br>
        Dropout (0.3)<br>↓<br>
        <strong style="color:#1e0a4a;">Softmax Output → 6 Classes</strong>
    </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════
# PERFORMANCE
# ══════════════════════════════════════════════════════════════════════════
st.markdown(f"""
<div style="{CARD} {TOP}">
    <span style="{LABEL}">Results</span>
    <h2 style="font-family:'Syne',sans-serif; color:#1e0a4a; margin:8px 0 20px 0;">Model Performance</h2>
    <div style="display:inline-flex; align-items:center; gap:16px; background:linear-gradient(135deg,#f5f3ff,#ede9fe); border:1px solid #ddd6fe; border-radius:50px; padding:16px 36px; margin-bottom:20px;">
        <span style="font-family:'Syne',sans-serif; font-size:2.4rem; font-weight:800; color:#7c3aed; letter-spacing:-0.03em;">93.9%</span>
        <div>
            <div style="font-size:0.72rem; color:#9ca3af; text-transform:uppercase; letter-spacing:0.08em;">Validation Accuracy</div>
            <div style="font-size:0.85rem; color:#6b7280; margin-top:3px;">~94 out of every 100 scene images correctly classified</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════
# THEORY: CNN
# ══════════════════════════════════════════════════════════════════════════
card_open("Theory · Part 01", "Convolutional Neural Network (CNN) — ทฤษฎีและหลักการ")
body("CNN เป็น Neural Network ที่ออกแบบมาเพื่อประมวลผลข้อมูลภาพโดยเฉพาะ โดยใช้ <strong style='color:#2d1167;'>Convolution Operation</strong> ตรวจจับ Visual Feature แบบ Hierarchical ตั้งแต่ระดับต่ำ (edges) ไปจนถึงระดับสูง (objects, scenes)")

subhead("1. Convolution Layer")
body("ใช้ <strong style='color:#2d1167;'>Filter (Kernel)</strong> ขนาด k×k เลื่อนผ่านภาพ Input เพื่อสร้าง Feature Map แต่ละ Filter เรียนรู้การตรวจจับ Pattern ที่แตกต่างกัน")
st.markdown(f'''<div style="background:#0d1117;border:1px solid #30363d;border-radius:10px;padding:20px 24px;font-family:'Courier New',monospace;font-size:0.82rem;color:#e6edf3;line-height:1.75;margin:12px 0 20px 0;display:block;width:100%;">Output(i,j) = Σₘ Σₙ  Input(i+m, j+n) · Kernel(m,n)  +  bias<br><br>Output Size = (W - K + 2P) / S + 1<br><br>เมื่อ  W = Input width<br>       K = Kernel size<br>       P = Padding<br>       S = Stride</div>''', unsafe_allow_html=True)

subhead("2. Activation Function — ReLU")
st.markdown(f'''<div style="background:#0d1117;border:1px solid #30363d;border-radius:10px;padding:20px 24px;font-family:'Courier New',monospace;font-size:0.82rem;color:#e6edf3;line-height:1.75;margin:12px 0 20px 0;display:block;width:100%;">ReLU(x) = max(0, x)<br><br>ข้อดี:<br>  - คำนวณเร็ว, แก้ปัญหา Vanishing Gradient<br>  - ทำให้เครือข่ายเรียนรู้ Non-linear Patterns ได้<br>  - Sparse Activation ช่วยลด Overfitting</div>''', unsafe_allow_html=True)

subhead("3. Pooling Layer")
st.markdown(f'''<div style="background:#0d1117;border:1px solid #30363d;border-radius:10px;padding:20px 24px;font-family:'Courier New',monospace;font-size:0.82rem;color:#e6edf3;line-height:1.75;margin:12px 0 20px 0;display:block;width:100%;">Max Pooling:  Output(i,j) = max(region)<br>Avg Pooling:  Output(i,j) = mean(region)<br><br>วัตถุประสงค์:<br>  - ลดขนาด Feature Map (Spatial Downsampling)<br>  - เพิ่ม Translation Invariance<br>  - ลดจำนวน Parameters</div>''', unsafe_allow_html=True)

subhead("4. Softmax Output Layer")
st.markdown(f'''<div style="background:#0d1117;border:1px solid #30363d;border-radius:10px;padding:20px 24px;font-family:'Courier New',monospace;font-size:0.82rem;color:#e6edf3;line-height:1.75;margin:12px 0 20px 0;display:block;width:100%;">Softmax(zᵢ) = exp(zᵢ) / Σⱼ exp(zⱼ)<br><br>แปลง Raw Scores (Logits) เป็น Probability Distribution<br>Σ Softmax(zᵢ) = 1.0  เสมอ<br>ใช้สำหรับ Multi-class Classification (6 คลาส)</div>''', unsafe_allow_html=True)

subhead("5. Categorical Cross-Entropy Loss")
st.markdown(f'''<div style="background:#0d1117;border:1px solid #30363d;border-radius:10px;padding:20px 24px;font-family:'Courier New',monospace;font-size:0.82rem;color:#e6edf3;line-height:1.75;margin:12px 0 20px 0;display:block;width:100%;">L = -Σᵢ  yᵢ · log(ŷᵢ)<br><br>เมื่อ  yᵢ  = True label (One-hot encoded)<br>       ŷᵢ  = Predicted probability จาก Softmax<br><br>Optimizer (Adam) ทำการ Minimize L ด้วย Backpropagation</div>''', unsafe_allow_html=True)

subhead("6. Adam Optimizer")
body("<strong style='color:#2d1167;'>Backpropagation</strong> คำนวณ Gradient ของ Loss ต่อ Weight ทุกตัวผ่าน Chain Rule จาก Output Layer ย้อนกลับสู่ Input Layer")
st.markdown(f'''<div style="background:#0d1117;border:1px solid #30363d;border-radius:10px;padding:20px 24px;font-family:'Courier New',monospace;font-size:0.82rem;color:#e6edf3;line-height:1.75;margin:12px 0 20px 0;display:block;width:100%;">Adam Optimizer:<br>  mₜ = β₁·mₜ₋₁ + (1-β₁)·gₜ          (1st moment / momentum)<br>  vₜ = β₂·vₜ₋₁ + (1-β₂)·gₜ²         (2nd moment / velocity)<br>  m̂ₜ = mₜ / (1-β₁ᵗ)                  (bias correction)<br>  v̂ₜ = vₜ / (1-β₂ᵗ)                  (bias correction)<br>  θₜ = θₜ₋₁ - α · m̂ₜ / (√v̂ₜ + ε)<br><br>Default:  α=0.001, β₁=0.9, β₂=0.999, ε=1e-8</div>''', unsafe_allow_html=True)
card_close()

# ══════════════════════════════════════════════════════════════════════════
# THEORY: MOBILENETV2
# ══════════════════════════════════════════════════════════════════════════
card_open("Theory · Part 02", "MobileNetV2 — สถาปัตยกรรมและหลักการ")
body("MobileNetV2 เป็น CNN Architecture ที่ออกแบบโดย Google เพื่อให้ทำงานได้ดีบน <strong style='color:#2d1167;'>อุปกรณ์ที่มีทรัพยากรจำกัด</strong> โดยใช้ 2 Innovation หลัก: <strong style='color:#2d1167;'>Depthwise Separable Convolution</strong> และ <strong style='color:#2d1167;'>Inverted Residual Block</strong>")

subhead("1. Depthwise Separable Convolution")
body("แทน Standard Convolution ที่คำนวณ Spatial และ Channel ไปพร้อมกัน MobileNetV2 แยกออกเป็น 2 ขั้นตอน ลดการคำนวณได้ 8-9 เท่า")
st.markdown(f'''<div style="background:#0d1117;border:1px solid #30363d;border-radius:10px;padding:20px 24px;font-family:'Courier New',monospace;font-size:0.82rem;color:#e6edf3;line-height:1.75;margin:12px 0 20px 0;display:block;width:100%;">Standard Conv:  Dₖ × Dₖ × M × N  operations<br>Depthwise Conv: Dₖ × Dₖ × M       (per-channel spatial filter)<br>Pointwise Conv: 1  × 1  × M × N   (channel mixing)<br><br>Reduction Factor ≈ 1/N + 1/Dₖ²<br>≈ 8–9x ลดการคำนวณโดยแทบไม่สูญเสีย Accuracy</div>''', unsafe_allow_html=True)

subhead("2. Inverted Residual Block (Bottleneck)")
body("Innovation หลักของ MobileNetV2 คือการกลับโครงสร้าง Residual Block โดย <strong style='color:#2d1167;'>Expand ก่อน แล้ว Project ลง</strong> (แทนที่จะ Compress แล้ว Expand แบบ ResNet)")
st.markdown(f'''<div style="background:#0d1117;border:1px solid #30363d;border-radius:10px;padding:20px 24px;font-family:'Courier New',monospace;font-size:0.82rem;color:#e6edf3;line-height:1.75;margin:12px 0 20px 0;display:block;width:100%;">Input (low-dim) → Expand (t×) → Depthwise Conv → Project (low-dim)<br>↑___________________Residual Connection (ถ้า in == out)___________________↑<br><br>t = Expansion Factor (default = 6)<br>Linear Bottleneck: ไม่ใช้ ReLU หลัง Projection Layer<br>                   เพื่อรักษาข้อมูลใน low-dim space</div>''', unsafe_allow_html=True)

subhead("3. Transfer Learning Strategy")
body("ใช้ MobileNetV2 pretrained บน <strong style='color:#2d1167;'>ImageNet</strong> (1.28M ภาพ, 1000 คลาส) เป็น Feature Extractor แล้ว Fine-tune เฉพาะ Classification Head สำหรับ 6 คลาส Scene")
st.markdown(f'''<div style="background:#0d1117;border:1px solid #30363d;border-radius:10px;padding:20px 24px;font-family:'Courier New',monospace;font-size:0.82rem;color:#e6edf3;line-height:1.75;margin:12px 0 20px 0;display:block;width:100%;">Phase 1 — Feature Extraction:<br>  base_model.trainable = False   (Freeze all base layers)<br>  Train only: GAP → Dense(256) → Dropout → Softmax(6)<br>  Optimizer: Adam(lr=1e-4)<br><br>Phase 2 — Fine-tuning (optional):<br>  Unfreeze top layers ของ Base Model<br>  Train ด้วย lr ต่ำ (1e-5) เพื่อ fine-tune high-level features</div>''', unsafe_allow_html=True)

subhead("4. Dropout Regularization")
st.markdown(f'''<div style="background:#0d1117;border:1px solid #30363d;border-radius:10px;padding:20px 24px;font-family:'Courier New',monospace;font-size:0.82rem;color:#e6edf3;line-height:1.75;margin:12px 0 20px 0;display:block;width:100%;">During Training:  ปิด Neuron แบบ Random ด้วยความน่าจะเป็น p<br>During Inference: ใช้ทุก Neuron แต่ Scale output ด้วย (1-p)<br><br>ผลลัพธ์: ลด Co-adaptation ของ Neurons → ลด Overfitting<br>โปรเจคนี้ใช้ Dropout Rate = 0.3</div>''', unsafe_allow_html=True)
card_close()

# ══════════════════════════════════════════════════════════════════════════
# TRANSFER LEARNING BENEFITS
# ══════════════════════════════════════════════════════════════════════════
st.markdown(f'<div style="{CARD} {TOP}"><span style="{LABEL}">Transfer Learning</span><h2 style="font-family:\'Syne\',sans-serif; color:#1e0a4a; margin:8px 0 14px 0;">ข้อดีของ Transfer Learning</h2><p style="color:#6b7280; margin-bottom:20px;">การใช้ MobileNetV2 ที่ pretrained บน ImageNet ช่วยลดเวลาและทรัพยากรในการ train อย่างมาก</p>', unsafe_allow_html=True)
tl1,tl2 = st.columns(2, gap="medium"); tl3,tl4 = st.columns(2, gap="medium")
for col,txt in zip([tl1,tl2,tl3,tl4],["⚡ Faster training — ไม่ต้องเรียนรู้ low-level features ใหม่","📈 Higher accuracy — ImageNet features transfer ได้ดี","💾 Less compute — update เฉพาะ Classification Head","🎯 Better generalization — ลด Overfitting บน dataset เล็ก"]):
    with col:
        st.markdown(f'<div style="{HL} margin-bottom:14px;"><p style="margin:0; font-size:0.88rem; color:#4b5563;">{txt}</p></div>', unsafe_allow_html=True)
card_close()

# ══════════════════════════════════════════════════════════════════════════
# DEVELOPMENT STEPS
# ══════════════════════════════════════════════════════════════════════════
st.markdown(f'<div style="{CARD} {TOP}"><span style="{LABEL}">Development</span><h2 style="font-family:\'Syne\',sans-serif; color:#1e0a4a; margin:8px 0 6px 0;">ขั้นตอนการพัฒนาโมเดล</h2><p style="color:#6b7280; margin-bottom:8px;">กระบวนการพัฒนาตั้งแต่การเตรียมข้อมูลจนได้ Neural Network พร้อม Deploy</p>', unsafe_allow_html=True)
nn_steps = [
    ("01","โหลด Dataset และวิเคราะห์","โหลดภาพ Intel Dataset ตรวจสอบ class distribution ดูตัวอย่างภาพแต่ละคลาส"),
    ("02","Data Augmentation Pipeline","ImageDataGenerator(rotation_range=20, zoom_range=0.2, horizontal_flip=True)"),
    ("03","โหลด MobileNetV2 Pretrained","MobileNetV2(weights='imagenet', include_top=False) → base_model.trainable=False"),
    ("04","สร้าง Classification Head","base → GAP → Dense(256, relu) → Dropout(0.3) → Dense(6, softmax)"),
    ("05","Compile","Adam(lr=1e-4), loss='categorical_crossentropy', metrics=['accuracy']"),
    ("06","Train พร้อม Callbacks","fit(train_gen, validation_data=val_gen, epochs=30, callbacks=[EarlyStopping, ModelCheckpoint])"),
    ("07","Evaluate และ Visualize","Test Accuracy, Learning Curves, Confusion Matrix, Grad-CAM"),
    ("08","บันทึกโมเดล","model.save('intel_nn_model_93_9.h5') → Deploy"),
]
for i,(num,title,desc) in enumerate(nn_steps):
    border = "1px solid #f3f4f6" if i < len(nn_steps)-1 else "none"
    st.markdown(f'<div style="display:flex; gap:18px; align-items:flex-start; padding:18px 0; border-bottom:{border};"><div style="font-family:\'Syne\',sans-serif; font-size:1.4rem; font-weight:800; color:#ddd6fe; min-width:38px; line-height:1;">{num}</div><div><div style="font-family:\'Syne\',sans-serif; font-weight:700; color:#2d1167; font-size:0.98rem; margin-bottom:5px;">{title}</div><div style="font-size:0.88rem; color:#6b7280;">{desc}</div></div></div>', unsafe_allow_html=True)
card_close()

# ══════════════════════════════════════════════════════════════════════════
# CODE
# ══════════════════════════════════════════════════════════════════════════
dark_card_open("Implementation", "โค้ดหลักในการสร้างโมเดล")
st.markdown(f'''<div style="background:#0d1117;border:1px solid #30363d;border-radius:10px;padding:20px 24px;font-family:'Courier New',monospace;font-size:0.82rem;color:#e6edf3;line-height:1.75;margin:12px 0 20px 0;display:block;width:100%;"># 1. Load Pretrained Base Model<br>base_model = MobileNetV2(<br>    weights='imagenet',<br>    include_top=False,<br>    input_shape=(224, 224, 3)<br>)<br>base_model.trainable = False   # Freeze base layers<br><br># 2. Build Classification Head<br>x      = base_model.output<br>x      = GlobalAveragePooling2D()(x)<br>x      = Dense(256, activation='relu')(x)<br>x      = Dropout(0.3)(x)<br>output = Dense(6, activation='softmax')(x)<br>model  = Model(inputs=base_model.input, outputs=output)<br><br># 3. Compile<br>model.compile(<br>    optimizer=Adam(learning_rate=1e-4),<br>    loss='categorical_crossentropy',<br>    metrics=['accuracy']<br>)<br><br># 4. Train with Callbacks<br>history = model.fit(<br>    train_generator,<br>    validation_data=val_generator,<br>    epochs=30,<br>    callbacks=[<br>        EarlyStopping(patience=5, restore_best_weights=True),<br>        ModelCheckpoint('best_model.h5', save_best_only=True)<br>    ]<br>)<br><br># 5. Save<br>model.save('intel_nn_model_93_9.h5')</div>''', unsafe_allow_html=True)
card_close()

# ══════════════════════════════════════════════════════════════════════════
# REFERENCES
# ══════════════════════════════════════════════════════════════════════════
card_open("References", "แหล่งอ้างอิง")
nn_refs = [
    ("📦","Dataset","Intel Image Classification Dataset","Kaggle — puneet6060","https://www.kaggle.com/datasets/puneet6060/intel-image-classification"),
    ("📄","Research Paper","MobileNetV2: Inverted Residuals and Linear Bottlenecks","Sandler, M., Howard, A., Zhu, M., Zhmoginov, A., & Chen, L. (2018). CVPR.","https://arxiv.org/abs/1801.04381"),
    ("📄","Research Paper","Grad-CAM: Visual Explanations from Deep Networks via Gradient-based Localization","Selvaraju, R.R. et al. (2017). ICCV.","https://arxiv.org/abs/1610.02391"),
    ("📄","Research Paper","ImageNet Large Scale Visual Recognition Challenge","Russakovsky, O. et al. (2015). IJCV 115(3), 211–252.","https://arxiv.org/abs/1409.0575"),
    ("📄","Research Paper","Dropout: A Simple Way to Prevent Neural Networks from Overfitting","Srivastava, N. et al. (2014). JMLR 15(1), 1929–1958.","https://jmlr.org/papers/v15/srivastava14a.html"),
    ("📄","Research Paper","Adam: A Method for Stochastic Optimization","Kingma, D.P., & Ba, J. (2015). ICLR.","https://arxiv.org/abs/1412.6980"),
    ("🐍","Library","TensorFlow / Keras","Abadi, M. et al. (2015). Google Brain.","https://www.tensorflow.org"),
    ("🐍","Library","OpenCV (cv2) — Grad-CAM Visualization","Bradski, G. (2000). Dr. Dobb's Journal.","https://opencv.org"),
]
for icon,rtype,title,source,url in nn_refs:
    st.markdown(f'<div style="display:flex; gap:16px; align-items:flex-start; padding:14px 0; border-bottom:1px solid #f3f4f6;"><div style="background:#f5f3ff; border:1px solid #ddd6fe; border-radius:8px; padding:8px 10px; font-size:1.1rem; min-width:40px; text-align:center;">{icon}</div><div style="flex:1;"><div style="font-size:0.7rem; color:#a78bfa; text-transform:uppercase; letter-spacing:0.1em; margin-bottom:3px;">{rtype}</div><div style="font-family:\'Syne\',sans-serif; font-weight:700; color:#2d1167; font-size:0.95rem; margin-bottom:3px;">{title}</div><div style="font-size:0.83rem; color:#6b7280; margin-bottom:4px;">{source}</div><a href="{url}" target="_blank" style="font-size:0.8rem; color:#7c3aed; text-decoration:none;">{url}</a></div></div>', unsafe_allow_html=True)
card_close()
