Bank Customer Churn Prediction using Artificial Neural Networks (ANN)
Overview

This project predicts whether a bank customer is likely to leave the bank (churn) using an Artificial Neural Network (ANN). The model is trained on customer demographic and banking information such as age, balance, geography, gender, credit score, and tenure.

Features
Data preprocessing using Scikit-Learn
Label Encoding and One-Hot Encoding
Feature Scaling
ANN model built with TensorFlow/Keras
Hyperparameter tuning experiments
Model persistence using Pickle and H5 files
Interactive prediction interface using Streamlit/Flask
Dataset

The project uses the Bank Customer Churn Dataset containing:

Credit Score
Geography
Gender
Age
Tenure
Balance
Number of Products
Has Credit Card
Is Active Member
Estimated Salary

Target Variable:

Exited (1 = Customer Churned, 0 = Customer Retained)
Tech Stack
Python
TensorFlow / Keras
Scikit-Learn
Pandas
NumPy
Streamlit / Flask
Pickle
Model Architecture

Input Layer

↓

Hidden Layer 1 (ReLU)

↓

Hidden Layer 2 (ReLU)

↓

Output Layer (Sigmoid)

Project Workflow
Data Collection
Data Preprocessing
Feature Engineering
Train-Test Split
Feature Scaling
ANN Model Training
Hyperparameter Tuning
Model Evaluation
Deployment
Results

The ANN model learns customer behavior patterns and predicts the probability of customer churn, helping banks identify at-risk customers and improve retention strategies.

Installation
git clone <repository-url>
cd ANN

pip install -r requirements.txt
Run Application
streamlit run app.py
Future Improvements
XGBoost vs ANN comparison
Explainable AI (SHAP)
Customer segmentation
Real-time prediction API using FastAPI
Docker deployment
