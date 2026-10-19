import streamlit as st
import random
import plotly.graph_objects as go

# ---------------- PAGE CONFIG ----------------
st.set_page_config(layout="wide")

# ---------------- CSS ----------------
st.markdown("""
<style>

/* Hide Streamlit default menu & footer */

footer {visibility: hidden;}
#MainMenu {visibility: hidden;}

/* App Background */
.stApp {
    background-color: #0d1117;
}

/* Adjust spacing and width */
.block-container {
    padding-top: 1rem;
    padding-bottom: 2rem;
    max-width: 1050px;
}

/* Sidebar (Bluish like Home) */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0f172a 0%, #1e293b 100%);
}

[data-testid="stSidebar"] * {
    color: #e2e8f0 !important;
}

/* -------- FONT SIZE INCREASE (Zoom Effect) -------- */

/* Base font */
html, body, [class*="css"]  {
    font-size: 18px !important;
}

/* Bigger Title */
h1 {
    font-size: 44px !important;
    font-weight: 700 !important;
}

/* Selectbox text */
div[data-baseweb="select"] {
    font-size: 17px !important;
}

/* Slider label */
.stSlider label {
    font-size: 17px !important;
}

/* Button */
.stButton > button {
    background-color: #10b981;
    color: white;
    font-weight: 600;
    border-radius: 10px;
    padding: 14px 28px;
    border: none;
    transition:0.2s ease;
    font-size: 17px !important;
}

.stButton > button:hover {
    background-color: #059669;
    transform:scale(1.03);
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown(
    "<h1 style='color:#e6edf3;'> Check Your Vehicle's Health</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='font-size:18px; color:#cbd5e1;'>"
    "Please enter the following details below to evaluate your vehicle's battery health."
    "</p>",
    unsafe_allow_html=True
)
st.markdown("Vehicle Information")

# ---------------- FORM ----------------
col1, col2 = st.columns(2)

with col1:
    vehicle_category = st.selectbox(
        "Vehicle Category",
        ["Electric Bike", "Electric Car", "Electric Scooter"]
    )

bike_models = ["Revolt RV400", "Tork Kratos", "Ultraviolette F77"]
car_models = ["Tata Nexon EV", "MG ZS EV", "Hyundai Kona EV", "Mahindra XUV400"]
scooter_models = ["Ola S1 Pro","Ather 450X", "Ather 450S", "TVS iQube", "Bajaj Chetak EV"]

if vehicle_category == "Electric Bike":
    vehicle_options = bike_models
elif vehicle_category == "Electric Car":
    vehicle_options = car_models
else:
    vehicle_options = scooter_models

with col2:
    vehicle_name = st.selectbox("Vehicle Model", vehicle_options)
import os

vehicle_data = {
    "Electric Scooter": {
        "Ather 450X": "assets/ather_450x.jpg",
        "Ather 450S": "assets/ather_450s.jpg",
        "Ola S1 Pro": "assets/ola_s1_pro.jpg",
        "TVS iQube": "assets/tvs_iqube.jpg",
        "Bajaj Chetak EV": "assets/chetak_ev.jpg"
    },
    "Electric Bike": {
        "Revolt RV400": "assets/revolt_rv400.jpg",
        "Tork Kratos": "assets/tork_kratos.jpg",
        "Ultraviolette F77": "assets/ultraviolette_f77.jpg"
    },
    "Electric Car": {
        "Tata Nexon EV": "assets/nexon_ev.jpg",
        "MG ZS EV": "assets/mg_zs_ev.jpg",
        "Hyundai Kona EV": "assets/kona_ev.jpg",
        "Mahindra XUV400": "assets/xuv400.jpg"
    }
}

image_path = vehicle_data[vehicle_category][vehicle_name]

if os.path.exists(image_path):
    st.image(image_path, width=700)
else:
    st.warning("⚠ Image not found. Check file name in assets folder.")
st.caption("⚠️ This image is for reference purposes only. The actual vehicle appearance may vary.")
st.markdown("---")
st.markdown("Usage Details")
charging_range = st.selectbox(
    "Charging Range Habit",
    ["0–100% Regularly", "20–80% Mostly", "Mixed"]
)
col3, col4 = st.columns(2)


with col3:
    charging_frequency = st.selectbox(
        "Charging Frequency",
        ["Daily", "Alternate Days", "Weekly"]
    )
with col4:
    fast_charging = st.selectbox(
        "Fast Charging Usage",
        ["Rarely", "Sometimes", "Frequently"]
    )
with col3:
    climate_condition = st.selectbox(
        "Climate Condition",
        ["Cool", "Moderate", "Hot"]
    )

vehicle_age = st.slider("Vehicle Age (Years)", 0, 30, 2)
# Total Charging Cycles (manual entry first)
charging_cycles = st.slider(
    "Total Charging Cycles",
    min_value=0,
    max_value=2000,
    value=300,
    step=50
)

# Checkbox placed AFTER slider
estimate_cycles = st.checkbox(
    "I don’t know total charging cycles (Estimate automatically)"
)

# If user selects estimate, override manual value
if estimate_cycles:

    if charging_frequency == "Daily":
        freq_factor = 365
    elif charging_frequency == "Alternate Days":
        freq_factor = 180
    else:
        freq_factor = 52

    charging_cycles = vehicle_age * freq_factor
    st.info(f"Estimated Charging Cycles: {charging_cycles}")

avg_travel = st.slider("Average Daily Travel (km)", 0, 100, 25)

    # ----------- PREDICTION -----------
st.markdown("---")
if st.button("Predict Battery Health"):
        st.divider()

        max_cycles = 1000

        # Health based on cycles
        health_from_cycles = 100 - (charging_cycles / max_cycles) * 100

        # Health based on age
        health_from_age = 100 - (vehicle_age * 5)

        # Combine both
        soh = (health_from_cycles + health_from_age) / 2

      # Limit between 0 and 100
        soh = max(0, min(soh, 100))
        st.markdown("<br>", unsafe_allow_html=True)
        st.subheader("🔋 Battery Health Result")

        st.progress(int(soh))

        st.metric("Battery Health (SOH)", f"{soh:.1f}%")

        # Condition status
        if soh >= 80:
            st.success("🔋 Battery is in Excellent Condition")
        elif soh >= 60:
            st.warning("⚡ Battery Health is Average – Monitor usage")
        else:
            st.error("⚠ Battery Health is Poor – " \
            "Recommended Action : " \
            "Consider battery inspection or replacement within next 12 months.")
        base_range = 300
        estimated_range = base_range * (soh / 100)

        st.subheader("Estimated Driving Range")
        st.info(f"Approx Range: {estimated_range:.0f} km")

        remaining_cycles = max_cycles * (soh / 100)

        st.subheader("Remaining Useful Life")

        st.write(f"Estimated Remaining Cycles: {remaining_cycles:.0f} cycles")

        years_left = remaining_cycles / 300

        st.write(f"Estimated Remaining Life: {years_left:.1f} years")

        st.divider()

        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=soh,
            title={'text': "Battery Health Gauge"},
            gauge={
                'axis': {'range': [0, 100]},
                'bar': {'color': "lightgreen"},
                'steps': [
                    {'range': [0, 40], 'color': "red"},
                    {'range': [40, 70], 'color': "orange"},
                    {'range': [70, 100], 'color': "green"}
            ]
        }
    ))

        st.plotly_chart(fig, use_container_width=True)