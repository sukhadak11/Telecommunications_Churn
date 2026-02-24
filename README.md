# 📊 Telecom Customer Churn Prediction

## 🚀 Live Deployment
🔗 **Streamlit App:**  
https://telecommunication.streamlit.app/

---

## 📌 Project Overview

Customer churn is a major challenge in the telecommunications industry. Retaining existing customers is significantly more cost-effective than acquiring new ones.

This project aims to:

- Predict whether a customer is likely to churn
- Estimate churn probability
- Provide business insights for retention strategies
- Deploy the trained model using Streamlit for real-time predictions

---

## 🎯 Business Objective

To build a machine learning model that predicts customer churn probability based on customer usage patterns, subscription plans, and service behavior.

The goal is to help telecom companies:

- Identify high-risk customers
- Implement proactive retention strategies
- Reduce revenue loss

---

## 📂 Dataset Information

The dataset contains:

- 3333 customer records
- 19 features
- Binary target variable:
  - 1 → Churn
  - 0 → No Churn

### Key Features:
- Account length
- Voice mail plan
- International plan
- Day/Evening/Night minutes
- Customer service calls
- Total charges
- International minutes

---

## 🛠️ Project Workflow

### 1️⃣ Data Preprocessing
- Label encoding of categorical variables
- Outlier handling (Capping using IQR)
- Train-Test split (Stratified)
- Handling class imbalance

### 2️⃣ Model Building
Built and compared multiple models:

- Logistic Regression
- Decision Tree
- Random Forest
- Support Vector Machine
- XGBoost
- Artificial Neural Network (ANN)

### 3️⃣ Hyperparameter Tuning
Used **GridSearchCV** with 5-fold cross-validation.

Evaluation metric:
- ROC-AUC Score

### 4️⃣ Model Evaluation

Best Model: **XGBoost**

Performance Metrics:

- ✅ Accuracy: 97%
- ✅ ROC-AUC: 0.92
- ✅ Recall (Churn Class): 78%
- ✅ Precision (Churn Class): 99%

### 5️⃣ Threshold Tuning
Experimented with custom thresholds to improve recall.  
Default threshold (0.5) provided optimal performance balance.

---

## 📊 Feature Importance

Top features influencing churn:

- Customer Service Calls
- International Plan
- Total Charges
- Day Minutes
- International Minutes

These insights help businesses design targeted retention campaigns.

---

## 🌐 Deployment

The final model was deployed using **Streamlit Cloud**.

Features of the web application:

- User-friendly dashboard
- Real-time churn prediction
- Probability risk indicator
- Downloadable prediction report
- Feature importance visualization

🔗 Live App:  
https://telecommunication.streamlit.app/

---

## 🧠 Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- TensorFlow (ANN)
- Matplotlib
- Streamlit

---


---

## 📈 Key Learning Outcomes

- End-to-end ML pipeline development
- Handling imbalanced datasets
- Hyperparameter tuning
- Model evaluation using ROC-AUC
- Threshold optimization
- Real-world deployment using Streamlit

---

## 👩‍💻 Developed By

**Sukhada Khade**  
Machine Learning & Data Science Enthusiast  

---

⭐ If you found this project useful, feel free to star the repository!
