#Import libraries
import pytest

#Import files/modules
from prediction_model.config import config
from prediction_model.processing.data_management import load_dataset
from prediction_model.predict import make_prediction


@pytest.fixture
def single_prediction():
	''' This function will predict the result for a single record'''
	test_data = load_dataset(file_name=config.TEST_FILE)
	single_test = test_data[0:1]
	result = make_prediction(single_test)
	return result

#Test Prediction
def test_single_prediction_not_none(single_prediction):
	''' This function will check if result of prediction is not None'''
	assert single_prediction is not None

def test_single_prediction_dtype(single_prediction):
	''' This function will check if data type of result of prediction is str i.e. string '''
	assert isinstance(single_prediction.get('prediction')[0], str)

def test_single_prediction_output(single_prediction):
	''' This function will check if result of prediction is Y '''
	assert single_prediction.get('prediction')[0] == 'Y'
