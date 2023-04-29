# Importing the required packages
import pandas as pd
import numpy as np

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier

from matplotlib import pyplot as plt

from sklearn import preprocessing
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn import metrics

import mlflow
# mlflow.set_tracking_uri('file:/home/suhas/test/src/mlruns')

# Reading the data
data = pd.read_csv("loan_dataset.csv")
num_col = data.select_dtypes(include=['int64','float64']).columns.tolist()
cat_col = data.select_dtypes(include=['object']).columns.tolist()
cat_col.remove('Loan_Status')
cat_col.remove('Loan_ID')

# Creating list of categorical and numerical variables
for col in cat_col:
    data[col].fillna(data[col].mode()[0], inplace=True)

for col in num_col:
    data[col].fillna(data[col].median(), inplace=True)

# Clipping extreme values
data[num_col] = data[num_col].apply(lambda x: x.clip(*x.quantile([0.05, 0.95])))

# creating new feature as Total Income
data['LoanAmount'] = np.log(data['LoanAmount']).copy()
data['TotalIncome'] = data['ApplicantIncome'] + data['CoapplicantIncome']
data['TotalIncome'] = np.log(data['TotalIncome']).copy()


# Dropping ApplicantIncome and CoapplicantIncome
data = data.drop(['ApplicantIncome','CoapplicantIncome'], axis=1)

# Label encoding categorical variables
for col in cat_col:
    le = preprocessing.LabelEncoder()
    data[col] = le.fit_transform(data[col])

data['Loan_Status'] = le.fit_transform(data['Loan_Status'])

# Train test split
X = data.drop(['Loan_Status', 'Loan_ID'],1)
y = data.Loan_Status

SEED = 1

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size =0.3, random_state = SEED)

#_______________Random Forest___________________________#

rf = RandomForestClassifier(random_state=SEED)
rf_param_grid = {
    'n_estimators': [400, 700],
    'max_depth': [15,20,25],
    'criterion' : ["gini", "entropy"],
    'max_leaf_nodes': [50, 100]
}

rf_gs = GridSearchCV(
        estimator=rf,
        param_grid=rf_param_grid, 
        cv=5, 
        n_jobs=-1, 
        scoring='accuracy',
        verbose=0
    )
rf_model = rf_gs.fit(X_train, y_train)

#______________Logistic Regresssion__________________________#

lr = LogisticRegression(random_state=SEED)
lr_param_grid = {
    'C': [100, 10, 1.0, 0.1, 0.01],
    'penalty': ['l1','l2'],
    'solver':['liblinear']
}

lr_gs = GridSearchCV(
        estimator=lr,
        param_grid=lr_param_grid, 
        cv=5,
        n_jobs=-1,
        scoring='accuracy',
        verbose=0
    )
lr_model = lr_gs.fit(X_train, y_train)

#___________________Decision Tree__________________________#

dt = DecisionTreeClassifier(
    random_state=SEED
)

dt_param_grid = {
    "max_depth": [3, 5, 7, 9, 11, 13],
    'criterion' : ["gini", "entropy"],
}

dt_gs = GridSearchCV(
        estimator=dt,
        param_grid=dt_param_grid, 
        cv=5,
        n_jobs=-1,
        scoring='accuracy',
        verbose=0
    )
dt_model = dt_gs.fit(X_train, y_train)

#mlflow.set_experiment("Loan_prediction")

# Model evelaution metrics
def model_metrics(actual, pred):
    accuracy = metrics.accuracy_score(y_test, pred)
    f1 = metrics.f1_score(actual, pred, pos_label=1)
    fpr, tpr, thresholds1 = metrics.roc_curve(y_test, pred)
    auc = metrics.auc(fpr, tpr)
    plt.figure(figsize=(8,8))
    # plot auc 
    plt.plot(fpr, tpr, color='blue', label='ROC curve area = %0.2f'%auc)
    plt.plot([0,1],[0,1], 'r--')
    plt.xlim([-0.1, 1.1])
    plt.ylim([-0.1, 1.1])
    plt.xlabel('False Positive Rate', size=14)
    plt.ylabel('True Positive Rate', size=14)
    plt.legend(loc='lower right')
    
    # Save plot
    plt.savefig("plots/ROC_curve.png")
    
    # Close plot
    plt.close()

    return(accuracy, f1, auc)


# MLflow's logging functions
def mlflow_logs(model, X, y, name):
    
     with mlflow.start_run(run_name = name) as run:
        
        # Run id
        run_id = run.info.run_id
        mlflow.set_tag("run_id", run_id)
         
        # Make predictions        
        pred = model.predict(X)
    
        # Generate performance metrics
        (accuracy, f1, auc) = model_metrics(y, pred)

        # Logging best parameters 
        mlflow.log_params(model.best_params_)

        # Logging model metric 
        mlflow.log_metric("Mean cv score", model.best_score_)
        mlflow.log_metric("Accuracy", accuracy)
        mlflow.log_metric("f1-score", f1)
        mlflow.log_metric("AUC", auc)

        # Logging artifacts and model
        mlflow.log_artifact("plots/ROC_curve.png")
        mlflow.sklearn.log_model(model, name)
        
        mlflow.end_run()

# Make predictions using ML models 

mlflow_logs(dt_model, X_test, y_test, "DecisionTreeClassifier")
mlflow_logs(lr_model, X_test, y_test, "LogisticRegression")
mlflow_logs(rf_model, X_test, y_test, "RandomForestClassifier")
