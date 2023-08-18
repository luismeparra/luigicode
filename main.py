#######################  VF ###############################

"""Main module."""
from load.load_data import DataRetriever
from train.train_model import PassengerSatisfactionPipeline
import pandas as pd
from sklearn.model_selection import train_test_split
import joblib
from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn.ensemble import RandomForestClassifier

# Constants for data and model paths
DATASETS_DIR = './data/'
URL = 'https://github.com/luismeparra/luigicode/raw/main/data/train.csv'

RETRIEVED_DATA = 'retrieved_data.csv'
SEED_MODEL = 404

NUMERICAL_VARS = ['Age', 'Flight Distance', 'Departure Delay in Minutes', 'Arrival Delay in Minutes']
CATEGORICAL_VARS = ['Gender', 'Customer Type', 'Type of Travel', 'Class', 'Inflight wifi service', 'Online boarding', 'Seat comfort', 'Inflight entertainment', 'On-board service', 'Leg room service', 'Baggage handling', 'Checkin service', 'Cleanliness']

SELECTED_FEATURES = NUMERICAL_VARS + CATEGORICAL_VARS

TRAINED_MODEL_DIR = './models/'
PIPELINE_NAME = 'random_forest_model'
PIPELINE_SAVE_FILE = f'{PIPELINE_NAME}_output.pkl'

def main():
    """Main function."""
    # Retrieve data
    data_retriever = DataRetriever(URL, DATASETS_DIR)
    result = data_retriever.retrieve_data()
    print(result)
    
    # Read data
    df = pd.read_csv(DATASETS_DIR + RETRIEVED_DATA)
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        df.drop('satisfaction', axis=1),
        df['satisfaction'],
        test_size=0.2,
        random_state=404
    )
    
    # Instantiate the PassengerSatisfactionPipeline class
    satisfaction_pipeline = PassengerSatisfactionPipeline(
        seed_model=SEED_MODEL,
        numerical_vars=NUMERICAL_VARS,
        categorical_vars_with_na=[],  # No categorical vars with missing values
        numerical_vars_with_na=NUMERICAL_VARS,
        categorical_vars=CATEGORICAL_VARS,
        selected_features=SELECTED_FEATURES
    )
    
    # Fit the RandomForest model
    rf_model = satisfaction_pipeline.fit_random_forest(X_train, y_train)
    
    # Save the trained model using joblib
    save_path = TRAINED_MODEL_DIR + PIPELINE_SAVE_FILE
    joblib.dump(rf_model, save_path)
    print(f"Model saved in {save_path}")

if __name__ == "__main__":
    main()
