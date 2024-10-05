from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

class Input(BaseModel)
    X: float

class Output(BaseModel)
    y: float

@app.post("/predict")
def predict(data: Input) -> Output:
    X_input = np.array([[data.X]])
    model = joblib.load(r"D:\Manikandan\Documents\Datascience_ML_DL_AI\Programming\Github\ds23_future_datascience_legend_work\Linear_Regression\house_price_lr_model.pkl")
    prediction = model.predict(X_input)
    return Output(y=prediction)