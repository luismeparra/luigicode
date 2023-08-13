"""Main module."""
from load.load_data import DataRetriever
from train.train_data import PassengerSatisfactionPipeline  # Updated class name
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

DATASETS_DIR = './data/'
URL = 'https://www.openml.org/data/get_csv/16826755/phpMYEkMl'
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
        df.drop('satisfactionN', axis=1),
        df['satisfactionN'],
        test_size=0.2,
        random_state=404
    )
    
    # Instantiate the PassengerSatisfactionPipeline class
    satisfaction_pipeline = PassengerSatisfactionPipeline(
        seed_model=SEED_MODEL,
        numerical_vars=NUMERICAL_VARS,
        categorical_vars=CATEGORICAL_VARS,
        selected_features=SELECTED_FEATURES
    )
    
    random_forest_model = satisfaction_pipeline.fit_random_forest(X_train, y_train)
    
    X_test_processed = satisfaction_pipeline.PIPELINE.transform(X_test)
    y_pred = random_forest_model.predict(X_test_processed)
    
    acc = accuracy_score(y_test, y_pred)
    print(f'Test accuracy: {acc}')
    
    # Save the model using joblib
    save_path = TRAINED_MODEL_DIR + PIPELINE_SAVE_FILE
    joblib.dump(random_forest_model, save_path)
    print(f"Model saved in {save_path}")

if __name__ == "__main__":
    main()

#######################  VF ###############################
"""Main module."""
from load.load_data import DataRetriever
from train.train_data import PassengerSatisfactionPipeline
import pandas as pd
from sklearn.model_selection import train_test_split
import joblib
from sklearn.metrics import accuracy_score, roc_auc_score

# Constants for data and model paths
DATASETS_DIR = './data/'
URL = 'https://www.kaggle.com/datasets/teejmahal20/airline-passenger-satisfaction?resource=download'
# ... (other constants)

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
        df.drop(TARGET, axis=1),
        df[TARGET],
        test_size=0.2,
        random_state=404
    )
    
    # Instantiate the PassengerSatisfactionPipeline class
    satisfaction_pipeline = PassengerSatisfactionPipeline(
        seed_model=SEED_MODEL,
        numerical_vars=NUMERICAL_VARS,
        categorical_vars_with_na=CATEGORICAL_VARS_WITH_NA,
        numerical_vars_with_na=NUMERICAL_VARS_WITH_NA,
        categorical_vars=CATEGORICAL_VARS,
        selected_features=SELECTED_FEATURES
    )
    
    logistic_regression_model = satisfaction_pipeline.fit_logistic_regression(X_train, y_train)
    
    # ... (rest of the code)

if __name__ == "__main__":
    main()
