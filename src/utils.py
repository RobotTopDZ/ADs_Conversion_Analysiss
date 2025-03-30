import logging
import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import joblib

def setup_logging(log_file="logs/app.log"):
    """Configures logging settings."""
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

def log_message(message, level="info"):
    """Logs a message at the specified level."""
    if level == "info":
        logging.info(message)
    elif level == "error":
        logging.error(message)
    elif level == "warning":
        logging.warning(message)
    elif level == "debug":
        logging.debug(message)
    else:
        logging.info(message)

def save_model(model, filename="models/model.pkl"):
    """Saves the trained model to a file."""
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    joblib.dump(model, filename)
    log_message(f"Model saved to {filename}")

def load_model(filename="models/model.pkl"):
    """Loads a trained model from a file."""
    if os.path.exists(filename):
        log_message(f"Model loaded from {filename}")
        return joblib.load(filename)
    else:
        log_message(f"Model file not found: {filename}", "error")
        return None

def plot_feature_importance(model, feature_names, save_path="reports/feature_importance.png"):
    """Plots and saves feature importance."""
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    importance = model.feature_importances_
    feature_importance_df = pd.DataFrame({"Feature": feature_names, "Importance": importance})
    feature_importance_df = feature_importance_df.sort_values(by="Importance", ascending=False)
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x="Importance", y="Feature", data=feature_importance_df, palette="viridis")
    plt.title("Feature Importance")
    plt.xlabel("Importance")
    plt.ylabel("Feature")
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()
    log_message(f"Feature importance plot saved to {save_path}")
