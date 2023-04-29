"""
Copyright (C) Microsoft Corporation. All rights reserved.​
 ​
Microsoft Corporation (“Microsoft”) grants you a nonexclusive, perpetual,
royalty-free right to use, copy, and modify the software code provided by us
("Software Code"). You may not sublicense the Software Code or any use of it
(except to your affiliates and to vendors to perform work on your behalf)
through distribution, network access, service agreement, lease, rental, or
otherwise. This license does not purport to express any claim of ownership over
data you may have shared with Microsoft in the creation of the Software Code.
Unless applicable law gives you more rights, Microsoft reserves all other
rights not expressly granted herein, whether by implication, estoppel or
otherwise. ​
 ​
THE SOFTWARE CODE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
MICROSOFT OR ITS LICENSORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER
IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THE SOFTWARE CODE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.
"""
import pickle
from azureml.core import Workspace
from azureml.core.run import Run
import os
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.externals import joblib
import pandas as pd
import numpy as np
import json
import subprocess
from typing import Tuple, List

# run_history_name = 'devops-ai'
# os.makedirs('./outputs', exist_ok=True)
# #ws.get_details()
# Start recording results to AML
# run = Run.start_logging(workspace = ws, history_name = run_history_name)
run = Run.get_submitted_run()


url = "https://gist.githubusercontent.com/suhas-ds/a318d2b1dda8d8cbf2d6990a8f0b7e8a/raw/9b548fab0952dd12b8fdf057188038c8950428f1/loan_dataset.csv"
df = pd.read_csv(url)

# fill the missing values for numerical cols with median
num_col = ['LoanAmount','Loan_Amount_Term','Credit_History']
for col in num_col:
    df[col].fillna(df[col].median(), inplace=True)

# fill the missing values for categorical cols with mode
cat_col = ['Gender','Married','Dependents','Self_Employed']
for col in cat_col:
    df[col].fillna(df[col].mode()[0], inplace=True)

# Total Income = Applicant Income + Coapplicant Income
df['Total_Income'] = df['ApplicantIncome'] + df['CoapplicantIncome']

# drop unnecessary columns
cols = ['ApplicantIncome', 'CoapplicantIncome', "LoanAmount", "Loan_Amount_Term", 'Loan_ID']
df = df.drop(columns=cols, axis=1)

# Label encoding
cols = ['Gender',"Married","Education",'Self_Employed',"Property_Area","Loan_Status","Dependents"]
le = LabelEncoder()
for col in cols:
    df[col] = le.fit_transform(df[col])

# Train test data preparation
target = 'Loan_Status'

X = df.drop(columns=['Loan_Status'], axis=1)
y = df['Loan_Status']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

print("Running train.py")

model = LogisticRegression()
model.fit(X_train, y_train)
print("Accuracy is", model.score(X_test, y_test)*100)
# cross validation - it is used for better validation of model
# eg: cv-5, train-4, test-1
cv_score = cross_val_score(model, X, y, cv=5)
print("Cross validation is",np.mean(cv_score)*100)
run.log("CV_score", np.mean(cv_score)*100)
y_pred = model.predict(X_test)
print("Accuracy = " , accuracy_score(y_test, y_pred))
run.log("accuracy", accuracy_score(y_test, y_pred))


# Save model as part of the run history
model_name = "sklearn_classification_model.pkl"
# model_name = "."

with open(model_name, "wb") as file:
    joblib.dump(value=model, filename=model_name)

# upload the model file explicitly into artifacts
run.upload_file(name="./outputs/" + model_name, path_or_stream=model_name)
print("Uploaded the model {} to experiment {}".format(model_name, run.experiment.name))
dirpath = os.getcwd()
print(dirpath)

# register the model
# run.log_model(file_name = model_name)
# print('Registered the model {} to run history {}'.format(model_name, run.history.name))


print("Following files are uploaded ")
print(run.get_file_names())
run.complete()
