import streamlit as st
import pandas as pd
import requests
import json

st.title("Cross Sell Insurance Prediction")
st.title("Provide the input and predict")

df = pd.read_csv("hack_test.csv")

Gender = st.selectbox("Gender", pd.unique(df['Gender']))
Age = st.number_input("Age", step=1)
Driving_License = st.number_input("Driving_License", step=1)
Region_Code = st.number_input("Region_Code", step=1)
Previously_Insured = st.number_input("Previously_Insured", step=1)
Vehicle_Age = st.selectbox("Vehicle_Age", pd.unique(df['Vehicle_Age']))
Vehicle_Damage = st.selectbox("Vehicle_Damage", pd.unique(df['Vehicle_Damage']))
Annual_Premium = st.number_input("Annual_Premium", step=1)
Policy_Sales_Channel = st.number_input("Policy_Sales_Channel", step=1)
Vintage = st.number_input("Vintage", step=1)


inputs = {
    "Gender"              :   Gender,
    "Age"                 :   Age,     
    "Driving_License"     :   Driving_License,
    "Region_Code"         :   Region_Code,
    "Previously_Insured"  :   Previously_Insured,
    "Vehicle_Age"         :   Vehicle_Age,
    "Vehicle_Damage"      :   Vehicle_Damage,
    "Annual_Premium"      :   Annual_Premium,
    "Policy_Sales_Channel":   Policy_Sales_Channel,
    "Vintage"             :   Vintage
}

if st.button('Predict'):
    #res = requests.post(url = "http://127.0.0.1:8000/predict", data = json.dumps(inputs))
    res = requests.post(url = "https://api-cross-sell-1094332162336.us-central1.run.app/predict", data = json.dumps(inputs))

    st.json(res.text)


# command to run in terminal: streamlit run webview.py    