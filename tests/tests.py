#!/usr/bin/env python

"""Tests for your project package."""
import os
import pytest
import pandas as pd
from preprocess.custom_transformers import CustomTransformer  # Import your custom transformer

def test_custom_transformer():
    """
    Test the `transform` method of your custom transformer.

    This test checks if your custom transformer correctly encodes categorical variables
    and returns the transformed DataFrame.

    Make sure to replace 'CustomTransformer' with the actual name of your custom transformer class.
    """
    # Sample input data
    data = {
        'Gender': ['M', 'F', 'M'],
        'Customer Type': ['Loyal', 'Regular', 'Loyal'],
        'Type of Travel': ['Business', 'Leisure', 'Business'],
        'Class': ['Business', 'Eco', 'Eco']
    }
    df = pd.DataFrame(data)

    # Instantiate your custom transformer
    custom_transformer = CustomTransformer(columns_to_encode=['Gender', 'Customer Type', 'Type of Travel', 'Class'])

    # Transform the DataFrame using your custom transformer
    df_transformed = custom_transformer.transform(df)

    # Check if the transformed DataFrame has the expected shape
    expected_shape = (3, 10)  # Update this with the actual shape after transformation
    assert df_transformed.shape == expected_shape, \
        f"The transformed DataFrame should have shape {expected_shape}"

def test_csv_file_existence():
    """
    Test case to check if the CSV file exists.
    """
    # Provide the path to your CSV file that needs to be tested
    csv_file_path = "./data/train.csv"  # Update this with the actual path

    # Call the function to check if the CSV file exists
    file_exists = os.path.isfile(csv_file_path)

    # Use Pytest's assert statement to check if the file exists
    assert file_exists == True, f"The CSV file at '{csv_file_path}' does not exist."

if __name__ == "__main__":
    # Run the test functions using Pytest
    pytest.main([__file__])
