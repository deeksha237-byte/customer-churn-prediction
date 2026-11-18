
import streamlit as st
import pandas as pd
import joblib

# Load model
saved_objects = joblib.load("models/churn_prediction_model.pkl")
preprocessor = saved_objects["preprocessor"]
model = saved_objects["model"]

st.title("Telecom Customer Churn Prediction")
st.write("Enter customer details to predict churn.")

with st.form("customer_form"):

    st.subheader("Customer Information")

    gender = st.selectbox("Gender", ["Male", "Female"])
    senior = st.selectbox("Senior Citizen", ["No", "Yes"])
    partner = st.selectbox("Partner", ["No", "Yes"])
    dependents = st.selectbox("Dependents", ["No", "Yes"])

    tenure = st.number_input("Tenure Months", 0, 72, 12)

    phone = st.selectbox("Phone Service", ["No", "Yes"])
    multiple = st.selectbox(
        "Multiple Lines",
        ["No phone service", "No", "Yes"]
    )

    internet = st.selectbox(
        "Internet Service",
        ["DSL", "Fiber optic", "No"]
    )

    security = st.selectbox(
        "Online Security",
        ["No", "Yes", "No internet service"]
    )

    backup = st.selectbox(
        "Online Backup",
        ["No", "Yes", "No internet service"]
    )

    protection = st.selectbox(
        "Device Protection",
        ["No", "Yes", "No internet service"]
    )

    support = st.selectbox(
        "Tech Support",
        ["No", "Yes", "No internet service"]
    )

    tv = st.selectbox(
        "Streaming TV",
        ["No", "Yes", "No internet service"]
    )

    movies = st.selectbox(
        "Streaming Movies",
        ["No", "Yes", "No internet service"]
    )

    contract = st.selectbox(
        "Contract",
        ["Month-to-month", "One year", "Two year"]
    )

    paperless = st.selectbox("Paperless Billing", ["No", "Yes"])

    payment = st.selectbox(
        "Payment Method",
        [
            "Bank transfer (automatic)",
            "Credit card (automatic)",
            "Electronic check",
            "Mailed check"
        ]
    )

    monthly = st.number_input("Monthly Charges", min_value=0.0, value=70.0)
    total = st.number_input("Total Charges", min_value=0.0, value=840.0)
    cltv = st.number_input("CLTV", min_value=0, value=4000)

    submitted = st.form_submit_button("Predict Churn")


if submitted:

    # Create a DataFrame from customer inputs
    customer_data = pd.DataFrame([{
        "Gender": gender,
        "Senior Citizen": senior,
        "Partner": partner,
        "Dependents": dependents,
        "Tenure Months": tenure,
        "Phone Service": phone,
        "Multiple Lines": multiple,
        "Internet Service": internet,
        "Online Security": security,
        "Online Backup": backup,
        "Device Protection": protection,
        "Tech Support": support,
        "Streaming TV": tv,
        "Streaming Movies": movies,
        "Contract": contract,
        "Paperless Billing": paperless,
        "Payment Method": payment,
        "Monthly Charges": monthly,
        "Total Charges": total,
        "CLTV": cltv
    }])

    # Apply the same preprocessing used during training
    processed_data = preprocessor.transform(customer_data)

    # Make prediction
    prediction = model.predict(processed_data)[0]
    probability = model.predict_proba(processed_data)[0][1]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("Customer is likely to Churn!")
    else:
        st.success("Customer is likely to Stay!")

    st.metric("Churn Probability", f"{probability * 100:.2f}%")
