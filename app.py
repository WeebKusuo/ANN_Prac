import streamlit as st
import pandas as pd
import numpy as np
import tensorflow as tf
import pickle
from sklearn.preprocessing import StandardScaler,OneHotEncoder,LabelEncoder


#loading the trained model 
model=tf.keras.models.load_model('model.h5')

with open("gender_encoder.pkl",'rb') as file:
    label_encoder_gen=pickle.load(file)


with open("preprocessor.pkl",'rb') as file:
    preprocessor=pickle.load(file)


## streamlit app
st.title('Customer Churn Prediction')

# User input
geography = st.selectbox(
    'Geography',
    preprocessor.named_transformers_['onehot'].categories_[0]
)

gender = st.selectbox(
    'Gender',
    label_encoder_gen.classes_
)

age = st.slider('Age', 18, 92)

balance = st.number_input('Balance')

credit_score = st.number_input('Credit Score')

estimated_salary = st.number_input('Estimated Salary')

tenure = st.slider('Tenure', 0, 10)

num_of_products = st.slider('Number of Products', 1, 4)

has_cr_card = st.selectbox('Has Credit Card', [0, 1])

is_active_member = st.selectbox('Is Active Member', [0, 1])

input_data = pd.DataFrame({
    'CreditScore': [credit_score],
    'Geography': [geography],   # <-- Missing tha
    'Gender': [gender],
    'Age': [age],
    'Tenure': [tenure],
    'Balance': [balance],
    'NumOfProducts': [num_of_products],
    'HasCrCard': [has_cr_card],
    'IsActiveMember': [is_active_member],
    'EstimatedSalary': [estimated_salary]
})
input_data['Gender'] = label_encoder_gen.transform(
    input_data['Gender']
)
input_data_scaled=preprocessor.transform(input_data)

prediction=model.predict(input_data_scaled)
prediction_proba=prediction[0][0]

if prediction_proba>0.5:
    st.write('The Customer is likely to Churn')

else:
    st.write("THe Customer is not likely to churn")    