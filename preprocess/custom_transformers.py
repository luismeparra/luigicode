from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import LabelEncoder
import pandas as pd

class CustomTransformer(BaseEstimator, TransformerMixin):
    """Custom transformer for data preprocessing."""
    
    def __init__(self, columns_to_encode):
        self.columns_to_encode = columns_to_encode

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Copy the DataFrame to avoid modifying the original
        X_transformed = X.copy()

        # Apply transformations to specified columns
        label_encoder = LabelEncoder()
        for col in self.columns_to_encode:
            X_transformed[col] = label_encoder.fit_transform(X_transformed[col])

        return X_transformed

# Define other custom transformers as needed
# For example, you can create a transformer to handle missing values or other preprocessing steps
