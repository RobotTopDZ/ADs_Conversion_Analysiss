from flask import Flask, render_template, request, jsonify, send_file
from flask_bootstrap import Bootstrap
import logging
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.io as pio
from model_loader import predict

# Initialize Flask app
app = Flask(__name__)
Bootstrap(app)

# Logging
logging.basicConfig(filename="logs/app.log", level=logging.INFO)

TRAIN_FEATURES = [
    "Age", "Gender", "Income", "CampaignChannel", "CampaignType", "AdSpend",
    "ClickThroughRate", "ConversionRate", "WebsiteVisits", "PagesPerVisit",
    "TimeOnSite", "SocialShares", "EmailOpens", "EmailClicks",
    "PreviousPurchases", "LoyaltyPoints", "AdvertisingPlatform", "AdvertisingTool"
]

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def make_prediction():
    try:
        if "file" in request.files:
            file = request.files["file"]
            if file.filename == "":
                return jsonify({"error": "No selected file"})
            
            # Read CSV and preprocess
            df = pd.read_csv(file)
        else:
            # Manual Input Processing
            data = request.json
            df = pd.DataFrame([data])

        # One-hot encode categorical features
        df = pd.get_dummies(df, columns=["Gender", "CampaignChannel", "CampaignType", "AdvertisingPlatform", "AdvertisingTool"])
        df = df.reindex(columns=TRAIN_FEATURES, fill_value=0)

        # Make predictions
        df["Prediction"] = predict(df)

        # Generate Report
        report_path = "static/prediction_report.csv"
        df.to_csv(report_path, index=False)
        
        return jsonify({"message": "Prediction successful", "download_url": report_path})
    except Exception as e:
        logging.error(f"Error processing prediction: {e}")
        return jsonify({"error": f"Error processing file: {str(e)}"})

@app.route("/visualization", methods=["GET"])
def visualization():
    try:
        # Load data (assumed recent predictions for visualization)
        df = pd.read_csv("static/prediction_report.csv")
        
        # Generate Histogram for Ad Spend
        plt.figure(figsize=(8, 5))
        sns.histplot(df["AdSpend"], bins=20, kde=True)
        plt.title("Ad Spend Distribution")
        plt.savefig("static/ad_spend_histogram.png")
        plt.close()
        
        # Pie chart of Predictions
        fig = px.pie(df, names="Prediction", title="Prediction Breakdown")
        pio.write_image(fig, "static/prediction_pie_chart.png")
        
        return jsonify({"message": "Visualizations generated successfully"})
    except Exception as e:
        logging.error(f"Error generating visualizations: {e}")
        return jsonify({"error": f"Error generating visualization: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)
