from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import joblib

app = Flask(__name__)

# ================= LOAD MODELS =================
lr_model = joblib.load("models/logistic_model.pkl")
dt_model = joblib.load("models/decision_tree_model.pkl")
rf_model = joblib.load("models/random_forest_model.pkl")

scaler = joblib.load("models/scaler.pkl")

# ================= MANUAL FEATURE COLUMNS =================
FEATURE_COLUMNS = [
    'step',
    'amount',
    'oldbalanceOrg',
    'newbalanceOrig',
    'oldbalanceDest',
    'newbalanceDest',
    'isFlaggedFraud',
    'type_CASH_OUT',
    'type_DEBIT',
    'type_PAYMENT',
    'type_TRANSFER'
]

# ================= ROUTES =================
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # ---------- GET INPUT ----------
        step = float(request.form["step"])
        amount = float(request.form["amount"])
        oldbalanceOrg = float(request.form["oldbalanceOrg"])
        newbalanceOrig = float(request.form["newbalanceOrig"])
        oldbalanceDest = float(request.form["oldbalanceDest"])
        newbalanceDest = float(request.form["newbalanceDest"])
        txn_type = request.form["type"]

        # ---------- BASE DATAFRAME ----------
        input_dict = {
            'step': step,
            'amount': amount,
            'oldbalanceOrg': oldbalanceOrg,
            'newbalanceOrig': newbalanceOrig,
            'oldbalanceDest': oldbalanceDest,
            'newbalanceDest': newbalanceDest,
            'isFlaggedFraud':  1, 
            'type': txn_type
        }

        input_df = pd.DataFrame([input_dict])

        # ---------- DUMMY ENCODING ----------
        input_df = pd.get_dummies(input_df, drop_first=True)

        # ---------- ALIGN COLUMNS ----------
        input_df = input_df.reindex(columns=FEATURE_COLUMNS, fill_value=0)

        # ---------- SCALE ----------
        input_scaled = scaler.transform(input_df)

        # ---------- MODEL PREDICTIONS ----------
        lr_pred = lr_model.predict(input_scaled)[0]
        dt_pred = dt_model.predict(input_scaled)[0]
        rf_pred = rf_model.predict(input_scaled)[0]

        # ---------- PROBABILITIES ----------
        lr_prob = lr_model.predict_proba(input_scaled)[0][1]
        dt_prob = dt_model.predict_proba(input_scaled)[0][1]
        rf_prob = rf_model.predict_proba(input_scaled)[0][1]

        # ---------- MAJORITY VOTING ----------
        final_pred = int((lr_pred  + rf_pred) >= 2)
        final_prob = round((lr_prob  + rf_prob) / 2 * 100, 2)

        if final_prob >= 60:
            prediction_text = "Fraud"
        else :
            prediction_text = "Not Fraud"
        
        return render_template( "index.html",
             prediction=prediction_text, probability=final_prob )


    except Exception as e:
        return render_template(
            "index.html",
            error=str(e)
        )


if __name__ == "__main__":
    app.run(debug=True)