from kivy.app import App
from kivy.config import Config
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
import time
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.properties import StringProperty
from kivy.core.audio import SoundLoader
import string
import random
from questions import getQuestion

alarms=[]
with open('alarms.txt',mode='r+') as file:
    contents=file.read().split('\n')

for i in range(0,len(contents)-1):
    alarms.append(contents[i].split(','))

turn=0

def alarm_txt_update():

    with open("alarms.txt", mode="r+") as file:
        file.truncate()
        for i in range(len(alarms)):
            for j in range(len(alarms[i])):
                if j!=2:
                    file.write(alarms[i][j] + ",")
                else:
                    file.write(alarms[i][j])
            file.write('\n')


class Setting(Screen,Widget):
    hour_=ObjectProperty(None)
    minute_=ObjectProperty(None)
    ampm_=ObjectProperty(None)
    def alarm_set(self):
        hour_restraint=list(str(x) for x in range(1,13))
        minute_restraint=list(str(x) for x in range(0,60))
        ampm_restraint=["AM","PM"]
        global alarms
        global turn
        if(self.hour_.text not in hour_restraint or self.minute_.text not in minute_restraint or self.ampm_.text.upper() not in ampm_restraint):
            print("Invalid Input\n Try Again")
            alarms[turn-1][0]="null"
            print(alarms)
            alarm_txt_update()
        else:
            ampm_data=self.ampm_.text.upper()
            min_data=int(self.minute_.text)
            hour_data=int(self.hour_.text)
            if hour_data<10:
                self.hour_.text="0"+str(hour_data)
            if min_data<10:
                self.minute_.text="0"+str(min_data)

            time_string=self.hour_.text+":"+self.minute_.text+" "+ampm_data
            print(time_string)


            alarms[turn-1][0]=time_string
            print(alarms)
            alarm_txt_update()


sound=SoundLoader.load('default.wav')

class New(Screen):

    clock_label=ObjectProperty()

    text_label1=StringProperty('')
    text_label2=StringProperty('')
    text_label3=StringProperty('')
    text_label4=StringProperty('')
    text_label5=StringProperty('')



    def __init__(self, **kwargs):
        super(New, self).__init__(**kwargs)
        ##self.check_alarm()
        Clock.schedule_interval(self.clock_label.update,1)
        Clock.schedule_interval(lambda dt:self.text1(),1)
        Clock.schedule_interval(lambda dt:self.check_alarm(),60)

    def check_alarm(self):
        time_str = time.strftime('%I:%M %p')

        for i in alarms:
            if time_str in i and i[2] == "on":
                print("true")

                sound.play()
                sm.current = "Selection"
                sm.transition.direction = "right"


    def turn_update(self,number):
        global turn
        turn=number
        print("Setting Alarm: ",turn)

    def text1(self):
        if alarms[0][0]=="null":
            self.text_label1="Alarm 1"

        else:
            self.text_label1= alarms[0][0]
        if alarms[1][0]=="null":
            self.text_label2="Alarm 2"

        else:
            self.text_label2= alarms[1][0]

        if alarms[2][0]=="null":
            self.text_label3="Alarm 3"

        else:
            self.text_label3= alarms[2][0]

        if alarms[3][0]=="null":
            self.text_label4="Alarm 4"

        else:
            self.text_label4= alarms[3][0]
        if alarms[4][0]=="null":
            self.text_label5="Alarm 5"

        else:
            self.text_label5= alarms[4][0]

    def get_switch_state(self, id):
        if (alarms[id-1][2] == "on"):
            return True
        else:
            return False

    # Change status of alarm
    def toogle_status(self, object, active, id):
        if (active):
            alarms[id-1][2] = "on"
        else:
            alarms[id-1][2] = "off"
        alarm_txt_update()

    def text(self,num2):
        if alarms[num2-1][0]=="null":
            return "Alarm"+str(num2)

        else:
            return alarms[num2-1][0]


class ClockLabel(Label):
    def update(self, *args):
        self.text = time.strftime('%I:%M:%S %p')


class Selection(Screen):
    pass

class Captcha(Screen):

    def get_captcha(self):
        charset = string.ascii_letters + string.digits
        return ''.join(random.choice(charset) for i in range(10))

    def validate_captcha(self):
        captcha = self.ids.captcha
        text_input = self.ids.text_input
        result = (captcha.text == text_input.text)
        captcha.text = self.get_captcha()
        text_input.text = ""
        return result

    def get_screen(self, value):
        if(value):
            #stop_alarm()
            sound.stop()
            return "New"
        else:
            return "Captcha"



correct_counter = 0
options = []
answer = ""
question = ""
def get_quiz():
    global question,lis,options,answer
    options.clear()
    question = ""
    answer = ""
    quiz = getQuestion()
    question = quiz['question']
    answer = quiz['options'][quiz['answer']]
    for i in quiz['options'].keys():
        options.append(quiz['options'][i])
get_quiz()


class Quiz(Screen):
    global options,answer,question
    quiz_question = StringProperty('')
    option1 = StringProperty('')
    option2 = StringProperty('')
    option3 = StringProperty('')
    option4 = StringProperty('')
 
    def new_quiz(self):
        get_quiz()
        self.get_question()
        self.get_option()


    def get_question(self):
        #return "Question 1"
        global question 
        self.quiz_question = question     
        #return quiz_question

    def get_option(self):
        #self.get_question()
        self.option1 = str(options[0])
        self.option2 = str(options[1])
        self.option3 = str(options[2])
        self.option4 = str(options[3])
       
    def validate(self,id):
        print(options[id])
        global correct_counter
        if(str(options[id]) == str(answer)):
            #print("TRUE")
            correct_counter += 1
            if(correct_counter !=3):
                return False
            correct_counter = 0
            return True
        else:
            #print("FALSE")
            return False

    def validate_quiz(self, answer):
        if(answer):
            return "New"
        else:
            return "Quiz"


sm=ScreenManager()
class My1App(App):
    def build(self):

        sm.add_widget(New(name="New"))
        sm.add_widget(Setting(name="Setting"))
        sm.add_widget(Selection(name="Selection"))
        sm.add_widget(Captcha(name="Captcha"))
        sm.add_widget(Quiz(name="Quiz"))

        return sm


if __name__=="__main__":
    My1App().run()