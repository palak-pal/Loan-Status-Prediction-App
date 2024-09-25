Loan Status Prediction App
This repository contains a Loan Status Prediction web application built with Streamlit. The app allows users to predict whether a loan will be approved or not based on various input parameters.

Features:
User Input Fields: Users can input relevant financial and personal details like:
Number of dependents
Annual income
Loan amount
Loan term (in months)
CIBIL score
Education level (Graduate or Not)
Employment status (Self-employed or Not)

Total asset value
Prediction: Based on the provided information, the app predicts whether the loan will be approved or not.
Pre-trained Model: The application uses a pre-trained machine learning model (loaded from a pickle file) to make predictions, along with a scaler for input preprocessing.

Tech Stack:
Streamlit: For building the interactive web app interface
Pandas & NumPy: For data manipulation and input processing
Pickle: For loading the pre-trained model and scaler

Run the app using Streamlit: streamlit run app.py

Enter the required input values in the web interface.
Click Predict Loan Approval to get the prediction result.

Model Details:
The app uses a machine learning model trained on historical loan data to predict loan approval status.
The model and scaler are saved as model.pkl and scaler.pkl, respectively.
