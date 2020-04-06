"""This file contains logic component of the app"""

from kivy.app import App
from kivy.config import Config
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.uix.dropdown import DropDown
import time
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.properties import StringProperty
from kivy.core.audio import SoundLoader
import string
import random
from questions import getQuestion


""" Reading all the alarms saved in the alarms.text file and storing it in 
    alarms list to check for alarms and modify list."""
alarms=[]
with open('alarms.txt',mode='r+') as file:
    contents=file.read().split('\n')

for i in range(0,len(contents)-1):
    alarms.append(contents[i].split(','))
print(alarms)
turn=0

"""Modifying to alarms.txt file to save changes made to alarms made during app runtime"""
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


"""This function imports a dictionary which consists of a question,answer and 4 options.
    The returned dictionary is used to get Quiz question,options and to verift answer
    during Quiz Screen"""
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


class Setting(Screen,Widget):
    hour_=ObjectProperty(None)
    minute_=ObjectProperty(None)
    ampm_=ObjectProperty(None)
    soundname_=ObjectProperty(None)
    """Logic to set alarm by modifying the alarms list"""
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
            soundname = self.soundname_.text
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
            alarms[turn-1][1]= str(soundname) + ".mp3"
            print(alarms)
            alarm_txt_update()



""" Loading a refernce default sound """
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
        #self.check_alarm()
        Clock.schedule_interval(self.clock_label.update,1)
        Clock.schedule_interval(lambda dt:self.text1(),1)
        Clock.schedule_interval(lambda dt:self.check_alarm(),60)

    """ Checking whether the current time is present inside alarms so as to trigger the alarms.
        This function is triggered every 60 seconds."""
    def check_alarm(self):
        time_str = time.strftime('%I:%M %p')
        global turn
        for i in range(len(alarms)):
            if time_str in alarms[i] and alarms[i][2] == "on":
                global sound
                print("true")
                turn=i
                print(alarms[i][1])
                sound = SoundLoader.load(str(alarms[i][1]))
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

    """Logic to turn alarm on or off."""
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
    '''Snooze function stops the alarms and turnf it on for 10 mins'''
    def snooze_button(self):
        global turn
        alarms[5] = alarms[turn][:]
        a,b=alarms[turn][0].split(":")
        b, c = b.split()
        a = int(a)
        b = int(b)
        b += 10
        if b >= 60:
            b -= 60
            a += 1
            if a > 11:

                if c == "PM":
                    c = "AM"
                else:
                    c = "PM"
        if a < 10:
            a_str = "0" + str(a)
        else:
            a_str = str(a)
        if b < 10:
            b_str = "0" + str(b)
        else:
            b_str = str(b)
        time_str = a_str + ":" + b_str + " " + c
        alarms[turn][0]=time_str
        alarms[5][0] = time_str
        print(alarms)
        alarm_txt_update()
        sound.stop()
        sm.current="New"
        sm.transition.direction="left"


class Captcha(Screen):
    """Function to get captcha"""
    def get_captcha(self):
        charset = string.ascii_letters + string.digits
        return ''.join(random.choice(charset) for i in range(10))

    """This function checks whether entered captcha is correct or not."""
    def validate_captcha(self):
        captcha = self.ids.captcha
        text_input = self.ids.text_input
        result = (captcha.text == text_input.text)
        captcha.text = self.get_captcha()
        text_input.text = ""
        return result


    """This function decides which screen to render based on value returned
        above function after it is triggered.Returns to main app screen is
        true and turns off the alarm else render a new captcha screen if false."""
    def get_screen(self, value):
        if(value):
            #stop_alarm()
            sound.stop()
            return "New"
        else:
            return "Captcha"

    '''Snooze function stops the alarms and turnf it on for 10 mins'''
    def snooze_button(self):
        global turn
        alarms[5] = alarms[turn][:]
        a,b=alarms[turn][0].split(":")
        b, c = b.split()
        a = int(a)
        b = int(b)
        b += 10
        if b >= 60:
            b -= 60
            a += 1
            if a > 11:

                if c == "PM":
                    c = "AM"
                else:
                    c = "PM"
        if a < 10:
            a_str = "0" + str(a)
        else:
            a_str = str(a)
        if b < 10:
            b_str = "0" + str(b)
        else:
            b_str = str(b)
        time_str = a_str + ":" + b_str + " " + c
        alarms[turn][0]=time_str
        alarms[5][0] = time_str
        print(alarms)
        alarm_txt_update()
        sound.stop()
        sm.current="New"
        sm.transition.direction="left"


class Quiz(Screen):
    global options,answer,question
    global correct_counter
    quiz_question = StringProperty('')
    option1 = StringProperty('')
    option2 = StringProperty('')
    option3 = StringProperty('')
    option4 = StringProperty('')
    quiz_counter = StringProperty('')

    """Refresh quiz after quiz is answered."""
    def new_quiz(self):
        #get_quiz()
        self.get_question()
        self.get_option()
        self.get_counter()

    """Updates count of correct answered question"""
    def get_counter(self):
        global correct_counter
        self.quiz_counter = "Quiz correct answer count : " + str(correct_counter)

    """Returns question for quiz"""
    def get_question(self):
        global question 
        self.quiz_question = question     

    '''Sets the 4 options needed for quiz'''
    def get_option(self):
        self.option1 = str(options[0])
        self.option2 = str(options[1])
        self.option3 = str(options[2])
        self.option4 = str(options[3])
       
    """Return true or false depending on option choosen for quiz."""
    def validate(self,id):
        print(options[id])
        if(str(options[id]) == str(answer)):
            return True
        else:
            return False


    '''This function checks if the selected option for quiz question is correct or not.
        If correct,it increments correct counter and if counter value is less than 5,it
        loads a new quiz question or else loads the main screen and turn off the alarm.
        Wrong alarm leads to a new quiz.
    '''
    def validate_quiz(self, answer):
        global sound
        global correct_counter
        if(answer):
            correct_counter += 1
            get_quiz()
            self.get_question()
            self.get_option()
            self.get_counter()
            if(correct_counter < 5):                
                sm.current = "Quiz"
                sm.transition.direction = "left"
                return None
            correct_counter = 0
            sound.stop()
            sm.current = "New"
            sm.transition.direction = "right"
            return None
        else:
            get_quiz()
            self.get_question()
            self.get_option()
            self.get_counter()
            sm.current = "Quiz"
            sm.transition.direction = "right"


    def snooze_button(self):
        global turn
        alarms[5] = alarms[turn][:]
        a,b=alarms[turn][0].split(":")
        b, c = b.split()
        a = int(a)
        b = int(b)
        b += 10
        if b >= 60:
            b -= 60
            a += 1
            if a > 11:

                if c == "PM":
                    c = "AM"
                else:
                    c = "PM"
        if a < 10:
            a_str = "0" + str(a)
        else:
            a_str = str(a)
        if b < 10:
            b_str = "0" + str(b)
        else:
            b_str = str(b)
        time_str = a_str + ":" + b_str + " " + c
        alarms[turn][0]=time_str
        alarms[5][0] = time_str
        print(alarms)
        alarm_txt_update()
        sound.stop()
        sm.current="New"
        sm.transition.direction="left"



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