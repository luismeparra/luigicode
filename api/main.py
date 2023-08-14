from fastapi import FastAPI, HTTPException
from train.train_data import PassengerSatisfactionPipeline
import joblib
import pandas as pd
from pydantic import BaseModel

app = FastAPI()

class PassengerInfo(BaseModel):
    pclass: int
    gender: int
    age: float
    sibsp: int
    parch: int
    fare: float
    cabin: str
    embarked: str
    title: str
    pclass_nan: int
    age_nan: int
    sibsp_nan: int
    parch_nan: int
    fare_nan: int
    gender_male: int
    cabin_Missing: int
    cabin_rare: int
    embarked_Q: int
    embarked_S: int
    title_Mr: int
    title_Mrs: int
    title_rare: int

model_path = './models/logistic_regression_output.pkl'
loaded_model = joblib.load(model_path)

@app.post("/train-model")
def train_new_model():
    # Call the training function from the PassengerSatisfactionPipeline class
    # Return a message indicating success or failure
    pass


@app.post("/predict")
def predict_passenger_satisfaction(passenger: PassengerInfo):
    # Convert the input data into a DataFrame
    input_data = pd.DataFrame([passenger.dict()])
    
    # Apply any preprocessing required for prediction
    # For example, apply OneHotEncoder to categorical variables
    
    # Make predictions using the loaded model
    prediction = loaded_model.predict(input_data)
    
    # Return the prediction result
    return {"prediction": prediction[0]}


#uvicorn api.main:app --host 0.0.0.0 --port 8000

