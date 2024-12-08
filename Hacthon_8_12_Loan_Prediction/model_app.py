from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

import warnings
warnings.filterwarnings('ignore')

# create object for FastAPI
app = FastAPI()

class Input(BaseModel):
    Gender : object 
    Married : object 
    Dependents : object 
    Education : object 
    Self_Employed : object 
    ApplicantIncome : int  
    CoapplicantIncome : float
    LoanAmount : float
    Loan_Amount_Term : float
    Credit_History : float
    Property_Area : object

# to pass the output
class Output(BaseModel):
    Loan_Status    :   object

@app.post("/predict")
def predict(data: Input) ->  Output:
    X_input = pd.DataFrame([[data.Gender, data.Married, data.Dependents, data.Education, data.Self_Employed, data.ApplicantIncome, 
                             data.CoapplicantIncome, data.LoanAmount, data.Loan_Amount_Term, data.Credit_History, data.Property_Area]])
    
    X_input.columns = ['Gender', 'Married', 'Dependents', 'Education','Self_Employed', 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
                       'Loan_Amount_Term', 'Credit_History', 'Property_Area']

    # load the model
    model = joblib.load('load_prediction_model.pkl')

    # predict using model
    prediction = model.predict(X_input)

    # result/output
    return Output(Response = prediction)