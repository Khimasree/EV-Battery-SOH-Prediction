import streamlit as st
import base64

st.set_page_config(
    page_title="EV Battery Health System",
    page_icon="🔋",
    layout="wide"
)


    
# ---------- LOAD IMAGE ----------
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

img_base64 = get_base64_image("assets/hero.jpg")
features_img = get_base64_image("assets/vehicle_bg.jpg")

# ---------- GLOBAL STYLING ------#

st.markdown("""
<style>

/* Remove ALL default padding */
.block-container {
    padding: 0rem 0rem 0rem 0rem !important;
}

/* Remove main container margin */
section.main > div {
    padding-left: 0rem !important;
    padding-right: 0rem !important;
    max-width: 100% !important;
}

<style>

/* ===== Remove default padding ===== */
section.main > div {
    padding-left: 0rem !important;
    padding-right: 0rem !important;
    max-width: 100% !important;
}

/* ===== SIDEBAR FULL STYLING ===== */

/* Sidebar background */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0b1220 0%, #0f172a 50%, #111827 100%) !important;
    border-right: 1px solid #1F2937 !important;
}

/* Sidebar buttons */
[data-testid="stSidebar"] button {
    border-radius: 10px !important;
    padding: 10px 14px !important;
    transition: 0.2s ease !important;
}

/* Hover effect */
[data-testid="stSidebar"] button:hover {
    background-color: #1F2937 !important;
}

/* Active page highlight */
[data-testid="stSidebar"] button[aria-selected="true"] {
    background-color: #1F2937 !important;
    border-left: 4px solid #4CAF50 !important;
    font-weight: 600 !important;
}
.features-section{

background-size: cover;
background-position: center;
filter:brightness(1.1);
background-repeat: no-repeat;
min-height: 75vh;
display:flex;
align-items:center;
justify-content:center;
padding:120px 40px;
position:relative;
margin-top:0px;
overflow:hidden;
}

.features-section::before{
content:"";
position:absolute;
top:0;
left:0;
width:100%;
height:100%;
background:rgba(0,0,0,0.45);
}

.features-content{
position:relative;
z-index:2;
}

</style>
""", unsafe_allow_html=True)

# ---------- HERO SECTION ----------
hero_html = f"""
<style>
.hero {{
    position: relative;   /* 🔥 changed from fixed */
    width: 100%;
    height: 100vh;
    background-image: url("data:image/jpeg;base64,{img_base64}");
    background-size: cover;
    background-position: center;
}}

.hero::before {{
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 55%;
    height: 100%;
    background: linear-gradient(to right, rgba(0,0,0,0.65), rgba(0,0,0,0.15));
}}

.overlay {{
    position: absolute;
    top: 40%;
    left: 8%;
    color: white;
    z-index: 2;
}}

.small-text {{
    font-size: 14px;
    letter-spacing: 7px;
    font-weight: 600;
    margin-bottom: 20px;
}}

.main-title {{
    font-size: 80px;
    font-weight: 900;
    line-height: 1.05;
}}

.sub-text {{
    font-size: 22px;
    margin-top: 30px;
    margin-bottom: 45px;
}}

.gold-btn {{
    background:linear-gradient(135deg,#FFD700,#c9a227);
    padding:18px 45px;
    border-radius:6px;
    box-shadow:0 10px 30px rgba(0,0,0,0.5);
    color: black;
    font-weight: bold;
    text-decoration: none;
    font-size: 16px;
    letter-spacing: 2px;
}}

</style>

<div class="hero">
    <div class="overlay">
        <div class="small-text">A POWERFUL EV BATTERY HEALTH MONITORING PLATFORM</div>
        <div class="main-title">
            BATTERY HEALTH<br>
            PREDICTION ENGINE
        </div>
        <div class="sub-text">
            Accurate battery health analysis made simple
        </div>
        <a href="/Daily_Health_Check" target="_self" class="gold-btn">
    BEGIN ANALYSIS 
</a>
    </div>
</div>
"""

