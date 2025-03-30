from src.data_preprocessing import clean_data
from src.feature_engineering import create_features
from src.model_training import train_model
from src.model_evaluation import evaluate_model

df = clean_data("data/raw_data.csv")

# Feature Engineering
df = create_features(df)

# Train Model
model = train_model(df)

# Evaluate Model
evaluate_model(model, df)
