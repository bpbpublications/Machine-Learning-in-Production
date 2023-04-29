from tkinter import *

import joblib

trained_model = 'E:/tkinter_ml_app/trained_model/model.pkl'
model = joblib.load(trained_model)

class MyWindow:
    def __init__(self, win):
        # Create a text Label
        self.lbl0=Label(win, text="Loan Prediction App", font=(25))
        self.lbl0.pack(pady=10)
        self.lbl1=Label(win, text='Gender')
        self.lbl2=Label(win, text='Married')
        self.lbl3=Label(win, text='Total Income')
        self.lbl4=Label(win, text='Loan Amount')
        self.lbl5=Label(win, text='Credit History')
        self.lbl6=Label(win, text='Loan Status')
        
        # Create a entry widget to accept the user input
        self.t1=Entry(bd=2)
        self.t1.insert(0, "0:F, 1:M")
        self.t1.bind("<FocusIn>", lambda args: self.t1.delete('0', 'end'))
        
        self.t2=Entry(bd=2)
        self.t2.insert(0, "0:No, 1:Yes")
        self.t2.bind("<FocusIn>", lambda args: self.t2.delete('0', 'end'))
        
        self.t3=Entry(bd=2)
        self.t3.insert(0, "E.g. 6000")
        self.t3.bind("<FocusIn>", lambda args: self.t3.delete('0', 'end'))
        
        self.t4=Entry(bd=2)
        self.t4.insert(0, "E.g. 150")
        self.t4.bind("<FocusIn>", lambda args: self.t4.delete('0', 'end'))
        
        self.t5=Entry(bd=2)
        self.t5.insert(0, "0:Clear Debts, 1:Unclear Debts")
        self.t5.bind("<FocusIn>", lambda args: self.t5.delete('0', 'end'))
        
        self.t6=Entry(bd=2)
        
        # Create a Predict button
        self.btn1 = Button(win, text='Predict')
        
        # Organize widgets appropriately  
        self.lbl1.place(x=100, y=50)
        self.t1.place(x=200, y=50)
        
        self.lbl2.place(x=100, y=100)
        self.t2.place(x=200, y=100)
        
        self.lbl3.place(x=100, y=150)
        self.t3.place(x=200, y=150)
        
        self.lbl4.place(x=100, y=200)
        self.t4.place(x=200, y=200)
        
        self.lbl5.place(x=100, y=250)
        self.t5.place(x=200, y=250, width=165)

        self.b1=Button(win, text='Predict', command=self.predict, fg = 'blue')
        self.b1.place(x=170, y=300)
        
        self.lbl6.place(x=100, y=350)
        self.t6.place(x=200, y=350)
 
    # For making predictions       
    def predict(self):
        self.t6.delete(0, 'end')
        gender = float(self.t1.get())
        married = float(self.t2.get())
        income = float(self.t3.get())
        loan_amt = float(self.t4.get())
        credit_hist = float(self.t5.get())
        prediction = model.predict([[gender, married, income, loan_amt, credit_hist]])[0]
        if prediction == 0:
            pred = 'Rejected'
        else:
            pred = 'Approved'

        self.t6.insert(END, str(pred))

window=Tk()

mywin=MyWindow(window)

# Create a title
window.title('ML App')

# Define size of the window
window.geometry("400x400+10+10")

window.mainloop()