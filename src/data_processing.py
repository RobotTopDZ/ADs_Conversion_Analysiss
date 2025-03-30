import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, StandardScaler

def load_data(file_path):
    """Loads the dataset from a CSV file."""
    return pd.read_csv(file_path)

def handle_missing_values(df, strategy="mean"):
    """Handles missing values by filling or dropping them."""
    for col in df.columns:
        if df[col].isnull().sum() > 0:
            if df[col].dtype == "object":
                df[col].fillna(df[col].mode()[0], inplace=True)
            else:
                if strategy == "mean":
                    df[col].fillna(df[col].mean(), inplace=True)
                elif strategy == "median":
                    df[col].fillna(df[col].median(), inplace=True)
    return df

def encode_categorical_features(df, categorical_columns):
    """Encodes categorical features using one-hot encoding."""
    encoder = OneHotEncoder(sparse_output=False, drop='first')
    encoded = encoder.fit_transform(df[categorical_columns])
    encoded_df = pd.DataFrame(encoded, columns=encoder.get_feature_names_out(categorical_columns))
    df = df.drop(columns=categorical_columns)
    df = pd.concat([df, encoded_df], axis=1)
    return df

def scale_features(df, numerical_columns):
    """Scales numerical features using StandardScaler."""
    scaler = StandardScaler()
    df[numerical_columns] = scaler.fit_transform(df[numerical_columns])
    return df

def preprocess_data(file_path, categorical_columns, numerical_columns, output_path="processed_data.csv"):
    """Full preprocessing pipeline."""
    df = load_data(file_path)
    df = handle_missing_values(df)
    df = encode_categorical_features(df, categorical_columns)
    df = scale_features(df, numerical_columns)
    df.to_csv(output_path, index=False)
    return df

# Example usage
if __name__ == "__main__":
    file_path = "../data/raw_data.csv"  # Adjust file path
    categorical_columns = ["Gender", "CampaignChannel", "CampaignType", "AdvertisingPlatform", "AdvertisingTool"]
    numerical_columns = ["Age", "Income", "AdSpend", "ClickThroughRate", "ConversionRate", "WebsiteVisits", "PagesPerVisit", "TimeOnSite", "SocialShares", "EmailOpens", "EmailClicks", "PreviousPurchases", "LoyaltyPoints"]
    processed_df = preprocess_data(file_path, categorical_columns, numerical_columns)
    print("Data Preprocessing Completed. Processed file saved.")
