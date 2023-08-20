from fastapi import FastAPI, HTTPException
from train.train_pipeline import train_pipeline
from preprocess.custom_transformers import CustomTransformer
import pandas as pd
import joblib

app = FastAPI()

# Load the trained model
model_path = "./models/random_forest_model_output.pkl"
loaded_model = joblib.load(model_path)

# Define endpoint to train a new model
@app.post("./train")
def train_new_model():
    # Load and preprocess data
    data = pd.read_csv("./data/train.csv")
    X = data.drop("satisfaction", axis=1)
    y = data["satisfaction"]

    # Train the model using your training function
    trained_model = train_pipeline(X, y)

    # Save the trained model
    model_filename = "./models/new_trained_model.pkl"
    joblib.dump(trained_model, model_filename)

    return {"message": "New model trained and saved."}

# Define endpoint to make predictions
@app.post("./api/predict")
def predict_new_value(data: dict):
    try:
        # Convert input data to DataFrame and preprocess
        input_df = pd.DataFrame(data, index=[0])
        preprocessor = CustomTransformer(columns_to_encode=['Gender', 'Customer Type', 'Type of Travel', 'Class'])
        input_df = preprocessor.transform(input_df)

        # Make prediction using the loaded model
        prediction = loaded_model.predict(input_df)

        return {"prediction": prediction.tolist()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
