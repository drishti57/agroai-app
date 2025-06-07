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

# Footer
st.markdown("---")
st.write("Made by Indian Youth 🇮🇳 | Powered by Science & Innovation")