from sklearn.ensemble import RandomForestClassifier

def train_pipeline(X, y):
    """
    Train a machine learning pipeline.
    
    Args:
        X (DataFrame): Feature matrix.
        y (Series): Target labels.
    
    Returns:
        trained_model: Trained machine learning model.
    """
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    return model
