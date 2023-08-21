#!/usr/bin/env python

import sys
import os
import logging



# Add the parent directory to sys.path

#parent_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
#sys.path.append(parent_dir)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

from load.load_data import DataRetriever




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
