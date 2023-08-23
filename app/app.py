import sys
import os

# Add the parent directory to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)


import logging

#import os
#import sys
import pandas as pd
from fastapi import FastAPI, HTTPException
from starlette.responses import JSONResponse
from predict.predict import ModelPredictor
#from .utilities.custom_logging import CustomLogger

#from .models.models import PassengerSatisfaction  # Update with your PassengerSatisfaction model
import joblib

app = FastAPI()

#logger = CustomLogger("app.log")

# Configure logging
log_format = "[%(asctime)s] [%(levelname)s] [%(name)s] - %(message)s"
logging.basicConfig(level=logging.INFO, format=log_format)

## The  logging choosen is INFO and it can
# replace for logging.WARNING, logging.ERROR, or logging.CRITICAL to adjust the logging level


# Add the parent directory to sys.path

#current_dir = os.path.dirname(os.path.abspath(__file__))
#parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
#sys.path.append(parent_dir)

# Load the trained model
model_path = "/Users/luis.mendez/luigicode/app/ml_models/random_forest_model_output.pkl"
#model_path = "/Users/luis.mendez/luigicode/models/random_forest_model_output.pkl"

#model_path = "ml_models/random_forest_model_output.pkl"

loaded_model = joblib.load(model_path)

predictor = ModelPredictor(model_path)
#predictor = joblib.load(model_path)

@app.get('/', status_code=200)
async def healthcheck():
    logger.info("Passenger satisfaction predictor is ready to go!")
    return 'Passenger satisfaction predictor is ready to go!'
#1
@app.post('/predict')
def predict(passenger_features: dict) -> JSONResponse:   
    try:
        # Convert input data to DataFrame and preprocess   #I understand that instead of dict I need to put the class PassengerSatisfaction created and located in models folder but if i do that it does not work
        input_data = {
            "Gender": [passenger_features.gender],
            "Age": [passenger_features.age],
            "xx": [passenger_features.some_other_feature],  # Add other features here
            # ...
        }
        input_df = pd.DataFrame(input_data)

        # Make prediction using the loaded model
        prediction = predictor.predict(input_df)
        # Log prediction result
        logger.log_info(f"Prediction: {prediction}")

        return JSONResponse({"prediction": prediction.tolist()})
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
