#!/usr/bin/env python

import sys
import os
import logging



# Add the parent directory to sys.path

#parent_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
#sys.path.append(parent_dir)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

from load.load_data import DataRetriever
from preprocess.preprocess_data import MissingIndicator




#"""Tests for `luigicode` package."""
import os
import pytest
import pandas as pd

from sklearn.pipeline import Pipeline

#from load.load_data import DataRetriever
from preprocess.preprocess_data import MissingIndicator

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def does_csv_file_exist(file_path):
    """
    Check if a CSV file exists at the specified path.

    Parameters:
        file_path (str): The path to the CSV file.

    Returns:
        bool: True if the file exists, False otherwise.
    """
    logging.info(f"Checking if the CSV file exists at '{file_path}'...")
    return os.path.isfile(file_path)

def test_csv_file_existence():
    """
    Test case to check if the CSV file exists.
    """
    # Provide the path to your CSV file that needs to be tested
    csv_file_path = "./data/retrieved_data.csv"  # Update with the actual path
    
    DATASETS_DIR = './data/'
    
    #URL = 'https://www.openml.org/data/get_csv/16826755/phpMYEkMl'
    URL = 'https://github.com/luismeparra/luigicode/raw/main/data/train.csv'
    data_retriever = DataRetriever(URL, DATASETS_DIR)
    data_retriever.retrieve_data()

    logging.info("Starting the test_csv_file_existence function...")
    
    # Call the function to check if the CSV file exists
    file_exists = does_csv_file_exist(csv_file_path)

    # Use Pytest's assert statement to check if the file exists
    assert file_exists == True, f"The CSV file at '{csv_file_path}' does not exist."

    logging.info("Finished the test_csv_file_existence function.")
    
if __name__ == "__main__":
    # Run the test function using Pytest
    pytest.main([__file__])


def test_missing_indicator_transform():
    """
    Test the `transform` method of the MissingIndicator transformer.

    This test checks if the transformer correctly adds indicator features for missing values
    in the specified variables and returns the modified DataFrame.

    The test case uses a sample DataFrame with missing values and a custom transformer instance.

    It checks if the transformer successfully adds indicator features for the specified variables,
    and the transformed DataFrame has the expected additional columns.

    Note: Make sure to replace 'your_module' with the actual module name where the MissingIndicator class is defined.
    """
    # Sample DataFrame with missing values
    data = {
        'age': [25, 30, None, 40],
        'income': [50000, None, 75000, 60000],
        'gender': ['M', 'F', 'M', 'F']
    }
    df = pd.DataFrame(data)

    # Instantiate the custom transformer with specified variables
    missing_indicator = MissingIndicator(variables=['age', 'income'])

    # Transform the DataFrame using the custom transformer
    df_transformed = missing_indicator.transform(df)

    # Check if the transformed DataFrame has the expected additional columns
    expected_columns = ['age_nan', 'income_nan', 'gender']
    assert all(col in df_transformed.columns for col in expected_columns), \
        f"The transformed DataFrame should have the following additional columns: {expected_columns}"

    expected_values = [0, 1, 0, 0]
    assert all(df_transformed['income_nan'] == expected_values), \
        f"Expected values for 'income_nan': {expected_values}"

    # Check if the original DataFrame is not modified
    assert 'age_nan' not in df.columns, "The original DataFrame should not be modified."

def test_missing_indicator_fit():
    """
    Test the `fit` method of the MissingIndicator transformer.

    This test checks if the `fit` method returns the transformer instance itself,
    without performing any actual training or fitting.

    The test case uses a sample DataFrame and a custom transformer instance.

    Note: Make sure to replace 'your_module' with the actual module name where the MissingIndicator class is defined.
    """
    # Sample DataFrame
    data = {
        'age': [25, 30, 35, 40],
        'income': [50000, 60000, 75000, 80000],
        'gender': ['M', 'F', 'M', 'F']
    }
    df = pd.DataFrame(data)

    # Instantiate the custom transformer without specifying variables
    missing_indicator = MissingIndicator()

    # Fit the transformer to the DataFrame
    transformer_instance = missing_indicator.fit(df)

    # Check if the fit method returns the transformer instance itself
    assert transformer_instance == missing_indicator, \
        "The `fit` method should return the transformer instance itself."

def test_model_existence():
    """
    Test to validate the existence of a .pkl model file.

    This test function checks whether the specified .pkl model file exists
    in the specified directory.

    Raises:
        AssertionError: If the model file doesn't exist.

    Usage:
        Run this test using the pytest command:
        pytest test_model_existence.py
    """
    #model_filename = "random_forest_output.pkl"
    #MODEL_DIRECTORY = "/Users/luis.mendez/luigicode/models"
    model_path = "/Users/luis.mendez/luigicode/app/ml_models/random_forest_model_output.pkl"
    #model_path = 'https://github.com/luismeparra/luigicode/raw/main/models/random_forest_model_output.pkl'
    print(model_path)
    assert os.path.exists(model_path), f"Model file '{model_filename}' does not exist."

if __name__ == "__main__":
    # Run the test function using Pytest
    pytest.main([__file__])