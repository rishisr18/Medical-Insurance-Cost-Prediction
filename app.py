import streamlit as st
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

st.set_page_config(page_title="Medical Insurance Prediction", layout="centered")

st.title("💊 Medical Insurance Cost Predictor")
st.write("Fill the details below to estimate the insurance cost.")

# Input fields
age = st.slider("Age", 18, 70, 30)
sex = st.selectbox("Sex", ["Male", "Female"])
bmi = st.number_input("BMI (Body Mass Index)", min_value=10.0, max_value=50.0, value=25.0)
children = st.selectbox("Number of Children", list(range(6)))
smoker = st.selectbox("Smoker", ["Yes", "No"])
region = st.selectbox("Region", ["southeast", "southwest", "northeast", "northwest"])

# Encoding categorical variables
sex_encoded = 1 if sex == "Male" else 0
smoker_encoded = 1 if smoker == "Yes" else 0
region_encoded = {"southeast": 0, "southwest": 1, "northeast": 2, "northwest": 3}
region_val = region_encoded[region]

# Prediction
if st.button("Predict Insurance Cost 💰"):
    input_data = np.array([[age, sex_encoded, bmi, children, smoker_encoded, region_val]])
    prediction = model.predict(input_data)
    st.success(f"Estimated Insurance Charges: ₹{prediction[0]:,.2f}")
