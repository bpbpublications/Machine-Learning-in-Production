# Importing dependencies
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

# def test_pred():
#     # response = client.post("/predict_status")
#     url = "http://127.0.0.1:8005/predict_status"
#     payload = json.dumps({
#                         "Gender":"Male",
#                         "Married":"Yes",
#                         "Dependents":"0",
#                         "Education":"Graduate",
#                         "Self_Employed":"No",
#                         "ApplicantIncome":5720,
#                         "CoapplicantIncome":0,
#                         "LoanAmount":110,
#                         "Loan_Amount_Term":360,
#                         "Credit_History":1,
#                         "Property_Area":"Urban"
#                         })

#     headers = {
#       'Content-Type': 'application/json'
#     }

#     response = requests.request("POST", url, headers=headers, data=payload)

#     print(response.text)
#     assert response.json() == {"status": "Approved"}


def test_pred():
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

    response = client.post("/predict_status", json=data)
    assert response.json()["status"] != ''
    assert response.json() == {"status": "Approved"}