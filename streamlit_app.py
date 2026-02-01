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
        """)
    else:
        st.info("👆 Please upload a leaf image to start detection")

# -----------------------
# Tab 2: AI Farming Assistant (optional)
# -----------------------
with tab2:
    st.header("Ask an AI Farming Assistant")
    st.write("This section is optional. Requires OpenAI API key and internet.")

    #user_question = st.text_input("Type your question here:")
    #if user_question:
    #    openai.api_key = "YOUR_OPENAI_API_KEY"
    #    response = openai.ChatCompletion.create(
    #        model="gpt-3.5-turbo",
    #        messages=[
    #            {"role": "system", "content": "You are an expert agricultural assistant."},
    #            {"role": "user", "content": user_question}
    #        ],
    #        max_tokens=150
    #    )
    #    answer = response.choices[0].message.content.strip()
    #    st.write(answer)

# -----------------------
# Tab 3: Market Prices
# -----------------------
with tab3:
    st.header("Current Crop Market Prices")
    
    data = {
        "Crop": ["Tomato", "Rice", "Wheat", "Chilli"],
        "Price (Rs/kg)": [30, 50, 40, 120],
        "Market": ["Chennai", "Tuticorin", "Coimbatore", "Madurai"]
    }

    df = pd.DataFrame(data)
    st.table(df)
    st.write("⚠ Note: Market prices are indicative. For accurate rates, consult local mandis.")
