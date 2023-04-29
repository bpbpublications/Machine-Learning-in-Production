#Import Libraries
import pandas as pd
import numpy as np
import joblib

#Import other files/modules
from prediction_model.config import config
from prediction_model.processing.data_management import load_pipeline

pipeline_file_name = 'classification_v1.pkl'

_loan_pipe = load_pipeline(pipeline_file_name)

def make_prediction(input_data):
    """Predicting the output"""

    # Read Data
    data = pd.DataFrame(input_data)
    
    # prediction
    prediction = _loan_pipe.predict(data[config.FEATURES])
    output = np.where(prediction==1, 'Y', 'N').tolist()
    results = {'prediction': output}
    return results

