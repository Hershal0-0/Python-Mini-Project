from kivy.app import App
from kivy.config import Config
from kivy.clock import Clock
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.properties import ObjectProperty,StringProperty
from kivy.core.audio import SoundLoader
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button 
from kivy.uix.widget import Widget
from kivy.uix.slider import Slider
from kivy.uix.switch import Switch
from kivy.uix.popup import Popup
import time
import datetime as dt


#Alarm manager.
class AlarmManager:
    #loading alarm sound.
    sound = SoundLoader.load('test.wav')

    def __init__(self):
        #initializing alarm list for saving alarms.
        self.alarmList = [[13,40],[23,23],[33,33],[3,9],[4,5]]
        #self.sound = SoundLoader.load('test.wav')

    #checking for active alarm.
    def checkForAlarm(self,*args):
        currentTime = [dt.datetime.now().hour, dt.datetime.now().minute]
        #Checking if current time is in alarms.if yes,playing the laoded alarm sound.
        if(currentTime in self.alarmList):
            #self.sound = SoundLoader.load('test.wav')
            if(self.sound):
                self.sound.play()

    #Turning off alarm sound
    def stopAlarm(self):
        if(self.sound):
            self.sound.stop()



class ClockLabel(Label):
    am = AlarmManager()
    am.checkForAlarm()
    Clock.schedule_interval(am.checkForAlarm,60)
    def update(self, *args):
        self.text = time.strftime('%I:%M:%S %p')
        #elf.am.checkForAlarm()

    def close():
        self.am.stopAlarm()


class New(GridLayout):
    cl=ClockLabel()
    #switch_toggle = ObjectProperty()
    #$cl= Clock
    clock_label=ObjectProperty()
    def __init__(self, **kwargs):
        super(New, self).__init__(**kwargs)        
        #Clock.schedule_interval(self.a_m.checkForAlarm,5)
        Clock.schedule_interval(self.clock_label.update,1)
        self.cols = 1



    def switch_toggle(self,*args,pos):
    	if(not args[1]):
    		if(len(self.cl.am.alarmList)!= 0):
    			self.cl.am.alarmList[pos] = [-1,-1]
    	else:
    		saved_hour = str(self.cl.am.alarmList[pos][0])
    		saved_minute = str(self.cl.am.alarmList[pos][0])
    		meridian = "AM"
    		if(int(saved_hour) == 0 ):
    			saved_hour = "12"
    		if(int(saved_hour) > 12):
    			meridian = "PM"
    		layout = GridLayout(cols = 1,padding = 10)
    		popupLabel = Label(text="Enter time")
    		input_layout = GridLayout(cols = 3)
    		tf1 = TextInput(text=saved_hour)
    		input_layout.add_widget(tf1)
    		tf2 = TextInput(text=saved_minute)
    		input_layout.add_widget(tf2)
    		tf3 = TextInput(text=meridian)
    		input_layout.add_widget(tf3)
    		button = Button(text = "Save Alarm")
    		layout.add_widget(input_layout)
    		layout.add_widget(button)

    		popup = Popup(title = "demo",content = layout)
    		popup.open()

    		button.bind(on_press = popup.dismiss)
    		cleaned_meridian = tf3.text
    		if(cleaned_meridian == "AM" and int(tf1.text) == 12):
    			cleaned_hour = 0
    		elif(cleaned_meridian == "PM"):
    			cleaned_hour = int(tf1.text) + 12
    		else:
    			cleaned_hour = int(tf1.text)

    		cleaned_minute = int(tf2.text)
    		new_alarm = [cleaned_hour,cleaned_minute]
    		self.cl.am.alarmList[pos] = new_alarm
    		print(self.cl.am.alarmList)
    		self.cl.am.checkForAlarm()
    		
    		
    def getTime(self,pos):
    	return str(self.cl.am.alarmList[pos-1][0]) + ":" + str(self.cl.am.alarmList[pos-1][1])


        
"""
class ClockLabel(Label):
    am = AlarmManager()
    am.checkForAlarm()
    Clock.schedule_interval(am.checkForAlarm,60)
    def update(self, *args):
        self.text = time.strftime('%I:%M:%S %p')
        #elf.am.checkForAlarm()

    def close():
        self.am.stopAlarm()
"""

#Class SettingPopup(FloatLayout):
  #@  pass


class MyApp(App):
    def build(self):
        return New()


if __name__=="__main__":
    MyApp().run()