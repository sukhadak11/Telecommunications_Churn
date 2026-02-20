import streamlit as st
import pandas as pd
import joblib
import xgboost
import matplotlib.pyplot as plt

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Telecom Churn Dashboard",
                   page_icon="📊",
                   layout="wide")

# ---------------- LOAD MODEL ----------------
model = joblib.load("final_xgb_model.pkl")

# ---------------- HEADER ----------------
st.title("📊 Telecom Customer Churn Prediction")
st.markdown("---")

# ---------------- SIDEBAR ----------------
if False:
    st.sidebar.title("📌 Model Info")
    st.sidebar.info("""
    Model: XGBoost  
    ROC-AUC: 0.92  
    Accuracy: 97%  
    Recall: 78%
    """)

# ---------------- FORM START ----------------
with st.form("prediction_form"):

    st.subheader("👤 Enter Customer Details")

    col1, col2 = st.columns(2)

    with col1:
        account_length = st.number_input("Account Length", min_value=0)
        voice_mail_plan = st.selectbox("Voice Mail Plan", ["Select", "Yes", "No"])
        voice_mail_messages = st.number_input("Voice Mail Messages", min_value=0)
        customer_service_calls = st.number_input("Customer Service Calls", min_value=0)

    with col2:
        international_plan = st.selectbox("International Plan", ["Select", "Yes", "No"])
        day_mins = st.number_input("Day Minutes")
        evening_mins = st.number_input("Evening Minutes")
        night_mins = st.number_input("Night Minutes")
        international_mins = st.number_input("International Minutes")
        total_charge = st.number_input("Total Charge")

    submitted = st.form_submit_button("🔍 Predict Churn")

# ---------------- PREDICTION ----------------
if submitted:

    # Validation
    if voice_mail_plan == "Select" or international_plan == "Select":
        st.warning("⚠ Please select all categorical options.")
    elif account_length == 0 and day_mins == 0 and total_charge == 0:
        st.warning("⚠ Please enter meaningful customer details.")
    else:

        # Convert categorical
        voice_mail_plan_val = 1 if voice_mail_plan == "Yes" else 0
        international_plan_val = 1 if international_plan == "Yes" else 0

        input_data = pd.DataFrame([[ 
            account_length,
            voice_mail_plan_val,
            voice_mail_messages,
            day_mins,
            evening_mins,
            night_mins,
            international_mins,
            customer_service_calls,
            international_plan_val,
            0, 0, 0, 0, 0, 0, 0, 0,
            total_charge
        ]], columns=[
            'account_length','voice_mail_plan','voice_mail_messages',
            'day_mins','evening_mins','night_mins','international_mins',
            'customer_service_calls','international_plan',
            'day_calls','day_charge','evening_calls','evening_charge',
            'night_calls','night_charge','international_calls','international_charge',
            'total_charge'
        ])

        prediction = model.predict(input_data)
        probability = model.predict_proba(input_data)[0][1]

        st.markdown("---")
        st.subheader("📊 Prediction Result")

        colA, colB = st.columns(2)
        colA.metric("Churn Probability", f"{probability:.2%}")
        colB.metric("Model Decision", "Churn" if prediction[0]==1 else "Stay")

        st.progress(float(probability))

        if probability > 0.7:
            st.error("🔴 High Churn Risk")
        elif probability > 0.4:
            st.warning("🟡 Moderate Churn Risk")
        else:
            st.success("🟢 Low Churn Risk")

        # Download Report
        report = pd.DataFrame({
            "Churn Probability": [probability],
            "Prediction": ["Churn" if prediction[0]==1 else "Stay"]
        })

        st.download_button(
            "📥 Download Prediction Report",
            report.to_csv(index=False),
            file_name="churn_prediction.csv",
            mime="text/csv"
        )

