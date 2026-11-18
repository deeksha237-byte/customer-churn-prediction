
# Telecom Customer Churn Prediction

## Project Overview
This project uses machine learning to predict whether a telecom customer is likely to leave the company (churn).

## Objectives
- Analyze customer data and identify churn patterns.
- Perform data cleaning and exploratory data analysis.
- Build and evaluate machine learning models.
- Identify important factors influencing customer churn.
- Explain model predictions using SHAP.

## Dataset
- Total records: 7,043
- Original features: 33
- Target variable: `Churn Value`
- 0 = No Churn
- 1 = Churn

## Technologies Used
- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- Scikit-learn
- SHAP
- Jupyter Notebook


## Model Performance

Two machine learning models were trained and evaluated:

| Metric | Logistic Regression | Random Forest |
|---|---:|---:|
| Accuracy | 74.38% | 77.86% |
| Precision (Churn) | 51.13% | 57.01% |
| Recall (Churn) | 78.34% | 66.38% |
| F1-Score (Churn) | 61.88% | 61.00% |
| ROC-AUC | 84.91% | 83.86% |

## Model Explainability

SHAP (SHapley Additive exPlanations) was used to understand:
- Global feature importance.
- How individual features influence churn predictions.
- Individual customer-level predictions.


## Project Structure

```text
Customer-Churn-Prediction/
│
├── data/
│   └── Telco_customer_churn.xlsx
│
├── notebooks/
│   └── Telecom_Customer_Churn_Prediction.ipynb
│
├── models/
│   └── churn_prediction_model.pkl
│
├── reports/
│
├── README.md
├── requirements.txt
└── .gitignore
```


## Conclusion

The project demonstrates how machine learning can help identify customers who are likely to churn.

- Random Forest achieved 77.86% accuracy.
- Logistic Regression achieved a higher ROC-AUC of 84.91%.
- Contract type, customer tenure, internet service, and payment method were important factors influencing churn predictions.
- SHAP helped explain both overall model behavior and individual customer predictions.

These insights can help telecom companies identify at-risk customers and develop better customer-retention strategies.

## Future Improvements

- Deploy the model using Streamlit.
- Improve model performance through hyperparameter tuning.
- Evaluate different classification thresholds based on business requirements.


### Dataset Source
The dataset used in this project is the IBM Telco Customer Churn sample dataset.