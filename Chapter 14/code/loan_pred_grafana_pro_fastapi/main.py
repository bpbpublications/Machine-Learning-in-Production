# Importing Dependencies
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import pickle
import os
import numpy as np
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator

# import prediction_model
# from prediction_model import train_pipeline
from prediction_model.predict import make_prediction
import pandas as pd

app = FastAPI(
    title="Loan Prediction Model API",
    description="A simple API that use ML model to predict the Loan application status",
    version="0.1",
    )

origins = [
    "*"
    ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    )

port = int(os.environ.get("PORT", 8000))

class LoanPred(BaseModel):
    Gender: str
    Married: str
    Dependents: str
    Education: str
    Self_Employed: str
    ApplicantIncome: float
    CoapplicantIncome: float
    LoanAmount: float
    Loan_Amount_Term: float
    Credit_History: float
    Property_Area: str

@app.get('/')
def index():
    return {'message': 'Loan Prediction App'}

@app.get('/health')
def healthcheck():
    return {'status':'ok'}

#defining the function which will make the prediction using the data which the user inputs 
@app.post('/predict_status')
def predict_loan_status(loan_details: LoanPred):
    data = loan_details.dict()
    Gender = data['Gender']
    Married = data['Married']
    Dependents = data['Dependents']
    Education = data['Education']
    Self_Employed = data['Self_Employed']
    ApplicantIncome = data['ApplicantIncome']
    CoapplicantIncome = data['CoapplicantIncome']
    LoanAmount = data['LoanAmount']
    Loan_Amount_Term = data['Loan_Amount_Term']
    Credit_History = data['Credit_History']
    Property_Area = data['Property_Area']

    # Making predictions 
    input_data = [Gender,  Married,  Dependents,  Education,
                Self_Employed,  ApplicantIncome,  CoapplicantIncome,
                LoanAmount,  Loan_Amount_Term,  Credit_History,  Property_Area]
    cols = ['Gender','Married','Dependents',
            'Education','Self_Employed','ApplicantIncome',
            'CoapplicantIncome','LoanAmount','Loan_Amount_Term',
            'Credit_History','Property_Area']
    data_dict = dict(zip(cols,input_data))
    prediction = make_prediction([data_dict])['prediction'][0]

    if prediction == 'Y':
        pred = 'Approved'
    else:
        pred = 'Rejected'

    return {'status':pred}

@app.post('/predict')
def get_loan_details(Gender: str, Married: str, Dependents: str, 
    Education: str, Self_Employed: str, ApplicantIncome: float, 
    CoapplicantIncome: float, LoanAmount: float, Loan_Amount_Term: float, 
    Credit_History: float, Property_Area: str):

    input_data = [Gender,  Married,  Dependents,  Education,
                Self_Employed,  ApplicantIncome,  CoapplicantIncome,
                LoanAmount,  Loan_Amount_Term,  Credit_History,  Property_Area]
    cols = ['Gender','Married','Dependents',
            'Education','Self_Employed','ApplicantIncome',
            'CoapplicantIncome','LoanAmount','Loan_Amount_Term',
            'Credit_History','Property_Area']

    data_dict = dict(zip(cols,input_data))
    prediction = make_prediction([data_dict])['prediction'][0]
    if prediction == 'Y':
        pred = 'Approved'
    else:
        pred = 'Rejected'

    return {'status':pred}


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)

Instrumentator().instrument(app).expose(app)
