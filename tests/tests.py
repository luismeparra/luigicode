#!/usr/bin/env python

"""Tests for `luigicode` package."""
import os
import pytest
import pandas as pd

from sklearn.pipeline import Pipeline

from load.load_data import DataRetriever
from .preprocess.preprocess_data import MissingIndicator

def does_csv_file_exist(file_path):
    """
    Check if a CSV file exists at the specified path.

    Parameters:
        file_path (str): The path to the CSV file.

    Returns:
        bool: True if the file exists, False otherwise.
    """
    return os.path.isfile(file_path)

def test_csv_file_existence():
    """
    Test case to check if the CSV file exists.
    """
    # Provide the path to your CSV file that needs to be tested
    csv_file_path = "./data/retrieved_data.csv"  # Update with the actual path
    
    DATASETS_DIR = './data/'
    
    URL = 'https://www.openml.org/data/get_csv/16826755/phpMYEkMl'
    data_retriever = DataRetriever(URL, DATASETS_DIR)
    data_retriever.retrieve_data()

    # Call the function to check if the CSV file exists
    file_exists = does_csv_file_exist(csv_file_path)

    # Use Pytest's assert statement to check if the file exists
    assert file_exists == True, f"The CSV file at '{csv_file_path}' does not exist."

if __name__ == "__main__":
    # Run the test function using Pytest
    pytest.main([__file__])
