import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.graph_objects as go

st.set_page_config(layout="wide")

# ===============================
# PREMIUM CSS
# ===============================
st.markdown("""
<style>

/* Page background */
body {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
}

.big-title {
    font-size: 34px;
    font-weight: 700;
    color: #ffffff;
}

/* Sidebar styling */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #1f2937 0%, #111827 100%);
}

[data-testid="stSidebar"] * {
    color: white !important;
}

/* Section Divider */
.section-divider {
    border-top: 1px solid rgba(255,255,255,0.1);
    margin: 35px 0;
}

.section-title {
    font-size: 22px;
    font-weight: 600;
    color: #00E5FF;
    margin-top: 30px;
}

.metric-card {
    background-color: rgba(255,255,255,0.05);
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.3);
    margin-bottom: 20px;
}

</style>
""", unsafe_allow_html=True)

st.title("Advanced Battery Diagnostics")

st.markdown("""
Please visit your nearby EV technician to export and upload your vehicle’s battery dataset for advanced diagnostics.
""")

st.markdown("---")

uploaded_file = st.file_uploader(
    "Upload Battery Dataset (CSV only, Max 50MB)",
    type=["csv"]
)

# ===============================
# RUN ONLY AFTER FILE UPLOAD
# ===============================
if uploaded_file is not None:

    with st.spinner("Analyzing your battery data... Please wait."):

        df = pd.read_csv(uploaded_file)

        # Cleaning
        df.drop_duplicates(inplace=True)
        df.dropna(inplace=True)

        # Feature Engineering
        df["capacity_fade"] = 1 - df["capacity"]
        df["volt_temp_interaction"] = df["voltage"] * df["temperature"]
        df["cycle_squared"] = df["cycle"] ** 2
        df["deg_rate"] = df["capacity_fade"] / df["cycle"]
        df["deg_rate"].replace([np.inf, -np.inf], 0, inplace=True)

        features = [
            "cycle",
            "voltage",
            "temperature",
            "capacity",
            "capacity_fade",
            "volt_temp_interaction",
            "cycle_squared",
            "deg_rate"
        ]

        X = df[features]

        # Load Models
        soh_model = joblib.load("battery_soh_model.pkl")
        rul_model = joblib.load("battery_rul_model.pkl")

        # Predictions
        df["Predicted_SOH"] = soh_model.predict(X)
        df["Predicted_RUL"] = rul_model.predict(X)

        latest = df.iloc[-1]

        health = round(latest["Predicted_SOH"] * 100, 2)
        cycles_model = round(latest["Predicted_RUL"])

    # ===============================
    # BATTERY HEALTH OVERVIEW
    # ===============================
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    st.markdown('<p class="section-title">Battery Health Overview</p>', unsafe_allow_html=True)

    st.markdown(f"""
    <h1 style='text-align:center;color:#00E5FF;font-size:50px'>
    Battery Health: {health:.2f}%
    </h1>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="metric-card">
    <h3 style='color:#00E5FF;'>Vehicle Impact Analysis</h3>
    <p style='color:white; font-size:16px;'>
    Battery health at <b>{health:.2f}%</b> ensures optimal vehicle performance,
    stable acceleration, and maintained driving efficiency.
    </p>
    </div>
    """, unsafe_allow_html=True)

    if health >= 80:
        st.success("Condition: Good – No immediate repair required.")
        status_label = "Good"
        bar_color = "#38A169"
    elif health >= 60:
        st.warning("Condition: Average – Maintenance recommended.")
        status_label = "Average"
        bar_color = "#D69E2E"
    else:
        st.error("Condition: Bad – Immediate inspection required.")
        status_label = "Bad"
        bar_color = "#E53E3E"

    avg_temp = df["temperature"].mean()

    st.markdown('<div class="section-title">🌡 Battery Temperature Status</div>', unsafe_allow_html=True)

    if avg_temp > 45:
        st.error("High thermal stress detected. Risk of accelerated degradation.")
    elif avg_temp > 35:
        st.warning("Moderate thermal exposure observed.")
    else:
        st.success("Thermal conditions within safe operating limits.")

    # ==============================
    # 🚗 Driving Range Estimation
    # ==============================
    st.markdown('<div class="section-title">🛣 Estimated Driving Range</div>', unsafe_allow_html=True)

    base_range = 300
    estimated_range = int((health / 100) * base_range)

    st.markdown(f"""
    <div class="metric-card">
    <h3 style='color:white;'>Estimated Available Range</h3>
    <h1 style='color:#00E5FF; font-size:40px;'>{estimated_range} km</h1>
    </div>
    """, unsafe_allow_html=True)

    degraded = 100 - health

    fig = go.Figure(data=[go.Pie(
        labels=['Healthy', 'Degraded'],
        values=[health, degraded],
        hole=.75,
        marker=dict(colors=["#4FD1C5", "#2D3748"])
    )])

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(t=0, b=0, l=0, r=0)
    )

    st.plotly_chart(fig, use_container_width=True)

    # ===============================
    # REMAINING USEFUL LIFE
    # ===============================
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    st.markdown('<p class="section-title">⏳ Remaining Useful Life</p>', unsafe_allow_html=True)

    remaining_cycles = max(0, int(cycles_model))

    max_design_cycles = 1000
    remaining_cycles = int((health / 100) * max_design_cycles)

    rul_percentage = (remaining_cycles / max_design_cycles) * 100

    st.markdown(f"### Estimated Remaining Cycles: **{remaining_cycles} cycles**")
    st.markdown(f"### RUL Percentage: **{rul_percentage:.2f}%**")

    st.markdown("### ⚠ Battery Risk Level")

    if health >= 80:
        st.success("Low Risk – Battery operating normally")
    elif health >= 60:
        st.warning("Moderate Risk – Monitor battery health")
    else:
        st.error("High Risk – Battery replacement may be required")

    if rul_percentage >= 60:
        st.success("Battery life expectancy is strong.")
    elif rul_percentage >= 30:
        st.warning("Battery entering mid-life phase.")
    else:
        st.error("Battery approaching end-of-life.")

    # ===============================
    # HEALTH CLASSIFICATION BAR
    # ===============================
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    st.markdown('<p class="section-title">📊 Health Classification</p>', unsafe_allow_html=True)

    score_bar = f"""
    <div style='margin-top:10px;'>
        <div style='width:100%; background:#2D3748; height:14px; border-radius:10px;'>
            <div style='width:{health}%; background:{bar_color}; height:14px; border-radius:10px;'></div>
        </div>
        <div style='margin-top:8px; font-weight:600;'>{status_label}</div>
    </div>
    """

    st.markdown(score_bar, unsafe_allow_html=True)

    # ===============================
    # RECOMMENDATIONS
    # ===============================
    st.markdown('<div class="section-title">🛠 Recommended Maintenance</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="metric-card">
    <ul style='color:white; font-size:16px;'>
    <li>Maintain charge between 20% and 80%</li>
    <li>Avoid frequent fast charging</li>
    <li>Prevent exposure to extreme temperatures</li>
    <li>Schedule battery health diagnostics every 6 months</li>
    <li>Update vehicle firmware regularly</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    # =================================
    # Battery Replacement Estimate
    # =================================
    st.markdown('<div class="section-title">🔋 Battery Replacement Estimate</div>', unsafe_allow_html=True)

    max_years = 8
    remaining_years = (health / 100) * max_years
    replacement_cost = 80000

    st.markdown(f"""
    <div class="metric-card">
    <h3 style='color:white;'>Estimated Remaining Battery Life</h3>
    <h1 style='color:#00E5FF;'>{remaining_years:.1f} years</h1>

    <h3 style='color:white;'>Estimated Replacement Cost</h3>
    <h1 style='color:#00E5FF;'>₹{replacement_cost:,}</h1>
    </div>
    """, unsafe_allow_html=True)