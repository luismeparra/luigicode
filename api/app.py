import os
import sys
import pandas as pd
from fastapi import FastAPI, HTTPException
from starlette.responses import JSONResponse
from predictor.predict import ModelPredictor
from .models.models import PassengerSatisfaction  # Update with your PassengerSatisfaction model

app = FastAPI()

# Add the parent directory to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

# Load the trained model
model_path = "./models/random_forest_model_output.pkl"  # Update with your model's path
predictor = ModelPredictor(model_path)

@app.get('/', status_code=200)
async def healthcheck():
    return 'Passenger satisfaction predictor is ready to go!'

@app.post('/predict')
def predict(passenger_features: PassengerSatisfaction) -> JSONResponse:
    try:
        # Convert input data to DataFrame and preprocess
        input_data = {
            "Gender": [passenger_features.gender],
            "Age": [passenger_features.age],
            "xx": [passenger_features.some_other_feature],  # Add other features here
            # ...
        }
        input_df = pd.DataFrame(input_data)

        # Make prediction using the loaded model
        prediction = predictor.predict(input_df)

        return JSONResponse({"prediction": prediction.tolist()})
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
