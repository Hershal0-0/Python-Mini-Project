from kivy.app import App
from kivy.config import Config
from kivy.clock import Clock
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.properties import ObjectProperty,StringProperty
from kivy.core.audio import SoundLoader
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
import time
import datetime as dt

#Alarm manager.
class AlarmManager:
    #loading alarm sound.
    sound = SoundLoader.load('test.wav')

    def __init__(self):
        #initializing alarm list for saving alarms.
        self.alarmList = [[23,47],[9,37]]
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


class New(GridLayout):
    
    #$cl= Clock
    clock_label=ObjectProperty()
    def __init__(self, **kwargs):
        super(New, self).__init__(**kwargs)        
        #Clock.schedule_interval(self.a_m.checkForAlarm,5)
        Clock.schedule_interval(self.clock_label.update,1)

    def close(self):
        AlarmManager().stopAlarm()
        

class ClockLabel(Label):
    am = AlarmManager()
    am.checkForAlarm()
    Clock.schedule_interval(am.checkForAlarm,59)
    def update(self, *args):
        self.text = time.strftime('%I:%M:%S %p')
        #elf.am.checkForAlarm()

    def close():
        self.am.stopAlarm()


#Class SettingPopup(FloatLayout):
  #@  pass


class MyApp(App):
    def build(self):
        return New()


if __name__=="__main__":
    MyApp().run()