# Online Payment Fraud Detection

**Description:** A Machine Learning-based system to detect and prevent fraudulent online payment transactions in real-time.

---

## Project Overview

With the exponential growth of online transactions, fraud detection has become a critical challenge for financial institutions. This project leverages Machine Learning techniques to analyze transaction data and identify fraudulent activities before they cause financial loss. The system learns patterns from historical data and distinguishes between legitimate and suspicious transactions.

Key objectives:  
- Build an accurate and reliable model to detect online payment fraud.  
- Enable real-time monitoring and alerting for suspicious transactions.  
- Improve financial security for users and institutions.

---

## Features

- **Fraud Detection:** Identify fraudulent transactions effectively.  
- **Real-time Predictions:** Model can be integrated for live transaction monitoring.  
- **Machine Learning Models Implemented:**
  - Logistic Regression
  - Decision Tree Classifier
  - Random Forest Classifier
  
- **Performance Metrics:**
  - Precision, Recall, F1-Score
  - Confusion Matrix
  - AUC-ROC Score

---

## Dataset: https://www.kaggle.com/code/saadatkhalid/online-payments-fraud-detection-with-ml

The dataset contains anonymized transaction records with features including:

step: represents a unit of time where 1 step equals 1 hour
type: type of online transaction
amount: the amount of the transaction
nameOrig: customer starting the transaction
oldbalanceOrg: balance before the transaction
newbalanceOrig: balance after the transaction
nameDest: recipient of the transaction
oldbalanceDest: initial balance of recipient before the transaction
newbalanceDest: the new balance of recipient after the transaction
isFraud: fraud transaction
