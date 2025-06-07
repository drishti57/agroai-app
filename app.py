import streamlit as st

# Background image using custom HTML and CSS
page_bg_img = '''
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://i.imgur.com/Ula4IwV.jpg");
background-size: cover;
background-position: center;
background-repeat: no-repeat;
}
[data-testid="stHeader"] {
background: rgba(0,0,0,0);
}
[data-testid="stToolbar"] {
right: 2rem;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)
import streamlit as st
from PIL import Image

# Title
st.title("🌾 AgroAI – Smart Farming Assistant")
st.subheader("Empowering Farmers with AI for Viksit Bharat 🇮🇳")

# Section 1: Crop Recommendation
st.header("📌 Crop Recommendation")

soil = st.selectbox("Select Soil Type", ["Black", "Red", "Alluvial", "Laterite"])
rain = st.selectbox("Expected Rainfall", ["Low", "Medium", "High"])
season = st.selectbox("Season", ["Rabi", "Kharif", "Zaid"])

if st.button("Get Recommended Crop"):
    if soil == "Black" and rain == "High":
        st.success("🌱 Recommended Crop: Cotton or Soybean")
    elif soil == "Alluvial" and season == "Rabi":
        st.success("🌾 Recommended Crop: Wheat or Barley")
    else:
        st.success("🌽 Recommended Crop: Maize or Pulses")

# Section 2: Disease Detection
st.header("📷 Crop Disease Detection (Demo)")

uploaded_file = st.file_uploader("Upload a crop image (leaf/plant)", type=["jpg", "png", "jpeg"])
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Crop Image", use_column_width=True)
    st.info("🧠 AI says: Detected Leaf Spot Disease")
    st.write("💡 Advice: Spray Neem Oil or use organic fungicide.")

# Section 3: Market Price Info
st.header("📈 Market Price Info (Sample Data)")

crop_selected = st.selectbox("Select Crop", ["Wheat", "Rice", "Tomato", "Onion", "Potato"])
market_data = {
    "Wheat": "₹22/kg",
    "Rice": "₹28/kg",
    "Tomato": "₹18/kg",
    "Onion": "₹14/kg",
    "Potato": "₹12/kg"
}
if crop_selected:
    st.success(f"Current Price of {crop_selected}: {market_data[crop_selected]}")
st.subheader("🌾 Fertilizer Recommendation")
crop_type = st.selectbox("Select Crop", ["Wheat", "Rice", "Maize", "Sugarcane"])
soil_type = st.selectbox("Select Soil Type", ["Sandy", "Loamy", "Clay", "Black", "Red"])

if st.button("Suggest Fertilizer"):
    if crop_type == "Wheat" and soil_type == "Loamy":
        st.success("Use Nitrogen-Phosphorus-Potassium (NPK) fertilizer")
    elif crop_type == "Rice":
        st.success("Use Urea and DAP")
    elif crop_type == "Maize":
        st.success("Use Nitrogen-rich fertilizers like Urea")
    elif crop_type == "Sugarcane":
        st.success("Use Potash-rich fertilizers")
    else:
        st.info("Use general organic compost as base")

# Footer
st.markdown("---")
st.write("Made by Indian Youth 🇮🇳 | Powered by Science & Innovation")