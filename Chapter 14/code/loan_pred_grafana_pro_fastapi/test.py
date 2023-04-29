from main import app
from fastapi.testclient import TestClient
import pytest
import requests
import json
# import warnings
# warnings.filterwarnings("ignore", category=DeprecationWarning) 

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {'message': 'Loan Prediction App'}


data = {
        "Gender":"Male",
        "Married":"Yes",
        "Dependents":"0",
        "Education":"Graduate",
        "Self_Employed":"No",
        "ApplicantIncome":5720,
        "CoapplicantIncome":0,
        "LoanAmount":110,
        "Loan_Amount_Term":360,
        "Credit_History":1,
        "Property_Area":"Urban"
        }

def test_pred_():
  response = client.post("/predict_status", json=data)
  assert response.json()["status"] != ''
  assert response.json() == {"status": "Approved"}