from sklearn.base import BaseEstimator, ClassifierMixin

class CustomClassifier(BaseEstimator, ClassifierMixin):
    """Custom classifier using a trained model for predictions."""
    
    def __init__(self, model):
        self.model = model

    def fit(self, X, y):
        self.model.fit(X, y)
        return self

    def predict(self, X):
        return self.model.predict(X)
