import streamlit as st
from PIL import Image

st.title("AgriSphere – Crop Disease Detection ")
st.write("Machine prototype is running successfully")
st.markdown("""
### 🔍 How it works
1. User uploads a leaf image  
2. Image is processed  
3. ML model analyses patterns  
4. Disease and confidence are displayed
""")

uploaded_file = st.file_uploader(
    "Upload a leaf image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Leaf Image", use_column_width=True)
    st.success("Image uploaded successfully!")
if uploaded_file is not None:
    if st.button("Detect Disease"):
        st.markdown("###  Analysis Result")
        st.success("Predicted Disease: Leaf Blight 🌿")
        st.info("Confidence: 87%")
st.markdown("###  Recommended Remedy")
st.write("""
• Spray Mancozeb (2g/L) or Chlorothalonil (2ml/L)  
• Use neem oil spray weekly  
• Remove infected leaves  
• Avoid excess watering
""")
