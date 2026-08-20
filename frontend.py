import streamlit as st
import requests

from schema import MyData

st.title("Breast Cancer Prediction")

API_URL = "http://127.0.0.1:8000/predict"

features = list(MyData.model_fields.keys())

data = {}

for feature in features:
    data[feature] = st.number_input(
        feature,
        min_value=0.000001,
        value=1.0
    )

if st.button("Predict"):

    response = requests.post(
        API_URL,
        json=data
    )

    if response.status_code == 200:
        result = response.json()

        st.success(
            f"Prediction: {result['Prediction']}"
        )
    else:
        st.error(response.text)