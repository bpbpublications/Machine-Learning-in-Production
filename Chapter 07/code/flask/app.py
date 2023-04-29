# Importing Dependencies
from flask import Flask,render_template,url_for,request
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pickle
import os


app = Flask(__name__)
port = int(os.environ.get("PORT", 80))

# Loading the trained model
pickle_in = open('trained_model/model_rf.pkl', 'rb') 
model = pickle.load(pickle_in)

# Views
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    if request.method == 'POST':

        # Fetch Value for Gender
        gender = request.form['gender'] 
        if gender == "Female":
            gender = int(0.0)
        if gender == "Male":
            gender = int(1.0)

        # Fetch Value for Married
        married = request.form['married'] 
        if married == "No":
            married = int(0.0)
        if married == "Yes":
            married = int(1.0)

        # Fetch value for LoanAmount
        loan_amt = float(request.form['loan_amt'])

        # Fetch value for Total_Income
        total_income = float(request.form['total_income'])

        # Fetch value for Prior Credit_Score
        credit_history = request.form['credit_history'] 
        if credit_history == "No":
            credit_history = int(0.0)
        if credit_history == "Yes":
            credit_history = int(1.0)

        to_predict_list = [gender, married, total_income, loan_amt, credit_history]
        print(to_predict_list)
        prediction_array = np.array(to_predict_list, dtype=np.float32).reshape(1, 5)
        
        # Making Prediction using trained model
        prediction = model.predict(prediction_array)
        prediction_value = prediction[0]
        print(prediction)

        
        if int(prediction_value) == 1:
            status = "Congratulations! your loan approval request is processed"
        if int(prediction_value) == 0:
            status = "Sorry! your loan approval request is rejected"

        return render_template('index.html',prediction = status)

@app.errorhandler(500)
def internal_error(error):
    return "500: Something went wrong"

@app.errorhandler(404)
def not_found(error):
    return "404: Page not found",404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
