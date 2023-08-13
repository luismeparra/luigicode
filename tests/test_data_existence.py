# test_data_existence.py
import pytest
from your_module import X_train, y_train  # Import your training data

def test_training_data_existence():
    assert len(X_train) > 0, "No training data available"
    assert len(y_train) > 0, "No target labels available"
