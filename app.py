
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
    import pandas as pd

# Example: agar user ne 'Yes' ya 'No' select kiya
input_data = pd.DataFrame([{
    'AGE': age,  # number
    'SMOKING': 1 if smoke == 'Yes' else 0,
    'ANXIETY': 1 if anxiety == 'Yes' else 0,
    'ALCOHOL CONSUMING': 1 if alcohol == 'Yes' else 0,
    'COUGHING': 1 if coughing == 'Yes' else 0,
    'FATIGUE': 1 if fatigue == 'Yes' else 0,
    'SHORTNESS OF BREATH': 1 if breath == 'Yes' else 0,
    # ... aur baaki features bhi isi tarah
}])

    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.error("You might have lung cancer.")
    else:
        st.success("You are likely safe.")
