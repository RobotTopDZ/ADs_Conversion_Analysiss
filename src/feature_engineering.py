import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import logging

# Setup logging
logging.basicConfig(filename='logs/feature_engineering.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def feature_engineering(df):
    try:
        logging.info("Starting feature engineering.")
        
        
        if 'CustomerID' in df.columns:
            df = df.drop(columns=['CustomerID'])
        
        for col in df.select_dtypes(include=['number']).columns:
            df[col].fillna(df[col].mean(), inplace=True)
        
        for col in df.select_dtypes(include=['object']).columns:
            df[col].fillna(df[col].mode()[0], inplace=True)
        
        # Feature transformation
        df['Log_AdSpend'] = np.log1p(df['AdSpend'])
        df['Interaction_ClickConversion'] = df['ClickThroughRate'] * df['ConversionRate']
        
        
        cateorical_cols = ['Gender', 'CampaignChannel', 'CampaignType', 'AdvertisingPlatform', 'AdvertisingTool']
        g
        # Scale numerical features
        numerical_cols = ['Age', 'Income', 'AdSpend', 'ClickThroughRate', 'ConversionRate', 'WebsiteVisits',
                          'PagesPerVisit', 'TimeOnSite', 'SocialShares', 'EmailOpens', 'EmailClicks',
                          'PreviousPurchases', 'LoyaltyPoints', 'Log_AdSpend', 'Interaction_ClickConversion']
        scaler = StandardScaler()
        df[numerical_cols] = scaler.fit_transform(df[numerical_cols])
        
        logging.info("Feature engineering completed successfully.")
        return df
    
    except Exception as e:
        logging.error(f"Error in feature engineering: {str(e)}")
        raise e


if __name__ == "__main__":
    df = pd.read_csv("data/raw_data.csv")
    processed_df = feature_engineering(df)
    processed_df.to_csv("data/processed_data.csv", index=False)
