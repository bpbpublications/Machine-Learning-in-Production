#Import Libraries
import pandas as pd
import numpy as np
import joblib
from sklearn.metrics import accuracy_score

#Import other files/modules
from prediction_model.config import config
from prediction_model.processing.data_management import load_pipeline

pipeline_file_name = 'classification_v1.pkl'

_loan_pipe = load_pipeline(pipeline_file_name)

def make_prediction(input_data):
    """Predicting the output"""

    # Read Data
    data = pd.DataFrame(input_data)
    
    # Prediction
    prediction = _loan_pipe.predict(data[config.FEATURES])
    output = np.where(prediction==1, 'Y', 'N').tolist()
    results = {'prediction': output}
    return results

def train_accuracy(input_data):
    """ Checking accuracy score of training data """

    # Read Data
    data = pd.DataFrame(input_data)
    y_train = np.where(data['Loan_Status']=='Y', 1, 0).tolist()

    # Prediction
    prediction = _loan_pipe.predict(data[config.FEATURES])
    y_pred = prediction.tolist()
    score = accuracy_score(y_train,y_pred)*100
    return score

