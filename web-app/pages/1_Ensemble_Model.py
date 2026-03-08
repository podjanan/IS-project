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
    <span style="{LABEL}; background:#f5f3ff; padding:6px 16px; border-radius:50px; border:1px solid #ddd6fe;">Model 01 · Ensemble Learning</span>
    <h1 style="font-family:'Syne',sans-serif; font-size:2.8rem; font-weight:800; color:#1e0a4a; margin:14px 0 14px 0; letter-spacing:-0.03em;">Garbage Classification</h1>
    <p style="font-size:1.05rem; color:#6b7280; max-width:580px; margin:0;">
        Automated waste image classification using an ensemble of three machine learning algorithms with deep feature extraction.
    </p>
</div>
""", unsafe_allow_html=True)

s1, s2, s3 = st.columns(3)
for col,(num,lbl) in zip([s1,s2,s3],[("6","Waste Classes"),("3","ML Algorithms"),("82%","Accuracy")]):
    with col:
        st.markdown(f'<div style="{CARD} {TOP} text-align:center; padding:22px 14px;"><div style="font-family:\'Syne\',sans-serif; font-size:2rem; font-weight:800; color:#7c3aed;">{num}</div><div style="font-size:0.74rem; color:#9ca3af; text-transform:uppercase; letter-spacing:0.08em; margin-top:4px;">{lbl}</div></div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════
# OVERVIEW
# ══════════════════════════════════════════════════════════════════════════
st.markdown(f"""
<div style="{CARD} {TOP}">
    <span style="{LABEL}">Overview</span>
    <h2 style="font-family:'Syne',sans-serif; color:#1e0a4a; margin:8px 0 14px 0;">Project Introduction</h2>
    <p style="color:#6b7280; margin:0;">
        This system classifies waste images into recyclable categories to support
        <strong style="color:#2d1167;">automated recycling and waste management pipelines</strong>.
        Traditional sorting relies on manual labor — this model provides a scalable, machine-vision alternative.
        Accurate waste classification is essential for recycling systems, waste management automation, and environmental sustainability.
    </p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════
