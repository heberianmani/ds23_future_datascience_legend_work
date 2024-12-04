import streamlit as st
import pandas as pd
import requests
import json

st.title("HR Analytics")
st.write("Provide the input and predict")

df = pd.read_csv('D:\Manikandan\Documents\Datascience_ML_DL_AI\Programming\Github\ds23_future_datascience_legend_work\Machine_Hack_Practice_23_11\data\hack_test.csv')

#CONSOLE  = st.text_input("CONSOLE")
department = st.selectbox("department", pd.unique(df['department']))
region = st.selectbox("region", pd.unique(df['region']))
education = st.selectbox("education", pd.unique(df['education']))
gender = st.selectbox("gender", pd.unique(df['gender']))
recruitment_channel = st.selectbox("recruitment_channel", pd.unique(df['recruitment_channel']))
no_of_trainings = st.number_input("no_of_trainings", step=1)
age = st.number_input("age", step=20)
previous_year_rating = st.selectbox("previous_year_rating", pd.unique(df['previous_year_rating']))
length_of_service = st.selectbox("length_of_service", pd.unique(df['length_of_service']))
KPIs_met_80_percent = st.selectbox("KPIs_met >80%", pd.unique(df['KPIs_met >80%']))
awards_won = st.number_input("awards_won", step=1) 
avg_training_score = st.number_input("avg_training_score", step=1)


inputs = {
"department" : department,
"region" : region,
"education" : education,
"gender" : gender,
"recruitment_channel" :  recruitment_channel,
"no_of_trainings" : no_of_trainings,
"age" : age,
"previous_year_rating" : previous_year_rating,
"length_of_service" : length_of_service,
"KPIs_met_80" :  KPIs_met_80_percent,
"awards_won" : awards_won,
"avg_training_score" : avg_training_score
}

if st.button('Predict'):
    res = requests.post(url = "https://api-test2-1094332162336.us-central1.run.app/predict", data = json.dumps(inputs))

    st.json(res.text)


# command to run in terminal: streamlit run webview.py    