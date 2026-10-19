import streamlit as st

st.set_page_config(layout="wide")

# ---------- SIDEBAR STYLE ----------
st.markdown("""
<style>

/* Sidebar Gradient */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0f172a 0%, #1e293b 100%);
}

[data-testid="stSidebar"] * {
    color: white !important;
}

/* Font Size */
html, body, [class*="css"] {
    font-size: 18px;
}

</style>
""", unsafe_allow_html=True)

# ---------- PAGE TITLE ----------
st.title("📘 About This Project")

st.markdown(
"""
<h3 style='color:#38bdf8'>
Project Title:
Data-Driven Diagnostics and Advanced Modeling for Robust State of Health Estimation in EV Batteries
</h3>
""",
unsafe_allow_html=True
)

st.markdown(
"""
<p style='font-size:18px; color:#cbd5e1;'>
This project focuses on predicting and monitoring the health of Electric Vehicle (EV) batteries using data-driven techniques. 
The system helps EV users understand battery condition, estimate remaining battery life, detect potential issues early, 
and locate nearby EV service centers when maintenance is required.
</p>
""",
unsafe_allow_html=True
)

st.markdown("---")

# ---------- PROJECT OBJECTIVE ----------
st.header("🎯 Project Objective")

st.write("""
The primary objective of this project is to develop an intelligent system that can estimate the 
State of Health (SoH) of electric vehicle batteries using machine learning and data analytics. 
By analyzing battery datasets and user inputs, the system provides insights that help improve battery 
maintenance, reliability, and overall EV performance.
""")

# ---------- PROJECT OVERVIEW ----------
st.header("🔋 Project Overview")

st.write("""
Electric vehicles rely heavily on battery performance. Battery degradation over time can reduce 
vehicle range, efficiency, and reliability. 

This system analyzes battery behavior using historical data and predictive modeling techniques. 
It provides battery health estimation, diagnostics, and maintenance recommendations that help EV 
owners maintain their vehicles efficiently and extend battery lifespan.
""")

# ---------- SYSTEM MODULES ----------
st.header("⚙ System Modules")

st.write("""
• **Daily Battery Health Check** – Estimates battery health based on input parameters  
• **Advanced Battery Diagnostics** – Uses uploaded datasets for deeper battery analysis  
• **State of Health (SoH) Prediction** – Predicts remaining battery performance using ML models  
• **Range Estimation** – Estimates available driving range based on battery condition  
• **Remaining Useful Life (RUL)** – Predicts remaining battery cycles and lifespan  
• **EV Service Locator** – Helps users find nearby EV service and repair centers  
""")

# ---------- TECHNOLOGIES USED ----------
st.header("🛠 Technologies Used")

st.write("""
• **Python** – Core programming language  
• **Streamlit** – Web interface for interactive dashboards  
• **Machine Learning** – Battery health prediction models  
• **Pandas & NumPy** – Data processing and analysis  
• **Geopy** – Location and distance calculations  
• **PyDeck / Map Visualization** – Display nearby EV service centers on maps  
""")

# ---------- DATA ANALYSIS APPROACH ----------
st.header("📊 Data Analysis Approach")

st.write("""
The system uses battery cycle datasets to analyze patterns related to battery degradation. 
Machine learning models are applied to predict the battery's State of Health (SoH) and estimate 
remaining useful life. These predictions help identify early warning signs of battery performance decline.
""")

# ---------- FUTURE IMPROVEMENTS ----------
st.header("🚀 Future Improvements")

st.write("""
• Real-time battery monitoring using IoT sensors  
• Integration with official EV manufacturer diagnostic systems  
• Cloud-based battery data storage and analytics  
• Mobile application for real-time monitoring  
• AI-based predictive maintenance recommendations  
""")

st.markdown("---")

st.success("Developed as part of a Final Year Engineering Project on Electric Vehicle Battery Diagnostics and Health Prediction.")