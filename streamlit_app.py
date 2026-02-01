import streamlit as st
from PIL import Image
import pandas as pd

# Page config
st.set_page_config(page_title="AgriSphere – Crop Disease Detection", layout="centered")
st.title("AgriSphere – Crop Disease Detection 🌱")
st.write("Machine prototype is running successfully")



# Sidebar menu
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Crop Disease", "Market Prices"])

# --------------------------
# Page 1: Crop Disease Detection
# --------------------------
if page == "Crop Disease":
    st.title("Crop Disease Detection 🌱")

    uploaded_file = st.file_uploader(
        "Upload your leaf image here (JPG/PNG)",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Leaf", use_column_width=True)

        # Placeholder prediction
        disease = "Leaf Blight"
        confidence = 92
        st.success(f"Disease Detected: {disease} ({confidence}%)")

        st.subheader("Recommended Remedy")
        st.write("""
        • Spray Mancozeb (2g/L) or Chlorothalonil (2ml/L)  
        • Use neem oil spray weekly  
        • Remove affected leaves to prevent spreading
        """)
    else:
        st.info("👆 Please upload a leaf image to start detection")

# --------------------------
# Page 2: Market Prices
# --------------------------
elif page == "Market Prices":
    st.title("Current Crop Market Prices")

    data = {
        "Crop": ["Tomato", "Rice", "Wheat", "Chilli"],
        "Price (Rs/kg)": [30, 50, 40, 120],
        "Market": ["Chennai", "Tuticorin", "Coimbatore", "Madurai"]
    }

    df = pd.DataFrame(data)
    st.table(df)
    st.write("⚠ Note: Market prices are indicative. For accurate rates, consult local mandis.")
