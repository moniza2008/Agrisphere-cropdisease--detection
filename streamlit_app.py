import streamlit as st
from PIL import Image
import pandas as pd
#import openai  # Uncomment only if you want AI Bot

# -----------------------
# Page Config
# -----------------------
st.set_page_config(page_title="AgriSphere – Crop Detection App", layout="centered")
st.title("AgriSphere – Crop Detection 🌱")
st.write("Machine prototype is running successfully")

# -----------------------
# Tabs
# -----------------------
tab1, tab2, tab3 = st.tabs(["Crop Disease", "AI Assistant", "Market Prices"])

# -----------------------
# Tab 1: Crop Disease Detection
# -----------------------
with tab1:
    st.header("Crop Disease Detection 🌱")
    
    uploaded_file = st.file_uploader(
        "Upload your leaf image here (JPG/PNG)",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Leaf", use_column_width=True)

        # Placeholder prediction
        disease = "Leaf Blight"  # Replace with ML model later
        confidence = 92

        st.success(f"Disease Detected: {disease} ({confidence}%)")

        st.subheader("Recommended Remedy")
        st.write("""
        • Spray Mancozeb (2g/L) or Chlorothalonil (2ml/L)  
        • Use neem oil spray weekly  
        • Remove affected leaves to prevent spreading  
        • Avoid excess watering
        """)
    else:
        st.info("👆 Please upload a leaf image to start detection")

# -----------------------
# Tab 2: AI Farming Assistant (optional)
# -----------------------
with tab2:
    st.header("Ask an AI Farming Assistant 🤖")
    st.write("This section is optional and can be enabled using AI APIs.")

    st.info("AI assistant feature will be added in future versions.")

# -----------------------
# Tab 3: Location-based Market Prices
# -----------------------
with tab3:
    st.header("📊 Crop Market Prices (Location Based)")

    # Sample market data (Prototype)
    market_data = {
        "Thoothukudi": {
            "Rice": "₹38/kg",
            "Tomato": "₹22/kg",
            "Onion": "₹30/kg",
            "Chilli": "₹110/kg"
        },
        "Madurai": {
            "Rice": "₹40/kg",
            "Tomato": "₹18/kg",
            "Onion": "₹28/kg",
            "Chilli": "₹120/kg"
        },
        "Coimbatore": {
            "Rice": "₹42/kg",
            "Tomato": "₹25/kg",
            "Onion": "₹32/kg",
            "Chilli": "₹115/kg"
        },
        "Chennai": {
            "Rice": "₹45/kg",
            "Tomato": "₹28/kg",
            "Onion": "₹35/kg",
            "Chilli": "₹130/kg"
        }
    }

    # User selections
    location = st.selectbox(
        "📍 Select Market Location",
        list(market_data.keys())
    )

    crop = st.selectbox(
        "🌾 Select Crop",
        list(market_data[location].keys())
    )

    price = market_data[location][crop]

    st.success(f"💰 {crop} price in {location}: {price}")

    st.caption("⚠ Prices shown are indicative. Actual prices may vary based on market conditions.")
