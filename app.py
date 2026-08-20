import pickle
from fastapi import FastAPI
import pandas as pd
from fastapi.responses import JSONResponse
from schema import MyData

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

app = FastAPI()

@app.post("/predict")
def predict_output(data : MyData):

    input_data = pd.DataFrame([data.model_dump()])
    
    prediction = model.predict(input_data)
    
    return JSONResponse(status_code=200, content={"Prediction" : prediction[0]})