# create a api endpoints using fastapi

# load libraries
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

import warnings
warnings.filterwarnings('ignore')

# create object for FastAPI
app = FastAPI()

class Input(BaseModel):
    Gender              : int
    Age                 : int
    Driving_License     : int
    Region_Code         : float
    Previously_Insured  : int
    Vehicle_Age         : int
    Vehicle_Damage      : int
    Annual_Premium      : float
    Policy_Sales_Channel: float
    Vintage             : float

    '''
Gender                    int64
Age                       int64
Driving_License           int64
Region_Code             float64
Previously_Insured        int64
Vehicle_Age               int64
Vehicle_Damage            int64
Annual_Premium          float64
Policy_Sales_Channel    float64
Vintage                 float64
'''
    
# to pass the output
class Output(BaseModel):
    Response    :   int
'''
# addition of the columns and return the value in the third column
def add(data: Input) -> Output:
    Output.col3 = data.col1 + data.col2
'''

@app.post("/predict")
def predict(data: Input) ->  Output:
    X_input = pd.DataFrame([[data.Gender, data.Age, data.education, data.Driving_License, data.Region_Code, data.Region_Code, data.Vehicle_Age, 
                             data.Vehicle_Damage, data.Annual_Premium, data.Policy_Sales_Channel, data.Vintage]])
    
    X_input.columns = ['Gender', 'Age', 'education', 'Driving_License', 'Region_Code', 'Region_Code', 'Vehicle_Age', 'Vehicle_Damage',
       'Annual_Premium', 'Policy_Sales_Channel', 'Vintage']

    # load the model
    model = joblib.load('promote_pipeline_model.pkl')

    # predict using model
    prediction = model.predict(X_input)

    # result/output
    return Output(Response = prediction)
