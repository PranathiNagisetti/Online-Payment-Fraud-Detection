from flask import Flask, request, jsonify, render_template
import numpy as np
import joblib

app = Flask(__name__)

# Load model and scaler
model = joblib.load("fraud_model.pkl")
scaler = joblib.load("scaler.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get values from form
        step = float(request.form["step"])
        amount = float(request.form["amount"])
        oldbalanceOrg = float(request.form["oldbalanceOrg"])
        newbalanceOrig = float(request.form["newbalanceOrig"])
        oldbalanceDest = float(request.form["oldbalanceDest"])
        newbalanceDest = float(request.form["newbalanceDest"])
        type_input = request.form["type"]   # dropdown input

        # One-hot encode transaction type
        type_CASH_OUT = 1 if type_input == "CASH_OUT" else 0
        type_DEBIT = 1 if type_input == "DEBIT" else 0
        type_PAYMENT = 1 if type_input == "PAYMENT" else 0
        type_TRANSFER = 1 if type_input == "TRANSFER" else 0

        # Arrange in EXACT feature order
        features = np.array([[step, amount, oldbalanceOrg, newbalanceOrig,
                              oldbalanceDest, newbalanceDest,
                              type_CASH_OUT, type_DEBIT, type_PAYMENT, type_TRANSFER]])

        # Scale values
        scaled_features = scaler.transform(features)

        # Predict
        prediction = model.predict(scaled_features)[0]
        probability = model.predict_proba(scaled_features)[0][1]

        result = "Fraud Transaction" if prediction == 1 else "Legit Transaction"

        return render_template("index.html",
                               prediction=result,
                               probability=round(probability, 4))

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
