from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivy.network.urlrequest import UrlRequest
import certifi as cfi


Builder_string = '''
ScreenManager:
    Main:
<Main>:
    name : 'main'
    MDLabel:
        text: 'Loan Prediction App'
        halign: 'center'
        pos_hint: {'center_y':0.9}
        font_style: 'H4'

    MDLabel:
        text: 'Gender'
        pos_hint: {'center_y':0.75}

    MDTextField:
        id: input_1
        hint_text: '0:Female, 1:Male'
        width: 100
        size_hint_x: None
        pos_hint: {'center_y':0.75, 'center_x':0.50}

    MDLabel:
        text: 'Marital Status'
        pos_hint: {'center_y':0.68}

    MDTextField:
        id: input_2
        hint_text: '0:No, 1:Yes'
        width: 100
        size_hint_x: None
        pos_hint: {'center_y':0.68, 'center_x':0.50}

    MDLabel:
        text: 'Applicant Income'
        pos_hint: {'center_y':0.61}

    MDTextField:
        id: input_3
        hint_text: '6000'
        width: 100
        size_hint_x: None
        pos_hint: {'center_y':0.61, 'center_x':0.50}

    MDLabel:
        text: 'Loan Amount'
        pos_hint: {'center_y':0.54}

    MDTextField:
        id: input_4
        hint_text: '150'
        width: 100
        size_hint_x: None
        pos_hint: {'center_y':0.54, 'center_x':0.50}

    MDLabel:
        text: 'Credit History'
        pos_hint: {'center_y':0.47}

    MDTextField:
        id: input_5
        hint_text: '0:Clear Debts, 1:Unclear Debts'
        width: 100
        size_hint_x: None
        pos_hint: {'center_y':0.47, 'center_x':0.50}

    MDLabel:
        pos_hint: {'center_y':0.2}
        halign: 'center'
        text: ''
        id: output_text
        theme_text_color: "Custom"
        text_color: 0, 1, 1, 1

    MDRaisedButton:
        pos_hint: {'center_y':0.1, 'center_x':0.5}
        text: 'Predict'
        on_press: app.predict()
'''

class Main(Screen):
    pass

sm = ScreenManager()
sm.add_widget(Main(name='main'))

class MainApp(MDApp):
    def build(self):
        self.help_string = Builder.load_string(Builder_string)
        return self.help_string

    def predict(self):
        Gender = self.help_string.get_screen('main').ids.input_1.text
        Married = self.help_string.get_screen('main').ids.input_2.text
        ApplicantIncome = self.help_string.get_screen('main').ids.input_3.text
        LoanAmount = self.help_string.get_screen('main').ids.input_4.text
        Credit_History = self.help_string.get_screen('main').ids.input_5.text
        # url = f'http://127.0.0.1:8000/predict_status?gender={Gender}&married={Married}&income={ApplicantIncome}&loan_amt={LoanAmount}&credit_hist={Credit_History}'
        url = f'https://fastapi-appl.herokuapp.com/predict?gender={Gender}&married={Married}&income={ApplicantIncome}&loan_amt={LoanAmount}&credit_hist={Credit_History}'
        self.request = UrlRequest(url=url, on_success=self.res, ca_file=cfi.where(), verify=True)

    def res(self, *args):
        self.data = self.request.result
        ans = self.data
        self.help_string.get_screen('main').ids.output_text.text = ans['status']

MainApp().run()

# if __name__ == "__main__":
#     MainApp().run()