# DATASET
# ══════════════════════════════════════════════════════════════════════════
st.markdown(f"""
<div style="{CARD} {TOP}">
    <span style="{LABEL}">Data</span>
    <h2 style="font-family:'Syne',sans-serif; color:#1e0a4a; margin:8px 0 14px 0;">Dataset</h2>
    <p style="color:#6b7280; margin-bottom:16px;">
        This model uses the <strong style="color:#2d1167;">Garbage Classification Dataset</strong> — a curated
        collection of real-world waste material images used widely in computer vision research for recycling
        and sustainability applications.
    </p>
    <div style="{HL}">
        <p style="margin:0; font-size:0.9rem; color:#4b5563;">
            📦 Source: <strong style="color:#2d1167;">Kaggle</strong> — Garbage Classification Dataset<br>
            🔗 kaggle.com/datasets/asdasdasasdas/garbage-classification
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════
# CLASSES
# ══════════════════════════════════════════════════════════════════════════
st.markdown(f'<div style="{CARD} {TOP}"><span style="{LABEL}">Categories</span><h2 style="font-family:\'Syne\',sans-serif; color:#1e0a4a; margin:8px 0 20px 0;">Dataset Classes</h2>', unsafe_allow_html=True)
classes = [("📦","Cardboard","Boxes, packaging"),("🫙","Glass","Bottles, jars"),("🥫","Metal","Cans, metal objects"),("📰","Paper","Newspapers, sheets"),("🧴","Plastic","Bottles, bags"),("🗑️","Trash","Non-recyclable waste")]
r1 = st.columns(3, gap="medium"); r2 = st.columns(3, gap="medium")
for col,(icon,name,desc) in zip(list(r1)+list(r2), classes):
    with col:
        st.markdown(f'<div style="background:#faf9ff; border:1px solid #ede9fe; border-radius:12px; padding:18px 20px; margin-bottom:14px;"><div style="font-size:1.6rem; margin-bottom:8px;">{icon}</div><div style="font-family:\'Syne\',sans-serif; font-weight:700; color:#2d1167; font-size:0.95rem;">{name}</div><div style="font-size:0.82rem; color:#9ca3af; margin-top:4px;">{desc}</div></div>', unsafe_allow_html=True)
card_close()

# ══════════════════════════════════════════════════════════════════════════
# PREPROCESSING
# ══════════════════════════════════════════════════════════════════════════
st.markdown(f'<div style="{CARD} {TOP}"><span style="{LABEL}">Pipeline</span><h2 style="font-family:\'Syne\',sans-serif; color:#1e0a4a; margin:8px 0 6px 0;">Data Preprocessing</h2><p style="color:#6b7280; margin-bottom:8px;">Raw images vary in resolution, scale, and structure. A consistent preprocessing pipeline ensures every image is suitable for machine learning.</p>', unsafe_allow_html=True)
steps = [
    ("01","Image Loading","Images are read from class-labelled directories. Each folder name becomes the ground-truth label."),
    ("02","Resizing → 224 × 224 px","All images are resized to 224×224 pixels — the required input shape for MobileNetV2."),
    ("03","Normalization → [0, 1]","Pixel values (0–255) are divided by 255. Improves gradient stability and convergence speed."),
    ("04","Train / Test Split — 80 / 20","80% trains the models. 20% is held out to measure generalization on unseen images."),
]
for i,(num,title,desc) in enumerate(steps):
    border = "1px solid #f3f4f6" if i < len(steps)-1 else "none"
    st.markdown(f'<div style="display:flex; gap:18px; align-items:flex-start; padding:18px 0; border-bottom:{border};"><div style="font-family:\'Syne\',sans-serif; font-size:1.5rem; font-weight:800; color:#ddd6fe; min-width:38px; line-height:1;">{num}</div><div><div style="font-family:\'Syne\',sans-serif; font-weight:700; color:#2d1167; font-size:0.98rem; margin-bottom:5px;">{title}</div><div style="font-size:0.88rem; color:#6b7280;">{desc}</div></div></div>', unsafe_allow_html=True)
card_close()

# ══════════════════════════════════════════════════════════════════════════
# FEATURE EXTRACTION
# ══════════════════════════════════════════════════════════════════════════
st.markdown(f"""
<div style="{CARD} {TOP}">
    <span style="{LABEL}">Feature Extraction</span>
    <h2 style="font-family:'Syne',sans-serif; color:#1e0a4a; margin:8px 0 14px 0;">MobileNetV2 Backbone</h2>
    <p style="color:#6b7280; margin-bottom:16px;">
        Instead of raw pixel inputs, the system uses <strong style="color:#2d1167;">MobileNetV2</strong>
        pretrained on ImageNet (1M+ images, 1000 classes) to extract rich visual representations.
        Output: a compact <strong style="color:#7c3aed;">1280-dimensional feature vector</strong> per image.
    </p>
    <div style="{HL}">
        <p style="margin:0; font-size:0.9rem; color:#4b5563;">
            Hierarchical features: <strong style="color:#2d1167;">edges → textures → shapes → object contours</strong>
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════
# ML ALGORITHMS OVERVIEW
# ══════════════════════════════════════════════════════════════════════════
st.markdown(f'<div style="{CARD} {TOP}"><span style="{LABEL}">Classifiers</span><h2 style="font-family:\'Syne\',sans-serif; color:#1e0a4a; margin:8px 0 20px 0;">Machine Learning Algorithms</h2>', unsafe_allow_html=True)
a1,a2,a3 = st.columns(3, gap="medium")
for col,(icon,name,color,desc) in zip([a1,a2,a3],[
    ("🌲","Random Forest","#7c3aed","Aggregates many decision trees via bagging. Robust to overfitting."),
    ("📐","SVM","#6d28d9","Finds an optimal hyperplane separating classes in high-dimensional space."),
    ("⚡","XGBoost","#5b21b6","Gradient-boosted trees with regularization. State-of-the-art on structured data."),
]):
    with col:
        st.markdown(f'<div style="background:#faf9ff; border:1px solid #ede9fe; border-top:3px solid {color}; border-radius:14px; padding:24px; margin-bottom:14px;"><div style="font-size:1.6rem; margin-bottom:10px;">{icon}</div><div style="font-family:\'Syne\',sans-serif; font-size:1rem; font-weight:700; color:{color}; margin-bottom:8px;">{name}</div><p style="margin:0; font-size:0.87rem; color:#6b7280;">{desc}</p></div>', unsafe_allow_html=True)
card_close()

# ══════════════════════════════════════════════════════════════════════════
# THEORY: RANDOM FOREST
# ══════════════════════════════════════════════════════════════════════════
card_open("Theory · Algorithm 01", "Random Forest — ทฤษฎีและหลักการ")
body("Random Forest เป็นอัลกอริทึมแบบ <strong style='color:#2d1167;'>Ensemble Learning</strong> ที่สร้าง Decision Tree หลายต้นพร้อมกัน แล้วรวมผลลัพธ์ผ่านการโหวต เพื่อให้การทำนายมีความแม่นยำและเสถียรมากกว่าการใช้ Decision Tree เพียงต้นเดียว")

subhead("1. Bootstrap Aggregating (Bagging)")
body("จากชุดข้อมูลขนาด N ตัวอย่าง จะทำการสุ่มข้อมูลแบบ <strong style='color:#2d1167;'>Sampling with Replacement</strong> เพื่อสร้างชุดข้อมูลย่อย B ชุด แต่ละชุดจะถูกนำไป train Decision Tree 1 ต้น แต่ละ node สุ่มเลือกเพียง m = √p features เพื่อลดความสัมพันธ์ระหว่าง Tree")
st.markdown(f'''<div style="background:#0d1117;border:1px solid #30363d;border-radius:10px;padding:20px 24px;font-family:'Courier New',monospace;font-size:0.82rem;color:#e6edf3;line-height:1.75;margin:12px 0 20px 0;display:block;width:100%;">สำหรับ b = 1, 2, ..., B:<br>    1. สุ่ม Bootstrap Sample D_b จาก D (Sampling with Replacement)<br>    2. สร้าง Decision Tree T_b จาก D_b<br>       - แต่ละ node สุ่มเลือก m features (m = √p)<br>       - แบ่ง node ด้วย feature ที่ให้ Information Gain สูงสุด<br><br>ผลลัพธ์: Forest = {{ T_1, T_2, ..., T_B }}</div>''', unsafe_allow_html=True)

subhead("2. Gini Impurity — เกณฑ์การแบ่ง Node")
body("ใช้ Gini Impurity เป็นเกณฑ์ในการแบ่ง Node โดย Gini = 0 คือ node บริสุทธิ์ (ข้อมูลทั้งหมดเป็นคลาสเดียวกัน) และ Gini = 0.5 คือปนเปื้อนสูงสุด")
st.markdown(f'''<div style="background:#0d1117;border:1px solid #30363d;border-radius:10px;padding:20px 24px;font-family:'Courier New',monospace;font-size:0.82rem;color:#e6edf3;line-height:1.75;margin:12px 0 20px 0;display:block;width:100%;">Gini(t) = 1 - Σ p(c|t)²<br><br>เมื่อ p(c|t) = สัดส่วนของคลาส c ใน node t<br>Gini = 0.0  →  node บริสุทธิ์ (pure node)<br>Gini = 0.5  →  node ปนเปื้อนสูงสุด (2 คลาสเท่ากัน)</div>''', unsafe_allow_html=True)

subhead("3. Final Prediction (Majority Vote)")
st.markdown(f'''<div style="background:#0d1117;border:1px solid #30363d;border-radius:10px;padding:20px 24px;font-family:'Courier New',monospace;font-size:0.82rem;color:#e6edf3;line-height:1.75;margin:12px 0 20px 0;display:block;width:100%;">ŷ = argmax_c  Σ(b=1 to B)  I( T_b(x) = c )<br><br>เมื่อ I(·) = Indicator Function<br>คลาสที่ได้รับการโหวตมากที่สุดจาก B Trees คือผลลัพธ์สุดท้าย</div>''', unsafe_allow_html=True)

subhead("4. Out-of-Bag (OOB) Error Estimation")
body("ข้อมูลที่ไม่ถูกสุ่มเลือกใน Bootstrap Sample ประมาณ <strong style='color:#2d1167;'>36.8%</strong> (= 1 − 1/e) จะถูกใช้เป็น Validation Set สำหรับ Tree นั้นโดยอัตโนมัติ ทำให้ Random Forest ประเมินความแม่นยำได้โดยไม่ต้องแบ่ง Validation Set แยกต่างหาก")
card_close()

# ══════════════════════════════════════════════════════════════════════════
# THEORY: SVM
# ══════════════════════════════════════════════════════════════════════════
card_open("Theory · Algorithm 02", "Support Vector Machine (SVM) — ทฤษฎีและหลักการ")
body("SVM เป็นอัลกอริทึม Supervised Learning ที่หา <strong style='color:#2d1167;'>Hyperplane</strong> ที่แบ่งแยกคลาสได้ดีที่สุด โดยเน้นการ <strong style='color:#2d1167;'>Maximize Margin</strong> ระหว่าง Hyperplane กับจุดข้อมูลที่ใกล้ที่สุดของแต่ละคลาส")

subhead("1. Linear SVM — Maximum Margin Hyperplane")
body("กำหนด training data (xᵢ, yᵢ) โดย yᵢ ∈ {-1, +1} SVM หา Hyperplane w·x + b = 0 ที่ Maximize Margin = 2/||w||")
st.markdown(f'''<div style="background:#0d1117;border:1px solid #30363d;border-radius:10px;padding:20px 24px;font-family:'Courier New',monospace;font-size:0.82rem;color:#e6edf3;line-height:1.75;margin:12px 0 20px 0;display:block;width:100%;">Optimization Problem:<br>  minimize:   ½||w||²<br>  subject to: yᵢ(w·xᵢ + b) ≥ 1   สำหรับทุก i<br><br>Margin          = 2 / ||w||<br>Support Vectors = จุดข้อมูลที่อยู่บน margin boundary</div>''', unsafe_allow_html=True)

subhead("2. Soft Margin SVM (C-SVM)")
body("ข้อมูลจริงมักแบ่งแยกสมบูรณ์ไม่ได้ จึงเพิ่ม <strong style='color:#2d1167;'>Slack Variables ξᵢ ≥ 0</strong> และ Parameter C ที่ควบคุม trade-off ระหว่าง margin กับการยอมรับ error")
st.markdown(f'''<div style="background:#0d1117;border:1px solid #30363d;border-radius:10px;padding:20px 24px;font-family:'Courier New',monospace;font-size:0.82rem;color:#e6edf3;line-height:1.75;margin:12px 0 20px 0;display:block;width:100%;">minimize:   ½||w||² + C·Σξᵢ<br>subject to: yᵢ(w·xᵢ + b) ≥ 1 - ξᵢ,   ξᵢ ≥ 0<br><br>C ใหญ่  →  margin แคบ,  overfitting มากขึ้น<br>C เล็ก  →  margin กว้าง, underfitting มากขึ้น</div>''', unsafe_allow_html=True)

subhead("3. Kernel Trick — Non-linear Classification")
body("เมื่อข้อมูลไม่สามารถแบ่งแยกได้เชิงเส้น ใช้ <strong style='color:#2d1167;'>Kernel Function K(xᵢ, xⱼ)</strong> เพื่อแปลงข้อมูลไปยัง Feature Space มิติสูงโดยไม่ต้องคำนวณ Mapping ตรงๆ (Kernel Trick)")
st.markdown(f'''<div style="background:#0d1117;border:1px solid #30363d;border-radius:10px;padding:20px 24px;font-family:'Courier New',monospace;font-size:0.82rem;color:#e6edf3;line-height:1.75;margin:12px 0 20px 0;display:block;width:100%;">Linear:  K(xᵢ, xⱼ) = xᵢ · xⱼ<br>RBF:     K(xᵢ, xⱼ) = exp(-γ||xᵢ - xⱼ||²)   ← ใช้ในโปรเจคนี้<br>Poly:    K(xᵢ, xⱼ) = (γ·xᵢ·xⱼ + r)^d<br><br>RBF Kernel เหมาะกับ feature vector มิติสูง<br>เช่น output ของ MobileNetV2 (1280 มิติ)</div>''', unsafe_allow_html=True)

subhead("4. Multi-class SVM (One-vs-Rest)")
body("สำหรับ 6 คลาส SVM สร้าง Binary Classifier <strong style='color:#2d1167;'>6 ตัว</strong> แต่ละตัวแยกคลาสนั้นออกจากคลาสอื่น คลาสที่ได้คะแนน Decision Function สูงสุดคือผลลัพธ์สุดท้าย")
card_close()

# ══════════════════════════════════════════════════════════════════════════
# THEORY: XGBOOST
# ══════════════════════════════════════════════════════════════════════════
card_open("Theory · Algorithm 03", "XGBoost — ทฤษฎีและหลักการ")
body("XGBoost (eXtreme Gradient Boosting) เป็นอัลกอริทึม <strong style='color:#2d1167;'>Gradient Boosting</strong> ที่สร้าง Decision Tree ทีละต้นแบบ Sequential โดยแต่ละต้นพยายามแก้ไข Error ของต้นก่อนหน้า พร้อม Regularization เพื่อป้องกัน Overfitting")

subhead("1. Gradient Boosting Framework")
st.markdown(f'''<div style="background:#0d1117;border:1px solid #30363d;border-radius:10px;padding:20px 24px;font-family:'Courier New',monospace;font-size:0.82rem;color:#e6edf3;line-height:1.75;margin:12px 0 20px 0;display:block;width:100%;">F_m(x) = F_(m-1)(x) + η · h_m(x)<br><br>เมื่อ  F_m(x)  = โมเดลรวมที่ iteration m<br>       h_m(x)  = Decision Tree ต้นใหม่ที่ fit กับ Residual<br>       η (eta) = Learning Rate<br>       Residual = -∂L/∂F_(m-1)  (Negative Gradient ของ Loss)</div>''', unsafe_allow_html=True)

subhead("2. Objective Function + Regularization")
body("XGBoost เพิ่ม <strong style='color:#2d1167;'>Regularization Term Ω(f)</strong> ใน Objective Function เพื่อควบคุมความซับซ้อนของ Tree โดยตรง ป้องกัน Overfitting")
st.markdown(f'''<div style="background:#0d1117;border:1px solid #30363d;border-radius:10px;padding:20px 24px;font-family:'Courier New',monospace;font-size:0.82rem;color:#e6edf3;line-height:1.75;margin:12px 0 20px 0;display:block;width:100%;">Obj = Σ L(yᵢ, ŷᵢ)  +  Σ Ω(fₖ)<br><br>Ω(f) = γT + ½λ||w||²<br><br>เมื่อ  T  = จำนวน Leaf ของ Tree<br>       γ  = Penalty ต่อ Leaf (ควบคุมความลึก)<br>       λ  = L2 Regularization บน Leaf Weights</div>''', unsafe_allow_html=True)

subhead("3. Second-Order Approximation (Hessian)")
body("จุดเด่นของ XGBoost คือใช้ <strong style='color:#2d1167;'>อนุพันธ์อันดับสอง (Hessian)</strong> ในการ optimize ทำให้แม่นยำและเร็วกว่า Gradient Boosting ทั่วไป")
st.markdown(f'''<div style="background:#0d1117;border:1px solid #30363d;border-radius:10px;padding:20px 24px;font-family:'Courier New',monospace;font-size:0.82rem;color:#e6edf3;line-height:1.75;margin:12px 0 20px 0;display:block;width:100%;">L ≈ Σ [ gᵢ·fₜ(xᵢ) + ½hᵢ·fₜ(xᵢ)² ]  +  Ω(fₜ)<br><br>gᵢ = ∂L/∂ŷᵢ     (First-order gradient)<br>hᵢ = ∂²L/∂ŷᵢ²  (Hessian — Second-order gradient)<br><br>Optimal Leaf Weight:  w*_j = -G_j / (H_j + λ)<br>Optimal Score:        Obj* = -½ Σ G_j²/(H_j + λ) + γT</div>''', unsafe_allow_html=True)

subhead("4. Hyperparameters ที่ใช้ในโปรเจคนี้")
hp_cols = st.columns(3, gap="medium")
for col,(param,val,desc) in zip(hp_cols,[("n_estimators","100","จำนวน Tree ทั้งหมด"),("learning_rate","0.1","Step size การอัพเดท"),("max_depth","6","ความลึกสูงสุดของ Tree")]):
    with col:
        st.markdown(f'<div style="background:#faf9ff; border:1px solid #ede9fe; border-top:3px solid #5b21b6; border-radius:12px; padding:18px; text-align:center; margin-bottom:14px;"><div style="font-family:monospace; font-size:0.85rem; color:#7c3aed; margin-bottom:6px;">{param}</div><div style="font-family:\'Syne\',sans-serif; font-size:1.6rem; font-weight:800; color:#1e0a4a;">{val}</div><div style="font-size:0.8rem; color:#9ca3af; margin-top:4px;">{desc}</div></div>', unsafe_allow_html=True)
card_close()

# ══════════════════════════════════════════════════════════════════════════
# ENSEMBLE
# ══════════════════════════════════════════════════════════════════════════
st.markdown(f"""
<div style="{CARD} {TOP}">
    <span style="{LABEL}">Strategy</span>
    <h2 style="font-family:'Syne',sans-serif; color:#1e0a4a; margin:8px 0 14px 0;">Soft Voting Ensemble</h2>
    <p style="color:#6b7280; margin-bottom:20px;">
        รวมทั้ง 3 โมเดลด้วย <strong style="color:#2d1167;">Soft Voting</strong> — เฉลี่ย Predicted Probability จากทุกโมเดล
        คลาสที่มีค่าเฉลี่ยสูงสุดคือผลลัพธ์สุดท้าย
    </p>
    <div style="background:#f5f3ff; border:1px solid #ddd6fe; border-radius:14px; padding:28px; text-align:center; font-family:'Syne',sans-serif; color:#6d28d9; font-size:1rem; line-height:2.4;">
        Random Forest &nbsp;·&nbsp; SVM &nbsp;·&nbsp; XGBoost<br>↓ ↓ ↓<br>
        Probability Averaging (Soft Vote)<br>↓<br>
        <strong style="color:#1e0a4a;">Final Prediction</strong>
    </div>
</div>
""", unsafe_allow_html=True)

b1,b2,b3 = st.columns(3, gap="medium")
for col,txt in zip([b1,b2,b3],["Higher Accuracy","Better Stability","Generalization"]):
    with col:
        st.markdown(f'<div style="{HL} text-align:center; padding:16px;"><div style="font-size:0.72rem; color:#9ca3af; text-transform:uppercase; letter-spacing:0.08em;">Benefit</div><div style="font-family:\'Syne\',sans-serif; font-weight:700; color:#2d1167; margin-top:6px; font-size:0.95rem;">{txt}</div></div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════
# PERFORMANCE
# ══════════════════════════════════════════════════════════════════════════
st.markdown(f"""
<div style="{CARD} {TOP}">
    <span style="{LABEL}">Results</span>
    <h2 style="font-family:'Syne',sans-serif; color:#1e0a4a; margin:8px 0 20px 0;">Model Performance</h2>
    <div style="display:inline-flex; align-items:center; gap:16px; background:linear-gradient(135deg,#f5f3ff,#ede9fe); border:1px solid #ddd6fe; border-radius:50px; padding:16px 36px;">
        <span style="font-family:'Syne',sans-serif; font-size:2.4rem; font-weight:800; color:#7c3aed; letter-spacing:-0.03em;">82%</span>
        <div>
            <div style="font-size:0.72rem; color:#9ca3af; text-transform:uppercase; letter-spacing:0.08em;">Ensemble Accuracy</div>
            <div style="font-size:0.85rem; color:#6b7280; margin-top:3px;">~82 out of every 100 waste images correctly classified</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════
# DEVELOPMENT STEPS
# ══════════════════════════════════════════════════════════════════════════
st.markdown(f'<div style="{CARD} {TOP}"><span style="{LABEL}">Development</span><h2 style="font-family:\'Syne\',sans-serif; color:#1e0a4a; margin:8px 0 6px 0;">ขั้นตอนการพัฒนาโมเดล</h2><p style="color:#6b7280; margin-bottom:8px;">กระบวนการพัฒนาตั้งแต่ต้นจนได้ Ensemble Model พร้อม Deploy</p>', unsafe_allow_html=True)
dev_steps = [
    ("01","โหลดและตรวจสอบ Dataset","โหลดภาพจาก directory 6 คลาส ตรวจสอบจำนวนภาพต่อคลาส ตรวจหาภาพเสียหาย วิเคราะห์ Class Distribution"),
    ("02","Image Preprocessing","Resize ทุกภาพ 224×224 px, Normalize [0,1], แปลงเป็น NumPy array"),
    ("03","Feature Extraction ด้วย MobileNetV2","MobileNetV2(weights='imagenet', include_top=False, pooling='avg') → Feature Vector 1280 มิติต่อภาพ"),
    ("04","Train/Test Split","train_test_split(stratify=y) — 80% Train / 20% Test"),
    ("05","Train โมเดลทั้ง 3","RandomForestClassifier, SVC(kernel='rbf', probability=True), XGBClassifier บน Training Features"),
    ("06","สร้าง Soft Voting Ensemble","VotingClassifier(voting='soft') รวม 3 โมเดล แล้ว train"),
    ("07","Evaluate","accuracy_score, classification_report, confusion_matrix"),
    ("08","บันทึกโมเดล","joblib.dump() → .pkl พร้อม Deploy"),
]
for i,(num,title,desc) in enumerate(dev_steps):
    border = "1px solid #f3f4f6" if i < len(dev_steps)-1 else "none"
    st.markdown(f'<div style="display:flex; gap:18px; align-items:flex-start; padding:18px 0; border-bottom:{border};"><div style="font-family:\'Syne\',sans-serif; font-size:1.4rem; font-weight:800; color:#ddd6fe; min-width:38px; line-height:1;">{num}</div><div><div style="font-family:\'Syne\',sans-serif; font-weight:700; color:#2d1167; font-size:0.98rem; margin-bottom:5px;">{title}</div><div style="font-size:0.88rem; color:#6b7280;">{desc}</div></div></div>', unsafe_allow_html=True)
card_close()

# ══════════════════════════════════════════════════════════════════════════
# CODE
# ══════════════════════════════════════════════════════════════════════════
dark_card_open("Implementation", "โค้ดหลักในการสร้างโมเดล")
st.markdown(f'''<div style="background:#0d1117;border:1px solid #30363d;border-radius:10px;padding:20px 24px;font-family:'Courier New',monospace;font-size:0.82rem;color:#e6edf3;line-height:1.75;margin:12px 0 20px 0;display:block;width:100%;"># 1. Feature Extraction<br>base_model = MobileNetV2(weights='imagenet', include_top=False, pooling='avg')<br>features   = base_model.predict(X_images)   # shape: (N, 1280)<br><br># 2. Define Individual Models<br>rf  = RandomForestClassifier(n_estimators=100, random_state=42)<br>svm = SVC(kernel='rbf', probability=True, C=1.0)<br>xgb = XGBClassifier(n_estimators=100, learning_rate=0.1, max_depth=6)<br><br># 3. Soft Voting Ensemble<br>ensemble = VotingClassifier(<br>    estimators=[('rf', rf), ('svm', svm), ('xgb', xgb)],<br>    voting='soft'<br>)<br>ensemble.fit(X_train, y_train)<br><br># 4. Evaluate<br>y_pred = ensemble.predict(X_test)<br>print(classification_report(y_test, y_pred))<br><br># 5. Save<br>joblib.dump(ensemble, 'garbage_ensemble_model.pkl')</div>''', unsafe_allow_html=True)
card_close()

# ══════════════════════════════════════════════════════════════════════════
# REFERENCES
# ══════════════════════════════════════════════════════════════════════════
card_open("References", "แหล่งอ้างอิง")
refs = [
    ("📦","Dataset","Garbage Classification Dataset","Kaggle — asdasdasasdas","https://www.kaggle.com/datasets/asdasdasasdas/garbage-classification"),
    ("📄","Research Paper","Random Forests","Breiman, L. (2001). Machine Learning, 45(1), 5–32.","https://doi.org/10.1023/A:1010933404324"),
    ("📄","Research Paper","A Training Algorithm for Optimal Margin Classifiers (SVM)","Boser, B., Guyon, I., & Vapnik, V. (1992). COLT '92.","https://doi.org/10.1145/130385.130401"),
    ("📄","Research Paper","XGBoost: A Scalable Tree Boosting System","Chen, T., & Guestrin, C. (2016). KDD '16.","https://doi.org/10.1145/2939672.2939785"),
    ("🧠","Pretrained Model","MobileNetV2: Inverted Residuals and Linear Bottlenecks","Sandler, M. et al. (2018). CVPR.","https://arxiv.org/abs/1801.04381"),
    ("🐍","Library","Scikit-learn","Pedregosa et al. (2011). JMLR 12, 2825–2830.","https://scikit-learn.org"),
    ("🐍","Library","TensorFlow / Keras","Abadi, M. et al. (2015). Google Brain.","https://www.tensorflow.org"),
    ("🐍","Library","XGBoost","Chen, T. et al. DMLC.","https://xgboost.readthedocs.io"),
]
for icon,rtype,title,source,url in refs:
    st.markdown(f'<div style="display:flex; gap:16px; align-items:flex-start; padding:14px 0; border-bottom:1px solid #f3f4f6;"><div style="background:#f5f3ff; border:1px solid #ddd6fe; border-radius:8px; padding:8px 10px; font-size:1.1rem; min-width:40px; text-align:center;">{icon}</div><div style="flex:1;"><div style="font-size:0.7rem; color:#a78bfa; text-transform:uppercase; letter-spacing:0.1em; margin-bottom:3px;">{rtype}</div><div style="font-family:\'Syne\',sans-serif; font-weight:700; color:#2d1167; font-size:0.95rem; margin-bottom:3px;">{title}</div><div style="font-size:0.83rem; color:#6b7280; margin-bottom:4px;">{source}</div><a href="{url}" target="_blank" style="font-size:0.8rem; color:#7c3aed; text-decoration:none;">{url}</a></div></div>', unsafe_allow_html=True)
card_close()
