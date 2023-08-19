#def train_random_forest(X: DataFrame, y: Series) -> RandomForestClassifier:
#    """Train a RandomForestClassifier.
#    
#    Args:
#        X (DataFrame): Feature matrix.
#        y (Series): Target labels.
#    
#    Returns:
#        RandomForestClassifier: Trained model.
#    """
#    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#    model = RandomForestClassifier(n_estimators=100, criterion='entropy', random_state=0, n_jobs=-1)
#    model.fit(X_train, y_train)
#    return model


######

### VF ###

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestClassifier  # Import RandomForestClassifier
import joblib

class PassengerSatisfactionPipeline:
    def __init__(self, seed_model, numerical_vars, categorical_vars_with_na, numerical_vars_with_na,
                 categorical_vars, selected_features):
        self.seed_model = seed_model
        self.numerical_vars = numerical_vars
        self.categorical_vars_with_na = categorical_vars_with_na
        self.numerical_vars_with_na = numerical_vars_with_na
        self.categorical_vars = categorical_vars
        self.selected_features = selected_features

    def _create_preprocessing_pipeline(self):
        # Create transformers for numerical and categorical variables
        numerical_transformer = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='median')),
            ('scaler', StandardScaler())
        ])
        categorical_transformer = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='most_frequent')),
            ('encoder', OneHotEncoder(handle_unknown='ignore'))
        ])

        # Combine transformers using ColumnTransformer
        preprocessor = ColumnTransformer(
            transformers=[
                ('num', numerical_transformer, self.numerical_vars),
                ('cat', categorical_transformer, self.categorical_vars)
            ])

        # Create the full preprocessing pipeline with the RandomForestClassifier model
        preprocessing_pipeline = Pipeline(steps=[
            ('preprocessor', preprocessor),
            ('model', RandomForestClassifier(random_state=self.seed_model))  # Use RandomForestClassifier
        ])

        return preprocessing_pipeline

    def fit_random_forest(self, X_train, y_train):
        # Create the preprocessing pipeline
        preprocessing_pipeline = self._create_preprocessing_pipeline()

        # Fit the pipeline on the training data
        trained_pipeline = preprocessing_pipeline.fit(X_train, y_train)

        return trained_pipeline

# Save the trained model using joblib
def save_model(model, model_filename):
    with open(model_filename, 'wb') as model_file:
        joblib.dump(model, model_file)

