# Data Dictionary

This document provides an explanation of all features in the dataset used for model training and prediction.

## **Feature Descriptions**

### **1. CustomerID** *(Integer)*
- Unique identifier for each customer.
- Not used in model training but kept for reference.

### **2. Age** *(Integer)*
- Age of the customer in years.
- Used as a numerical predictor for customer behavior.

### **3. Gender** *(Categorical)*
- Gender of the customer.
- Possible values: `Male`, `Female`.
- One-hot encoded during feature engineering.

### **4. Income** *(Float)*
- Annual income of the customer.
- Measured in currency units (e.g., USD, DZD).

### **5. CampaignChannel** *(Categorical)*
- The marketing channel used to reach the customer.
- Possible values: `Social Media`, `Email`, `TV`, `Radio`, etc.
- One-hot encoded during feature engineering.

### **6. CampaignType** *(Categorical)*
- Type of marketing campaign the customer was exposed to.
- Possible values: `Discount`, `Loyalty Program`, `Referral`, etc.
- One-hot encoded during feature engineering.

### **7. AdSpend** *(Float)*
- The amount spent on advertising per customer.
- Measured in currency units.

### **8. ClickThroughRate** *(Float)*
- The ratio of clicks on an advertisement to the number of times it was displayed.
- Expressed as a percentage.

### **9. ConversionRate** *(Float)*
- The ratio of users who completed a desired action (e.g., purchase) after clicking on an ad.
- Expressed as a percentage.

### **10. WebsiteVisits** *(Integer)*
- Number of visits the customer made to the website.

### **11. PagesPerVisit** *(Float)*
- Average number of pages viewed per session.

### **12. TimeOnSite** *(Float)*
- Average time (in minutes) the customer spends on the website.

### **13. SocialShares** *(Integer)*
- Number of times the customer shared content on social media.

### **14. EmailOpens** *(Integer)*
- Number of times the customer opened an email marketing campaign.

### **15. EmailClicks** *(Integer)*
- Number of times the customer clicked on a link inside an email.

### **16. PreviousPurchases** *(Integer)*
- The number of previous purchases made by the customer.

### **17. LoyaltyPoints** *(Integer)*
- The number of loyalty points accumulated by the customer.

### **18. AdvertisingPlatform** *(Categorical)*
- The platform where advertisements were displayed.
- Possible values: `Google`, `Facebook`, `Instagram`, `TikTok`, etc.
- One-hot encoded during feature engineering.

### **19. AdvertisingTool** *(Categorical)*
- The specific tool or technique used for advertising.
- Possible values: `SEO`, `PPC`, `Influencer Marketing`, etc.
- One-hot encoded during feature engineering.

### **20. Conversion** *(Binary - Target Variable)*
- Whether the customer converted (e.g., made a purchase).
- Possible values: `0` (No), `1` (Yes).
- Used as the target variable for model training.

---

This data dictionary serves as a reference for understanding the dataset and its role in the model training and prediction process.

