# app.py
import streamlit as st
import numpy as np
import pickle

# Load model and columns using pickle
with open("models/logistic_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("models/columns.pkl", "rb") as f:
    columns = pickle.load(f)

st.title("📉 Customer Churn Prediction App")

# User Inputs
def get_user_input():
    gender = st.selectbox("Gender", ['Male', 'Female'])
    SeniorCitizen = st.selectbox("Senior Citizen", [0, 1])
    Partner = st.selectbox("Has Partner?", ['Yes', 'No'])
    Dependents = st.selectbox("Has Dependents?", ['Yes', 'No'])
    tenure = st.slider("Tenure (months)", 0, 72)
    PhoneService = st.selectbox("Phone Service", ['Yes', 'No'])
    MultipleLines = st.selectbox("Multiple Lines", ['Yes', 'No', 'No phone service'])
    InternetService = st.selectbox("Internet Service", ['DSL', 'Fiber optic', 'No'])
    OnlineSecurity = st.selectbox("Online Security", ['Yes', 'No', 'No internet service'])
    OnlineBackup = st.selectbox("Online Backup", ['Yes', 'No', 'No internet service'])
    DeviceProtection = st.selectbox("Device Protection", ['Yes', 'No', 'No internet service'])
    TechSupport = st.selectbox("Tech Support", ['Yes', 'No', 'No internet service'])
    StreamingTV = st.selectbox("Streaming TV", ['Yes', 'No', 'No internet service'])
    StreamingMovies = st.selectbox("Streaming Movies", ['Yes', 'No', 'No internet service'])
    Contract = st.selectbox("Contract", ['Month-to-month', 'One year', 'Two year'])
    PaperlessBilling = st.selectbox("Paperless Billing", ['Yes', 'No'])
    PaymentMethod = st.selectbox("Payment Method", [
        'Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'
    ])
    MonthlyCharges = st.number_input("Monthly Charges", 0.0)
    TotalCharges = st.number_input("Total Charges", 0.0)

    user_input = {
        'tenure': tenure,
        'MonthlyCharges': MonthlyCharges,
        'TotalCharges': TotalCharges,
        'SeniorCitizen': SeniorCitizen,
        'gender_Male': 1 if gender == 'Male' else 0,
        'Partner_Yes': 1 if Partner == 'Yes' else 0,
        'Dependents_Yes': 1 if Dependents == 'Yes' else 0,
        'PhoneService_Yes': 1 if PhoneService == 'Yes' else 0,
        'MultipleLines_No phone service': 1 if MultipleLines == 'No phone service' else 0,
        'MultipleLines_Yes': 1 if MultipleLines == 'Yes' else 0,
        'InternetService_Fiber optic': 1 if InternetService == 'Fiber optic' else 0,
        'InternetService_No': 1 if InternetService == 'No' else 0,
        'OnlineSecurity_No internet service': 1 if OnlineSecurity == 'No internet service' else 0,
        'OnlineSecurity_Yes': 1 if OnlineSecurity == 'Yes' else 0,
        'OnlineBackup_No internet service': 1 if OnlineBackup == 'No internet service' else 0,
        'OnlineBackup_Yes': 1 if OnlineBackup == 'Yes' else 0,
        'DeviceProtection_No internet service': 1 if DeviceProtection == 'No internet service' else 0,
        'DeviceProtection_Yes': 1 if DeviceProtection == 'Yes' else 0,
        'TechSupport_No internet service': 1 if TechSupport == 'No internet service' else 0,
        'TechSupport_Yes': 1 if TechSupport == 'Yes' else 0,
        'StreamingTV_No internet service': 1 if StreamingTV == 'No internet service' else 0,
        'StreamingTV_Yes': 1 if StreamingTV == 'Yes' else 0,
        'StreamingMovies_No internet service': 1 if StreamingMovies == 'No internet service' else 0,
        'StreamingMovies_Yes': 1 if StreamingMovies == 'Yes' else 0,
        'Contract_One year': 1 if Contract == 'One year' else 0,
        'Contract_Two year': 1 if Contract == 'Two year' else 0,
        'PaperlessBilling_Yes': 1 if PaperlessBilling == 'Yes' else 0,
        'PaymentMethod_Credit card (automatic)': 1 if PaymentMethod == 'Credit card (automatic)' else 0,
        'PaymentMethod_Electronic check': 1 if PaymentMethod == 'Electronic check' else 0,
        'PaymentMethod_Mailed check': 1 if PaymentMethod == 'Mailed check' else 0
    }

    return [user_input.get(col, 0) for col in columns]

# Predict
if st.button("Predict Churn"):
    features = get_user_input()
    result = model.predict([features])[0]
    if result == 1:
        st.error("⚠ Customer is likely to churn.")
    else:
        st.success("✅ Customer is likely to stay.")