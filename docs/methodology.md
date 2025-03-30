# Methodology

## Step 1: Data Collection
We gathered raw data containing various customer attributes, engagement metrics, and advertising campaign performance indicators. This dataset included structured information such as age, income, advertising channels, conversion rates, and other behavioral metrics.

## Step 2: Data Exploration & Cleaning
Using `01_data_exploration.ipynb`, we performed:
- **Missing Value Handling:** Imputed or removed missing data points.
- **Outlier Detection:** Used statistical methods to detect anomalies.
- **Data Type Normalization:** Converted categorical and numerical values into appropriate formats.

## Step 3: Feature Engineering
In `02_feature_engineering.ipynb`, we transformed raw data into meaningful features:
- **Encoding Categorical Variables:** Applied one-hot encoding to categorical features.
- **Feature Scaling:** Standardized numerical features for consistent model performance.
- **Feature Selection:** Identified the most relevant features to improve model efficiency.

## Step 4: Model Selection & Training
In `03_model_training.ipynb`, we tested multiple machine learning models, including:
- **Stacking Classifier (Best Model)**
- Gradient Boosting
- XGBoost
- Voting Classifier
- CatBoost
- LightGBM
- Random Forest

Hyperparameter tuning was performed to optimize each model’s performance, and cross-validation ensured robustness.

## Step 5: Model Evaluation
We benchmarked the models based on:
- **Accuracy, Precision, Recall, and F1-score.**
- Comparison across different classifiers.
- **Feature Importance Analysis** to understand key predictors.

## Step 6: Deployment & API Development
We built a Flask-based web application allowing:
- CSV file upload & manual feature input.
- Real-time predictions.
- Data visualization & insights.
- Downloadable reports (CSV/PDF).

## Step 7: CI/CD & Model Automation
- Developed an automated `model_training.py` script to retrain models when new data is available.
- Integrated logging and error-handling mechanisms.
- Established a systematic pipeline for continuous improvement.

## Step 8: Limitations & Future Work
- Potential data biases due to imbalanced datasets.
- Need for further feature refinement.
- Enhancing model generalizability with additional real-world datasets.

This methodology ensures a comprehensive, scalable, and effective machine-learning pipeline for predictive analytics.

