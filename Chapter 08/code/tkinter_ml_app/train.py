# Importing the required packages
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')
from sklearn.ensemble import RandomForestClassifier

from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn import metrics
import pickle

# Loading the data
data = pd.read_csv("data/loan_dataset.csv")

# Missing value treatent (if found)
num_col = data.select_dtypes(include=['int64','float64']).columns.tolist()
cat_col = data.select_dtypes(include=['object']).columns.tolist()
cat_col.remove('Loan_Status')

for col in cat_col:
    try:
        data[col].fillna(data[col].mode()[0], inplace=True)
    except:
        print("Error --------------------------------------->")

for col in num_col:
    try:
        data[col].fillna(data[col].median(), inplace=True)
    except:
        print("Error --------------------------------------->")

# Outlier treatent (if found)
data[num_col] = data[num_col].apply(
    lambda x: x.clip(*x.quantile([0.05, 0.95])))

# Creating a new variable
data['TotalIncome'] = data['ApplicantIncome'] + data['CoapplicantIncome']
data = data.drop(['ApplicantIncome','CoapplicantIncome'], axis=1)

cat_col.remove('Loan_ID')

# Encoding categorical features 
for col in cat_col:
    le = preprocessing.LabelEncoder()
    data[col] = le.fit_transform(data[col])

data['Loan_Status'] = le.fit_transform(data['Loan_Status'])

# Model building
X = data[['Gender', 'Married', 'TotalIncome', 'LoanAmount', 'Credit_History']]
y = data['Loan_Status']
features = X.columns.tolist()

model = RandomForestClassifier(max_depth=4, random_state = 10) 

# model = LogisticRegression(solver='lbfgs', max_iter=1000, random_state=1)
model.fit(X, y)

# saving the model 

pickle_model = open("trained_model/model.pkl", mode = "wb") 
pickle.dump(model, pickle_model) 
pickle_model.close()

# loading the trained model
pickle_model = open('trained_model/model.pkl', 'rb') 
model_rf = pickle.load(pickle_model)

prediction = model_rf.predict([[1, 1, 6000, 150, 0]])
print(prediction)

