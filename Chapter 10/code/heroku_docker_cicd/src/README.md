
# prediction_model


![prediction__model](https://img.shields.io/badge/prediction__model-v0.1.0-blue)

![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?) 

![Python version](https://img.shields.io/badge/python-3.6-blue)

#### Problem
Company wants to automate the loan eligibility process based on customer detail provided while filling online application form. 
It is a classification problem where we have to predict whether a loan would be approved or not. 

#### Data
The data corresponds to a set of financial transactions associated with individuals. The data has been standardized, de-trended, and anonymized. 

| Variables         | Description                                    |
|-------------------|------------------------------------------------|
| Loan_ID           | Unique Loan ID                                 |
| Gender            | Male/ Female                                   |
| Married           | Applicant married (Y/N)                        |
| Dependents        | Number of dependents                           |
| Education         | Applicant Education (Graduate/ Under Graduate) |
| Self_Employed     | Self employed (Y/N)                            |
| ApplicantIncome   | Applicant income                               |
| CoapplicantIncome | Coapplicant income                             |
| LoanAmount        | Loan amount in thousands                       |
| Loan_Amount_Term  | Term of loan in months                         |
| Credit_History    | credit history meets guidelines                |
| Property_Area     | Urban/ Semi Urban/ Rural                       |
| Loan_Status       | Loan approved (Y/N)                            |

Source: Kaggle


## Environment Variables

You may need to add the path to environment variable

For instance

`PYTHONPATH=/home/suhas/code/packages/prediction_model:$PYTHONPATH`
`export PYTHONPATH`

Re-open and test using

`echo $PYTHONPATH`


  
## Developement mode

Go to the project directory and install dependencies

```python
pip install -r requirements.txt  
```

Create a pickle file

```python
python prediction_model/train_pipeline.py
```

Creating a source distribution and wheel

```python
python setup.py sdist bdist_wheel
```
## Running Tests

To run tests, run the following command

```bash
  pytest -v
```
This will look for `test_*.py` or `*_test.py` files into directories and sub-directories
```python
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-4.6.11, py-1.10.0, pluggy-0.13.1 -- /home/suhas/code/venv_package/bin/python
cachedir: .pytest_cache
rootdir: /home/suhas/code/packages
collected 3 items                                                              

tests/test_predict.py::test_single_prediction_not_none PASSED            [ 33%]
tests/test_predict.py::test_single_prediction_dtype PASSED               [ 66%]
tests/test_predict.py::test_single_prediction_output PASSED              [100%]

=========================== 3 passed in 1.27 seconds ===========================
```
## Virtual Environment
Install virtualenv

```python
python3 -m pip install virtualenv
```

Check version
```python
virtualenv --version
```

Create virtual environment

```python
virtualenv venv_package
```

Activate virtual environment

For Linux
```python
source venv_package/bin/activate
```
For Windows
```python
venv_package\Scripts\activate
```

Verify python version
```python
(venv_package) suhas@ds:~/code/packages$ python
Python 3.6.9
[GCC 8.4.0] on linux
```
Deactivate virtual environment

```python
deactivate
```


## Installation

#### Install this project with pip

Go to project directory where `setup.py` file is located

To install it in editable or developer mode
```python
pip install -e .
```
```.``` refers to current directory

```-e``` refers to --editable mode

Normal installation
```python
pip install .
```
```.``` refers to current directory

#### To install from GitHub repository

With git
```python
pip install git+https://github.com/suhas-ds/prediction_model.git
```
Without git
```python
pip install https://github.com/suhas-ds/prediction_model/tarball/master
```
or
```python
pip install https://github.com/suhas-ds/prediction_model/zipball/master
```
or
```python
pip install https://github.com/suhas-ds/prediction_model/archive/master.zip
```

## Directory structure

```bash
prediction_model
├── build
│   ├── bdist.linux-x86_64
│   └── lib
│       └── prediction_model
├── dist
│   ├── prediction_model-0.1.0-py3-none-any.whl
│   └── prediction_model-0.1.0.tar.gz
├── MANIFEST.in
├── prediction_model
│   ├── config
│   │   ├── config.py
│   │   └── __init__.py
│   ├── datasets
│   │   ├── __init__.py
│   │   ├── test.csv
│   │   └── train.csv
│   ├── __init__.py
│   ├── pipeline.py
│   ├── predict.py
│   ├── processing
│   │   ├── data_management.py
│   │   ├── __init__.py
│   │   └── preprocessors.py
│   ├── trained_models
│   │   ├── classification_v1.pkl
│   │   └── __init__.py
│   ├── train_pipeline.py
│   └── VERSION
├── prediction_model.egg-info
│   ├── dependency_links.txt
│   ├── PKG-INFO
│   ├── requires.txt
│   ├── SOURCES.txt
│   └── top_level.txt
├── README.md
├── requirements.txt
├── setup.py
└── tests
    ├── pytest.ini
    └── test_predict.py
```

## Usage/Examples

Start python console

```python
(venv_package) suhas@ds:~/code/packages$ python
Python 3.6.9
[GCC 8.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
```
Import package and make the predictions

```python
>>> import prediction_model
>>> from prediction_model import train_pipeline
>>> from prediction_model.predict import make_prediction
>>> import pandas as pd
>>> train_pipeline.run_training()    # Save pickle object of trained model
Saved Pipeline :  classification_v1.pkl
>>> test_data = pd.read_csv("/home/suhas/code/test.csv")    # Load external data
>>> result = make_prediction(test_data[0:1])   # Make prediction
>>> print(result)
{'prediction': ['Y']}
>>> 
```





