from kivy.app import App
from kivy.config import Config
from kivy.clock import Clock
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.core.audio import SoundLoader
import time

class New(GridLayout):
    clock_label=ObjectProperty()
    def __init__(self, **kwargs):
        super(New, self).__init__(**kwargs)
        Clock.schedule_interval(self.clock_label.update,1)



class ClockLabel(Label):
    def update(self, *args):
        self.text = time.strftime('%I:%M:%S %p')




class MyApp(App):
    def build(self):
    	s = SoundLoader.load('test.wav')
    	#if s:
    		#s.play()
    	return New()


if __name__=="__main__":
    MyApp().run()





#if s:
 #	s.play()