import streamlit as st
from PIL import Image

st.title("AgriSphere – Crop Disease Detection 🌱")
st.write("Machine prototype is running successfully")

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
        st.markdown("### 🧪 Analysis Result")
        st.success("Predicted Disease: Leaf Blight 🌿")
        st.info("Confidence: 87%")
