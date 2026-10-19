import streamlit as st
import pandas as pd
import pydeck as pdk
from geopy.distance import geodesic
from geopy.geocoders import Nominatim
from streamlit_geolocation import streamlit_geolocation

ev_data = pd.read_csv("ev_service_centers.csv")

st.set_page_config(layout="wide")

# ------------------- STYLE -------------------

st.markdown("""
<style>
[data-testid="stSidebar"] {
background: linear-gradient(180deg,#1f2937 0%,#111827 100%);
}

.block-container {
padding-top:2rem;
}

h1 {
font-size:40px !important;
font-weight:700;
}

.stButton>button {
background:#16a34a;
color:white;
border-radius:8px;
}
</style>
""", unsafe_allow_html=True)

# ------------------- TITLE -------------------

st.title("⚡ Find Nearby EV Services")
st.caption("Locate EV charging stations and repair centers near you")
st.divider()

# ------------------- SEARCH RADIUS -------------------

radius = st.slider("Search Radius (km)", 5, 200, 50)

# ------------------- LOCATION OPTIONS -------------------

st.subheader("📍 Choose Location Method")

tab1, tab2, tab3 = st.tabs(["🔎 Search Location", "🏙 Select City", "📍 Detect GPS"])

# ------------------- SESSION STATE -------------------

if "user_lat" not in st.session_state:
    st.session_state.user_lat = None
    st.session_state.user_lon = None

centers = []

# ------------------- SEARCH LOCATION -------------------

with tab1:

    search_place = st.text_input("Enter city or area (Example: Bangalore, Tirupati)")

    if st.button("Search Location"):

        geolocator = Nominatim(user_agent="ev_locator")
        location = geolocator.geocode(search_place)

        if location:
            st.session_state.user_lat = location.latitude
            st.session_state.user_lon = location.longitude
            st.success(f"Showing EV services near {search_place}")
        else:
            st.warning("Location not found.")

# ------------------- CITY DATA -------------------

city_coords = {
"Bangalore": (12.9716,77.5946),
"Hyderabad": (17.3850,78.4867),
"Chennai": (13.0827,80.2707),
"Mumbai": (19.0760,72.8777),
"Delhi": (28.7041,77.1025),
"Tirupati": (13.6288,79.4192),
"Chittoor": (13.2172,79.1003),
"Palamaner": (13.2000,78.7500),
"Vellore": (12.9165,79.1325)
}

# ------------------- CITY SELECTION -------------------

with tab2:

    city = st.selectbox(
        "Select City",
        ["Select a city","Bangalore","Hyderabad","Chennai","Mumbai","Delhi","Tirupati","Chittoor","Palamaner","Vellore"]
    )

    if st.button("Find Services") and city != "Select a city":

        st.session_state.user_lat, st.session_state.user_lon = city_coords[city]
        st.success(f"Showing EV services in {city}")

# ------------------- GPS DETECTION -------------------

with tab3:

    if st.button("Detect My Location"):

        location_data = streamlit_geolocation()

        if location_data and location_data["latitude"]:

            st.session_state.user_lat = location_data["latitude"]
            st.session_state.user_lon = location_data["longitude"]

            user_lat = st.session_state.user_lat
            user_lon = st.session_state.user_lon

            geolocator = Nominatim(user_agent="ev_locator")
            location = geolocator.reverse((user_lat, user_lon), language="en")

            if location:
                address = location.raw["address"]

                place = (
                    address.get("city")
                    or address.get("town")
                    or address.get("village")
                    or address.get("state_district")
                )

                st.success(f"📍 Your Location: {place}")

        else:
            st.warning("Allow browser GPS access.")

# ------------------- GET USER LOCATION -------------------

user_lat = st.session_state.user_lat
user_lon = st.session_state.user_lon

# ------------------- FIND NEARBY SERVICES -------------------

if user_lat:

    with st.spinner("Finding nearby EV service centers..."):

        for _, row in ev_data.iterrows():

            lat = row["lat"]
            lon = row["lon"]

            distance = round(
                geodesic((user_lat, user_lon), (lat, lon)).km,
                2
            )

            if distance <= radius:

                centers.append({
                    "name": row["name"],
                    "lat": lat,
                    "lon": lon,
                    "distance": distance,
                    "address": row["address"]
                })

centers = sorted(centers, key=lambda x: x["distance"])

# ------------------- MAP -------------------

if user_lat and len(centers) > 0:

    df = pd.DataFrame(centers)

    service_layer = pdk.Layer(
        "ScatterplotLayer",
        data=df,
        get_position='[lon,lat]',
        get_color='[0,200,140,200]',
        get_radius=600
    )

    user_layer = pdk.Layer(
        "ScatterplotLayer",
        data=[{"lat": user_lat, "lon": user_lon}],
        get_position='[lon,lat]',
        get_color='[0,0,255,200]',
        get_radius=900
    )

    view = pdk.ViewState(
        latitude=user_lat,
        longitude=user_lon,
        zoom=12
    )

    deck = pdk.Deck(
        layers=[service_layer, user_layer],
        initial_view_state=view,
        tooltip={"text": "{name}\nDistance: {distance} km"}
    )

    st.pydeck_chart(deck,use_container_width=True)

# ------------------- SERVICE LIST -------------------

st.subheader("⚡ Nearby EV Service & Repair Centers")

if len(centers) > 0:

    st.info(f"{len(centers)} EV service centers found near you")

    nearest = centers[0]
    st.success(f"⭐ Nearest EV Service: {nearest['name']} ({nearest['distance']} km away)")

    for i, shop in enumerate(centers[:10]):

        col1, col2 = st.columns([1,5])

        with col1:
            st.image(
                "https://cdn-icons-png.flaticon.com/512/3202/3202926.png",
                width=70
            )

        with col2:

            st.markdown(f"### {shop['name']}")
            st.markdown(f"📍 **{shop['distance']} km away**")
            st.caption(shop["address"])

            colA, colB, colC = st.columns(3)

            with colA:
                st.button("📞 Call", disabled=True, key=f"call_{i}")

            with colB:
                st.link_button(
                    "🧭 Directions",
                    f"https://www.google.com/maps/dir/?api=1&destination={shop['lat']},{shop['lon']}"
                )

            with colC:
                st.link_button(
                    "📍 View Map",
                    f"https://www.google.com/maps/search/?api=1&query={shop['lat']},{shop['lon']}"
                )

        st.divider()      

else:
    if user_lat:
        st.warning("⚠️ No EV service centers found nearby.")

# ------------------- FOOTER -------------------

st.caption("EV Service Locator System | B.Tech Final Year Project | Developed using Streamlit, Python, Geopy and PyDeck")