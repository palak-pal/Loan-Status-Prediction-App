import streamlit as st
import pandas as pd
import numpy as np
import pickle as pk

# Load the trained model and scaler
model = pk.load(open('model.pkl', 'rb'))
scaler = pk.load(open('scaler.pkl', 'rb'))

# Title of the web application
st.header('Loan Prediction App')

# Collect user inputs for prediction
no_of_dependents = st.number_input('Number of Dependents', min_value=0, max_value=10, step=1)
income_annum = st.number_input('Income per Annum', min_value=0)
loan_amount = st.number_input('Loan Amount', min_value=0)
loan_term = st.number_input('Loan Term (in months)', min_value=0, max_value=480, step=12)
cibil_score = st.number_input('CIBIL Score', min_value=300, max_value=900)
education_not_graduate = st.selectbox('Education (Not Graduate: 1, Graduate: 0)', [1, 0])
self_employed_yes = st.selectbox('Self Employed (Yes: 1, No: 0)', [1, 0])
assets = st.number_input('Total Asset Value', min_value=0)

# Button to trigger prediction
if st.button('Predict Loan Approval'):
    # Prepare input data for prediction
    input_data = pd.DataFrame([[no_of_dependents, income_annum, loan_amount, loan_term, cibil_score,
                                education_not_graduate, self_employed_yes, assets]],
                              columns=['no_of_dependents', 'income_annum', 'loan_amount', 'loan_term',
                                       'cibil_score', 'education_ Not Graduate', 'self_employed_ Yes', 'Assets'])

    # Preprocess the input data using the loaded scaler
    input_data_scaled = scaler.transform(input_data)

    # Make prediction using the loaded model
    prediction = model.predict(input_data_scaled)

    # Display the prediction result
    result = 'Approved' if prediction[0] == 0 else 'Not Approved'
    st.subheader(f'Predicted Loan Status: {result}')
