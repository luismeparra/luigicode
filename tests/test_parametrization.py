# test_parametrization.py
import pytest
from your_module import X_train, y_train, YourCustomTransformer1, YourCustomTransformer2, loaded_model

@pytest.fixture(scope="module")
def transformed_data():
    transformer1 = YourCustomTransformer1()
    transformer2 = YourCustomTransformer2()

    X_transformed = transformer2.transform(transformer1.transform(X_train))
    return X_transformed

@pytest.mark.parametrize("sample_idx", range(100))
def test_large_dataset(sample_idx, transformed_data):
    assert transformed_data[sample_idx] is not None
    assert y_train[sample_idx] is not None
    assert isinstance(loaded_model.predict([transformed_data[sample_idx]]), (int, float))

    # Add more assertions to validate other aspects of the predictions

