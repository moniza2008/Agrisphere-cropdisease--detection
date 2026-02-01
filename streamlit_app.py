import streamlit as st
import pandas as pd
from PIL import Image
import openai  # AI bot

# Set your API key (or use environment variable)
openai.api_key = st.secrets["OPENAI_API_KEY"]  # safer way in Streamlit cloud

st.set_page_config(page_title="AgriSphere – Crop Disease Detection", layout="centered")
st.title("AgriSphere – Crop Disease Detection")
st.write("Machine prototype is running successfully")

# --------------------------
# Section A: Leaf Upload + Prediction
# --------------------------
st.header("Step 1: Upload a Leaf Image")

uploaded_file = st.file_uploader(
    "Upload your leaf image here (JPG/PNG)",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Leaf", use_column_width=True)

    # Step 2: Process image + ML prediction
    disease = "Leaf Blight"  # placeholder
    confidence = 92           # placeholder

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
# Section B: AI Bot for Farming Questions
# --------------------------
st.header("Step 3: Ask an AI Farming Assistant")

user_question = st.text_input("Type your question here:")

if user_question:
    with st.spinner("AI is thinking..."):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert agricultural assistant."},
                {"role": "user", "content": user_question}
            ],
            max_tokens=150
        )
        answer = response.choices[0].message.content.strip()
        st.write(answer)

# --------------------------
# Section C: Market Prices Table
# --------------------------
st.header("Step 4: Current Crop Market Prices")

data = {
    "Crop": ["Tomato", "Rice", "Wheat"],
    "Price (Rs/kg)": [30, 50, 40],
    "Market": ["Chennai", "Tuticorin", "Coimbatore"]
}

df = pd.DataFrame(data)
st.table(df)

st.write("⚠ Note: Market prices are indicative. For accurate rates, consult local mandis.")
