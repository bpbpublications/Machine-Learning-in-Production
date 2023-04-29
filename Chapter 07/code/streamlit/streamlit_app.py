# Importing Dependencies
import pickle
import streamlit as st
 
# loading the trained model
trained_model = 'trained_model/model_rf.pkl'
model = pickle.load(open(trained_model, 'rb'))
 
@st.cache()
  
# Following function will make the prediction based on data provided by user 
def prediction(Gender, Married, ApplicantIncome, LoanAmount, Credit_History):   
 
    # Pre-processing user input    
    if Gender == "Male":
        Gender = 1
    else:
        Gender = 0
 
    if Married == "Unmarried":
        Married = 1
    else:
        Married = 0
 
    if Credit_History == "Unclear Debts":
        Credit_History = 1
    else:
        Credit_History = 0  

    # Making predictions 
    prediction = model.predict( 
        [[Gender, Married, ApplicantIncome, LoanAmount, Credit_History]])
     
    if prediction == 0:
        pred = 'Rejected'
    else:
        pred = 'Approved'
    return pred
      
  
# Following function is to define home page of streamlit application   
def main():

    # Front end view for app
    html_temp = """ 
    <div style ="background-color:green;padding:1px"> 
        <h1 style ="color:black;text-align:center;">
            Loan Prediction App
        </h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # Following code is to create box field to get user data 
    Gender = st.selectbox('Gender',("Male","Female"))
    Married = st.selectbox('Marital Status',("Unmarried","Married")) 
    ApplicantIncome = st.number_input("Applicants monthly income") 
    LoanAmount = st.number_input("Total loan amount")
    Credit_History = st.selectbox('Credit_History',("Unclear Debts",
                                "No Unclear Debts"))
    result =""
      
    # When Predict button is clicked it will make the prediction and display it 
    if st.button("Predict"): 
        result = prediction(Gender, Married, ApplicantIncome, 
                            LoanAmount, Credit_History) 
        st.success('Your loan is {}'.format(result))
     
if __name__=='__main__': 
    main()