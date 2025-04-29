
import streamlit as st
import pandas as pd
import pickle

# Model load karo
model = pickle.load(open('lung_model.pkl', 'rb'))

st.title("Lung Cancer Detection")

# User input
age = st.slider("Age", 10, 100, 25)
smoking = st.selectbox("Do you smoke?", ["Yes", "No"])
anxiety = st.selectbox("Do you suffer from anxiety?", ["Yes", "No"])
# Add more inputs as per your dataset...

if st.button("Predict"):
    input_data = pd.DataFrame([[age, smoking, anxiety]], columns=['AGE', 'SMOKING', 'ANXIETY'])
    input_data = pd.get_dummies(input_data)
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.error("You might have lung cancer.")
    else:
        st.success("You are likely safe.")
