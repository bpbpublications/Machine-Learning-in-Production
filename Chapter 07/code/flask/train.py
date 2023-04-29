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

pickle_model = open("trained_model/model_rf.pkl", mode = "wb") 
pickle.dump(model, pickle_model) 
pickle_model.close()

# loading the trained model
pickle_model = open('trained_model/model_rf.pkl', 'rb') 
model_rf = pickle.load(pickle_model)

prediction = model_rf.predict([[1, 1, 6000, 150, 0]])
print(prediction)

# prediction = model_rf.predict([[1, 1, 5091, 128, 0]]) # No
# prediction = model_rf.predict([[1, 0, 5091, 128, 1]]) # Yes

# Menu driven

# print("Type 'exit' to terminate.....\n")
# print('''Gender: Female = 0, Male=1
# Married: No = 0, Yes = 1
# Education: Graduate = 0 , Under-graduate = 1
# Self_Employed: No = 0, Yes = 1
# Property_Area: Urban = 2, Semiurban = 1, Rural = 0
# Loan_Status: No = 0, Yes = 1\n''')

# print('''Pass the data in following sequence seperated by comma 
# Gender, Married, Dependents,Education,Self_Employed,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area,TotalIncome\n''')

# while True:
#     user_data=input("Enter your data: ")
    
#     if(user_data=="exit"):
#         break

#     data = list(map(float, user_data.split(',')))

#     # exception handling
#     if(len(data)<10):
#         print("Incomplete data provided!!")
#     else:
        
#         # predicting the value
#         predicted_value=model.predict([data])
#         print("/______________________________________________________________________/")
#         if (predicted_value[0]):
#             print("\tCongratulations! your loan approval request is processed")
#         else:
#             print("\tSorry! your loan approval request is rejected")
#         print("/______________________________________________________________________/")