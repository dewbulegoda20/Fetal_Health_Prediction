# app.py

import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load('fetal_health_model.pkl')

# Streamlit app title
st.title("Fetal Health Prediction")

st.write("""
Enter the fetal health parameters below to predict the health status.
""")

# Only keep the 14 remaining features
accelerations = st.number_input("Accelerations", step=0.001)
fetal_movement = st.number_input("Fetal Movement", step=0.001)
uterine_contractions = st.number_input("Uterine Contractions", step=0.001)
light_decelerations = st.number_input("Light Decelerations", step=0.001)
severe_decelerations = st.number_input("Severe Decelerations", step=0.001)
prolongued_decelerations = st.number_input("Prolongued Decelerations", step=0.001)
abnormal_short_term_variability = st.number_input("Abnormal Short-Term Variability", step=0.1)
mean_value_of_short_term_variability = st.number_input("Mean STV", step=0.001)
percentage_of_time_with_abnormal_long_term_variability = st.number_input("Abnormal LTV (%)", step=0.1)
mean_value_of_long_term_variability = st.number_input("Mean LTV", step=0.1)
histogram_max = st.number_input("Histogram Max", step=0.1)
histogram_number_of_zeroes = st.number_input("Number of Zeroes", step=1.0)
histogram_variance = st.number_input("Histogram Variance", step=0.1)
histogram_tendency = st.number_input("Histogram Tendency", step=0.1)

# Prediction
if st.button("Predict Fetal Health"):
    input_data = np.array([[
        accelerations, fetal_movement, uterine_contractions, light_decelerations,
        severe_decelerations, prolongued_decelerations, abnormal_short_term_variability,
        mean_value_of_short_term_variability, percentage_of_time_with_abnormal_long_term_variability,
        mean_value_of_long_term_variability, histogram_max, histogram_number_of_zeroes,
        histogram_variance, histogram_tendency
    ]])

    prediction = model.predict(input_data)[0]

    label = {
        1: "Normal",
        2: "Suspect",
        3: "Pathological"
    }

    st.success(f"Predicted Fetal Health Status: {label[prediction]}")
