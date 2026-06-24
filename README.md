# 🏦 Bank Customer Churn Prediction using Artificial Neural Networks (ANN)

## 📌 Project Overview

Customer churn is one of the most critical challenges faced by banks and financial institutions. Losing existing customers directly impacts revenue and customer acquisition costs.

This project uses an Artificial Neural Network (ANN) built with TensorFlow/Keras to predict whether a customer is likely to leave the bank based on demographic and financial attributes.

The solution includes a complete machine learning pipeline, from data preprocessing and feature engineering to model deployment through an interactive web application.

---

## 🎯 Problem Statement

The objective of this project is to predict customer churn using customer information such as:

* Credit Score
* Geography
* Gender
* Age
* Tenure
* Account Balance
* Number of Products
* Credit Card Ownership
* Active Membership Status
* Estimated Salary

The model predicts:

* **0 → Customer Retained**
* **1 → Customer Churned**

---

## 🚀 Features

✅ Data Cleaning and Preprocessing

✅ Feature Encoding

✅ Feature Scaling

✅ Artificial Neural Network (ANN)

✅ Model Saving and Loading

✅ Real-Time Customer Churn Prediction

✅ Interactive Streamlit Web Application

---

## 🛠️ Tech Stack

### Programming Language

* Python

### Machine Learning & Deep Learning

* TensorFlow
* Keras
* Scikit-Learn

### Data Processing

* Pandas
* NumPy

### Visualization

* Matplotlib
* Seaborn

### Deployment

* Streamlit

---

## 📂 Project Structure

```text
├── Churn_Modelling.csv
├── experiments.ipynb
├── prediction.ipynb
├── app.py
├── model.h5
├── preprocessor.pkl
├── label_encoder_gender.pkl
├── onehot_encoder_geo.pkl
├── requirements.txt
└── README.md
```

---

## ⚙️ Machine Learning Pipeline

### 1. Data Collection

Customer data is loaded from the Churn Modelling dataset.

### 2. Data Preprocessing

* Handling categorical variables
* Label Encoding (Gender)
* One-Hot Encoding (Geography)
* Feature Scaling using StandardScaler

### 3. Train-Test Split

Dataset is divided into training and testing sets for evaluation.

### 4. Model Development

A Deep Learning model is built using TensorFlow/Keras.

Architecture:

```text
Input Layer
      ↓
Dense Layer (ReLU)
      ↓
Dense Layer (ReLU)
      ↓
Output Layer (Sigmoid)
```

### 5. Model Training

The ANN learns customer behavior patterns from historical data.

### 6. Model Evaluation

Performance is evaluated using classification metrics and validation data.

### 7. Deployment

The trained model is deployed through a Streamlit application for real-time predictions.

---

## 📊 Input Features

| Feature         | Description             |
| --------------- | ----------------------- |
| CreditScore     | Customer credit score   |
| Geography       | Customer country        |
| Gender          | Male/Female             |
| Age             | Customer age            |
| Tenure          | Years with bank         |
| Balance         | Account balance         |
| NumOfProducts   | Number of products used |
| HasCrCard       | Credit card ownership   |
| IsActiveMember  | Activity status         |
| EstimatedSalary | Customer salary         |

---

## 🎯 Prediction Output

The application predicts:

```text
Customer is likely to churn
```

or

```text
Customer is likely to stay
```

along with the churn probability score.

---

## 📈 Business Impact

Banks can use this model to:

* Identify high-risk customers
* Improve retention strategies
* Reduce customer acquisition costs
* Increase customer lifetime value
* Improve targeted marketing campaigns

---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/customer-churn-ann.git
cd customer-churn-ann
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 🔮 Future Improvements

* Hyperparameter Tuning
* Explainable AI using SHAP
* Model Comparison (Logistic Regression, Random Forest, XGBoost)
* FastAPI Deployment
* Docker Containerization
* Cloud Deployment (AWS/GCP/Azure)

---


