# Importing Dependencies
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import pickle
import numpy as np
import pandas as pd

app = FastAPI()
# loading the trained model
trained_model = 'trained_model/model_rf.pkl'
# pickle_in = open(trained_model, 'rb')
model = pickle.load(open(trained_model, 'rb'))


class LoanPred(BaseModel):
	Gender: float
	Married: float
	ApplicantIncome: float
	LoanAmount: float
	Credit_History: float

@app.get('/')
def index():
    return {'message': 'Loan Prediction App'}

# defining the function which will make the prediction using the data which the user inputs 
@app.post('/predict')
def predict_loan_status(loan_details: LoanPred):
	data = loan_details.dict()
	gender = data['Gender']
	married = data['Married']
	income = data['ApplicantIncome']
	loan_amt = data['LoanAmount']
	credit_hist = data['Credit_History']

	# Making predictions 
	prediction = model.predict([[gender, married, income, loan_amt, credit_hist]])

	if prediction == 0:
		pred = 'Rejected'
	else:
		pred = 'Approved'

	return {'status':pred}

if __name__ == '__main__':
	uvicorn.run(app, host='127.0.0.1', port=8000)