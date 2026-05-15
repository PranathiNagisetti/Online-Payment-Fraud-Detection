# 💳 Online Payment Fraud Detection System

An AI-powered web application that detects fraudulent online transactions using Machine Learning models.
The system analyzes transaction details and predicts whether a transaction is **Fraudulent** or **Legitimate** with a probability score.

---

# 🚀 Live Demo

🔗 Add your deployed Hugging Face/Render link here

Example:

```md
https://huggingface.co/spaces/Pranathi55/OnlinePaymentFraudDetection
```

---

# 📌 Features

✅ Real-time fraud prediction
✅ Ensemble Machine Learning approach
✅ User-friendly web interface
✅ Fraud probability score
✅ Supports multiple transaction types
✅ Scaled and preprocessed input data
✅ Deployed as a live web application

---

# 🧠 Machine Learning Models Used

The project uses an ensemble of:

* Logistic Regression
* Random Forest Classifier

Predictions from both models are combined to improve accuracy and reliability.

---

# 📂 Project Structure

```bash
Online-Payment-Fraud-Detection/
│
├── app.py
├── requirements.txt
├── logistic_model.pkl
├── random_forest_model.pkl
├── scaler.pkl
├── templates/
├── static/
└── README.md
```

---

# 📊 Input Features

The model predicts fraud based on:

* Step
* Amount
* Old Balance Origin
* New Balance Origin
* Old Balance Destination
* New Balance Destination
* Transaction Type
* Fraud Flag

---

# ⚙️ Tech Stack

* Python
* Scikit-learn
* Pandas
* NumPy
* Gradio / Flask
* Joblib
* Hugging Face Spaces

---

# 🖥️ Installation & Running Locally

## 1️⃣ Clone Repository

```bash
git clone https://github.com/PranathiNagisetti/Online-Payment-Fraud-Detection.git
```

---

## 2️⃣ Navigate to Project Folder

```bash
cd Online-Payment-Fraud-Detection
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Run Application

```bash
python app.py
```

---

# 🌐 Deployment

This project is deployed using:

* Hugging Face Spaces

Deployment includes:

* Model hosting
* Real-time prediction
* Interactive web interface

---

# 📈 Output

The application returns:

* Fraud / Not Fraud prediction
* Fraud probability percentage

Example:

```text
⚠️ Fraud Detected
Probability: 92.45%
```

---

# 🔥 Future Enhancements

* Add Deep Learning models
* Real-time transaction monitoring
* Fraud analytics dashboard
* Visual probability charts
* API integration
* Database support

---
Output Screens:
<img width="1908" height="924" alt="image" src="https://github.com/user-attachments/assets/2eaa7817-7103-4857-aede-d60d2a944c97" />

<img width="1278" height="718" alt="image" src="https://github.com/user-attachments/assets/fce671bf-d0a1-436c-ae6b-41b86e46a64c" />

<img width="1100" height="584" alt="image" src="https://github.com/user-attachments/assets/703044d4-38d0-43c4-bbcf-7fc7f80ce694" />

---

# 👩‍💻 Author

## NAGISETTI PRANATHI

Computer Science Engineering Student
Passionate about Artificial Intelligence, Machine Learning, and Full Stack Development.

---

# 📜 License

This project is developed for educational and research purposes.
