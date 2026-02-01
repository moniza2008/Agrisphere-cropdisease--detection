import streamlit as st
from PIL import Image
import pandas as pd

# Page config
st.set_page_config(page_title="AgriSphere – Crop Disease Detection", layout="centered")
st.title("AgriSphere – Crop Disease Detection 🌱")
st.write("Machine prototype is running successfully")

# --------------------------
# Step 1: Upload Leaf Image
# --------------------------
uploaded_file = st.file_uploader(
    "Upload your leaf image here (JPG/PNG)",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    # Display uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Leaf", use_column_width=True)

    # Step 2: Placeholder for prediction
    disease = "Leaf Blight"  # placeholder
    confidence = 92           # placeholder

    st.success(f"Disease Detected: {disease} ({confidence}%)")

    # Recommended remedy
    st.subheader("Recommended Remedy")
    st.write("""
    • Spray Mancozeb (2g/L) or Chlorothalonil (2ml/L)  
    • Use neem oil spray weekly  
    • Remove affected leaves to prevent spreading
    """)
else:
    st.info("👆 Please upload a leaf image to start detection")

# --------------------------
# Step 3: Market Prices Table
# --------------------------
st.header("Current Crop Market Prices")

# Example data - you can update manually or connect API later
data = {
    "Crop": ["Tomato", "Rice", "Wheat", "Chilli"],
    "Price (Rs/kg)": [30, 50, 40, 120],
    "Market": ["Chennai", "Tuticorin", "Coimbatore", "Madurai"]
}

df = pd.DataFrame(data)
st.table(df)

st.write("⚠ Note: Market prices are indicative. For accurate rates, consult local mandis.")
