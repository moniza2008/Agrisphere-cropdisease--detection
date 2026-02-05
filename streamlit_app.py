import streamlit as st
from PIL import Image
from languages import LANG

# -----------------------
# Page Config
# -----------------------
st.set_page_config(page_title="AgriSphere", layout="centered")

# -----------------------
# Language Selector
# -----------------------
language = st.selectbox(
    "🌐 Select Language / भाषा / மொழி",
    ["English", "Hindi", "Tamil"]
)

T = LANG[language]

st.title(T["app_title"])
st.write(T["subtitle"])

# -----------------------
# Tabs
# -----------------------
tab1, tab2, tab3 = st.tabs([T["tab1"], T["tab2"], T["tab3"]])

# -----------------------
# Tab 1: Crop Disease Detection
# -----------------------
with tab1:
    uploaded_file = st.file_uploader(
        T["upload"],
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Leaf", use_column_width=True)

        disease = "Leaf Blight"
        confidence = 92

        st.success(f"{T['detected']}: {disease} ({confidence}%)")

        st.subheader(T["remedy"])
        st.write("""
        • Spray Mancozeb (2g/L) or Chlorothalonil (2ml/L)  
        • Use neem oil spray weekly  
        • Remove affected leaves  
        • Avoid excess watering
        """)
    else:
        st.info("👆 Upload an image to start detection")

# -----------------------
# Tab 2: AI Assistant
# -----------------------
with tab2:
    st.header(T["assistant"])
    st.info(T["future"])

# -----------------------
# Tab 3: Market Prices
# -----------------------
with tab3:
    st.header(T["market"])

    market_data = {
        "Thoothukudi": {"Rice": "₹38/kg", "Tomato": "₹22/kg", "Onion": "₹30/kg", "Chilli": "₹110/kg"},
        "Madurai": {"Rice": "₹40/kg", "Tomato": "₹18/kg", "Onion": "₹28/kg", "Chilli": "₹120/kg"},
        "Coimbatore": {"Rice": "₹42/kg", "Tomato": "₹25/kg", "Onion": "₹32/kg", "Chilli": "₹115/kg"},
        "Chennai": {"Rice": "₹45/kg", "Tomato": "₹28/kg", "Onion": "₹35/kg", "Chilli": "₹130/kg"}
    }

    location = st.selectbox(T["location"], list(market_data.keys()))
    crop = st.selectbox(T["crop"], list(market_data[location].keys()))

    st.success(f"{T['price']}: {market_data[location][crop]}")
    st.caption(f"⚠ {T['note']}")
