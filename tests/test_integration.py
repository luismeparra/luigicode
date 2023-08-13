# test_integration.py
import pytest
from your_module import X_train, y_train, YourCustomTransformer1, YourCustomTransformer2, loaded_model

@pytest.fixture(scope="module")
def transformed_data():
    transformer1 = YourCustomTransformer1()
    transformer2 = YourCustomTransformer2()

    X_transformed = transformer2.transform(transformer1.transform(X_train))
    return X_transformed

def test_all_functions_work(transformed_data):
    assert len(X_train) == len(transformed_data)
    assert len(y_train) == len(transformed_data)
    assert isinstance(loaded_model, joblib.base.BaseEstimator)

    # Add more assertions to validate other functions

