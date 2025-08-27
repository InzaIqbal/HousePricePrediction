import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Load best model
model = joblib.load("best_housing_model.pkl")

st.set_page_config(page_title="California Housing Price Prediction", layout="centered")
st.title("🏡 California Housing Price Prediction")
st.write("Enter housing details below to predict the median house value.")

# Sidebar inputs
st.sidebar.header("Input Features")

MedInc = st.sidebar.slider("Median Income (10k USD)", 0.5, 15.0, 5.0)
HouseAge = st.sidebar.slider("House Age (years)", 1, 50, 20)
AveRooms = st.sidebar.slider("Average Rooms", 1.0, 15.0, 6.0)
AveBedrms = st.sidebar.slider("Average Bedrooms", 0.5, 5.0, 1.0)
Population = st.sidebar.slider("Population", 100, 5000, 1000)
AveOccup = st.sidebar.slider("Average Occupancy", 1.0, 6.0, 3.0)
Latitude = st.sidebar.slider("Latitude", 32.0, 42.0, 35.0)
Longitude = st.sidebar.slider("Longitude", -125.0, -114.0, -120.0)

# Prediction
user_input = np.array([[MedInc, HouseAge, AveRooms, AveBedrms,
                        Population, AveOccup, Latitude, Longitude]])

prediction = model.predict(user_input)[0]

st.subheader("🏠 Predicted Median House Price")
st.success(f"${prediction * 100000:,.2f}")
