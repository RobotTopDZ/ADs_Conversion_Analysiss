import os
import numpy as np
import pandas as pd
import logging
import joblib
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, f1_score
from imblearn.over_sampling import SMOTE
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier

# Logging setup
logging.basicConfig(filename='training.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Load dataset
def load_data(file_path):
    df = pd.read_csv(file_path)
    logging.info("Data loaded successfully")
    return df

# Preprocess data
def preprocess_data(df):
    df = df.dropna()
    X = df.drop(columns=['Conversion'])
    y = df['Conversion']
    X = pd.get_dummies(X)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    if np.bincount(y_train)[0] / np.bincount(y_train)[1] > 2:
        smote = SMOTE(random_state=42)
        X_train, y_train = smote.fit_resample(X_train, y_train)
    
    return X_train, X_test, y_train, y_test

# Train models and find the best one
def train_models(X_train, y_train, X_test, y_test):
    models = {
        'RandomForest': RandomForestClassifier(n_estimators=100, random_state=42),
        'GradientBoosting': GradientBoostingClassifier(n_estimators=100, random_state=42),
        'XGBoost': XGBClassifier(use_label_encoder=False, eval_metric='logloss'),
        'LGBM': LGBMClassifier()
    }
    
    best_model = None
    best_score = 0
    
    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        score = f1_score(y_test, y_pred)
        
        if score > best_score:
            best_model = model
            best_score = score
        
        logging.info(f"{name} - F1 Score: {score:.4f}")
    
    return best_model

# Save best model
def save_model(model, filename='best_model.pkl'):
    joblib.dump(model, filename)
    logging.info(f"Best model saved: {filename}")

if __name__ == "__main__":
    try:
        df = load_data("raw_data.csv")
        X_train, X_test, y_train, y_test = preprocess_data(df)
        best_model = train_models(X_train, y_train, X_test, y_test)
        save_model(best_model)
        logging.info("Model training completed successfully.")
    except Exception as e:
        logging.error(f"Error in training pipeline: {str(e)}")
