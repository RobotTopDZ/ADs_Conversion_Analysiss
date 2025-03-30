import joblib
import numpy as np

# Load the Stacking Classifier model
model = joblib.load("models/CatBoost_Tuned.pkl")

def predict(features):
    """Takes a list of features and returns the model's prediction."""
    features = np.array(features).reshape(1, -1)
    return model.predict(features)[0]
