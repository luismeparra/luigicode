import pandas as pd
from typing import DataFrame

#This function allows to load data set that will use

def load_data(filepath: str) -> DataFrame:
    """Load data from a CSV file.
    
    Args:
        filepath (str): Path to the CSV file.
    
    Returns:
        DataFrame: Loaded data.
    """
    data = pd.read_csv(filepath)
    return data
