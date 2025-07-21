import streamlit as st
import joblib
import numpy as np

# Set page config
st.set_page_config(page_title="🏡 House Price Prediction - India", layout="centered")

# Page Title
st.markdown("<h1 style='text-align: center; color: #2E8B57;'>🏠 House Price Prediction (India)</h1>", unsafe_allow_html=True)

st.markdown("<hr style='border: 1px solid #ccc;'>", unsafe_allow_html=True)

st.markdown("""
<p style='text-align: center; font-size: 16px;'>
This application predicts the <strong>estimated price</strong> of a house in India based on the number of bedrooms, bathrooms, living area, and total area.
</p>
""", unsafe_allow_html=True)

st.divider()

# Load the trained model
model = joblib.load("model.pkl")

# Input layout in two columns
col1, col2 = st.columns(2)

with col1:
    bed = st.number_input("🛏️ Bedrooms", min_value=1, max_value=10, step=1)
    area = st.number_input("🛋️ Living Area (sqft)", min_value=350, max_value=15000, step=50)

with col2:
    bath = st.number_input("🛁 Bathrooms", min_value=1, max_value=10, step=1)
    la = st.number_input("🏡 Total Area (sqft)", min_value=350, max_value=10000, step=50)

# Prediction logic
X = [[bed, bath, la, area]]

st.markdown("<br>", unsafe_allow_html=True)

if st.button("📊 Predict Price", use_container_width=True):
    input_data = np.array(X)
    prediction = model.predict(input_data)
    formatted_price = f"₹ {prediction[0]:,.2f}"
    
    st.success(f"### ✅ Estimated House Price: {formatted_price}")
