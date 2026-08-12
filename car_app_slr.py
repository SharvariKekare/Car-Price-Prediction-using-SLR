import streamlit as st
import pandas as pd
import joblib

# Load Model
model = joblib.load("simple_linear_regression_model.pkl")

# Page Configuration
st.set_page_config(
    page_title="Car Price Prediction",
    page_icon="🚗",
    layout="centered"
)

st.title("🚗 Car Price Prediction")
st.subheader("Simple Linear Regression")

# Dropdown Menu
year = st.selectbox(
    "Select Manufacturing Year",
    options=list(range(1990, 2026)),
    index=28
)

# Predict Button
if st.button("Predict Price"):

    input_data = pd.DataFrame({
        "year": [year]
    })

    prediction = model.predict(input_data)

    st.success(f"Predicted Car Price: ₹ {prediction[0]:,.2f}")