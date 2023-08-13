# test_model_existence.py
import pytest
import joblib
from your_module import loaded_model  # Import your loaded model

def test_loaded_model_existence():
    assert isinstance(loaded_model, joblib.base.BaseEstimator), "Loaded model does not exist"
