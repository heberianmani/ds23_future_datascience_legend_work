from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
app = FastAPI()

class Input(BaseModel):
    CONSOLE: object
    YEAR: int
    CATEGORY: object
    PUBLISHER: object
    RATING: object
    CRITICS_POINTS: float
    USER_POINTS: float

class Output(BaseModel):
    SalesInMillions: float

@app.post("/predict")
def predict2(data: Input) -> Output:
    # input
    # dataframe thru list
    X_input = pd.DataFrame([[data.CONSOLE, data.YEAR, data.CATEGORY, data.PUBLISHER, data.RATING, data.CRITICS_POINTS, data.USER_POINTS]])
    X_input.columns = ['CONSOLE', 'YEAR', 'CATEGORY', 'PUBLISHER', 'RATING', 'CRITICS_POINTS', 'USER_POINTS']
    # dataframe thru dictionary (valid)
    #X_input = pd.DataFrame([{'CONSOLE':  data.CONSOLE,'YEAR':  data.YEAR,'CATEGORY':  data.CATEGORY,'PUBLISHER':  data.PUBLISHER,'RATING':  data.RATING,'CRITICS_POINTS':  data.CRITICS_POINTS,'USER_POINTS':  data.USER_POINTS}])
   
    print(X_input)
    # load the model
    model = joblib.load('vgsales_pipeline_model.pkl')
    #predict using the model
    prediction = model.predict(X_input)
    # output
    return Output(SalesInMillions = prediction)