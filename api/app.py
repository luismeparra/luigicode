
from fastapi import FastAPI, HTTPException
from train.train_model import train_random_forest
from train.train_pipeline import train_pipeline  # Import your actual training function
from preprocess.custom_transformers import CustomTransformer
import pandas as pd
import joblib

app = FastAPI()

# Load the trained model
model_path = "./models/random_forest_model.pkl"  # Update with your actual path
loaded_model = joblib.load(model_path)

# Define endpoint to train a new model
@app.post("/train")
def train_new_model():
    # Load and preprocess data
    data = pd.read_csv("./data/train.csv")  # Update with your actual path
    X = data.drop("satisfactionN", axis=1)
    y = data["satisfactionN"]

    # Train the model using your training function
    trained_model = train_pipeline(X, y)  # Update with your actual training function

    # Save the trained model
    model_filename = "./models/new_trained_model.pkl"
    joblib.dump(trained_model, model_filename)

    return {"message": "New model trained and saved."}

# Define endpoint to make predictions
@app.post("/predict")
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
