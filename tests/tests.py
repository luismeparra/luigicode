import os
import pytest
import pandas as pd
from train.train_pipeline import train_pipeline  # Import your actual training function

def test_train_pipeline():
    # Sample data for testing
    data = {
        'Feature1': [1, 2, 3],
        'Feature2': [4, 5, 6],
        'satisfaction': [0, 1, 0]
    }
    df = pd.DataFrame(data)

    X = df.drop("satisfaction", axis=1)
    y = df["satisfaction"]

    # Test train_pipeline function
    model = train_pipeline(X, y)

    assert model is not None, "Training pipeline should return a model."

if __name__ == "__main__":
    # Run the test function using Pytest
    pytest.main([__file__])