st.markdown(hero_html, unsafe_allow_html=True)


# ---------- FEATURE SECTION ----------



st.markdown("""
<style>

.section-title{
    text-align:center;
    font-size:40px;
    font-weight:800;
    margin-bottom:40px;
}

.feature-box{
    background:#111827;
    padding:30px;
    border-radius:12px;
    text-align:center;
    border:1px solid #1f2937;
    backdrop-filter: blur(8px);
    background: rgba(17,24,39,0.75);
}

.feature-icon{
    font-size:40px;
}

.feature-title{
    font-size:22px;
    font-weight:700;
    margin-top:10px;
}

.feature-desc{
    font-size:16px;
    opacity:0.8;
    margin-top:10px;
}

.tech-box{
    background:#0f172a;
    padding:18px 28px;
    border-radius:8px;
    border:1px solid #1f2937;
    text-align:center;
    font-weight:600;
}
.tech-box:hover{
transform:translateY(-4px);
transition:0.25s;
box-shadow:0 10px 25px rgba(0,0,0,0.5);
}

.footer{
    text-align:center;
    opacity:0.7;
    margin-top:60px;
    padding:20px;
}
.feature-box:hover{
transform: translateY(-6px);
transition:0.3s;
box-shadow:0 12px 30px rgba(0,0,0,0.6);
}

</style>
""", unsafe_allow_html=True)

st.markdown('<div class="features-section"><div class="features-content">', unsafe_allow_html=True)
st.markdown(f"""
<style>
.features-section {{
background-image: url("data:image/jpeg;base64,{features_img}");
background-size: cover;
background-position: center;
background-repeat: no-repeat;
}}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="section-title">⚡ System Features</div>', unsafe_allow_html=True)

col1,col2,col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-box">
        <div class="feature-icon">🔋</div>
        <div class="feature-title">Battery Health Prediction</div>
        <div class="feature-desc">
        Predict EV battery condition using intelligent analysis and health indicators.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-box">
        <div class="feature-icon">📊</div>
        <div class="feature-title">Advanced Diagnostics</div>
        <div class="feature-desc">
        Upload battery datasets and perform deeper analytics on battery behaviour.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-box">
        <div class="feature-icon">📍</div>
        <div class="feature-title">EV Service Locator</div>
        <div class="feature-desc">
        Detect your location and find nearby EV service and repair centers instantly.
        </div>
    </div>
    """, unsafe_allow_html=True)
st.markdown("</div></div>", unsafe_allow_html=True)


# ---------- WHY SYSTEM SECTION ----------

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown('<div class="section-title">🚗 Why This System</div>', unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center;font-size:18px;max-width:900px;margin:auto;opacity:0.85;">
Electric vehicles rely heavily on battery performance. This system helps EV owners monitor
battery health, detect possible degradation early, and find nearby service centers when maintenance is required.
It combines battery diagnostics, predictive analysis, and geolocation services into one integrated platform.
</div>
""", unsafe_allow_html=True)


# ---------- TECHNOLOGY STACK ----------

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown('<div class="section-title">⚙ Technology Stack</div>', unsafe_allow_html=True)

c1,c2,c3,c4,c5 = st.columns(5)

with c1:
    st.markdown('<div class="tech-box">Python</div>', unsafe_allow_html=True)

with c2:
    st.markdown('<div class="tech-box">Streamlit</div>', unsafe_allow_html=True)

with c3:
    st.markdown('<div class="tech-box">Pandas</div>', unsafe_allow_html=True)

with c4:
    st.markdown('<div class="tech-box">Geopy</div>', unsafe_allow_html=True)

with c5:
    st.markdown('<div class="tech-box">PyDeck</div>', unsafe_allow_html=True)


# ---------- FOOTER ----------

st.markdown("""
<div class="footer">
EV Battery Health Prediction System | B.Tech Final Year Project<br>
Developed using Streamlit, Python, Geopy and Data Analytics
</div>
""", unsafe_allow_html=True)