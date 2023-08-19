import os
import pytest
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from train.train_pipeline import train_pipeline
from preprocess.custom_transformers import CustomTransformer

# You might need to adjust the import paths based on your project structure

@pytest.fixture
def sample_data():
    data = {
        'Age': [25, 30, 35, 40],
        'Flight Distance': [1000, 1500, 800, 2000],
        'Gender': ['Male', 'Female', 'Male', 'Female'],
        'Customer Type': ['Loyal', 'Disloyal', 'Loyal', 'Loyal'],
        'Type of Travel': ['Business', 'Personal', 'Business', 'Business'],
        'Class': ['Business', 'Eco', 'Business', 'Eco'],
        'satisfactionN': [1, 0, 1, 1]
    }
    return pd.DataFrame(data)

def test_train_pipeline(sample_data):
    X = sample_data.drop('satisfactionN', axis=1)
    y = sample_data['satisfactionN']

    model = train_pipeline(X, y)

    assert isinstance(model, RandomForestClassifier), "The trained model should be a RandomForestClassifier."

def test_custom_transformer(sample_data):
    preprocessor = CustomTransformer(columns_to_encode=['Gender', 'Customer Type', 'Type of Travel', 'Class'])
    transformed_data = preprocessor.transform(sample_data)

    assert transformed_data.shape[0] == sample_data.shape[0], "Number of rows should remain the same after transformation."
    assert transformed_data.shape[1] > sample_data.shape[1], "Number of columns should increase after encoding."

# Add more test cases as needed for your specific functions and classes

if __name__ == "__main__":
    pytest.main([__file__])
