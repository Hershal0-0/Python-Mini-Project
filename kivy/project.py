import kivy
from kivy.app import App
from kivy.uix.label import Label
import datetime as dt
from kivy.clock import Clock 
from kivy.core.audio import SoundLoader
#from kivy.uix.
import time
class MyApp(App):
	def getTime(self):	
		time = str(dt.datetime.now().hour) + ' : ' + str(dt.datetime.now().minute) + ' : ' + str(dt.datetime.now().second)
		return time
	sound = SoundLoader.load('test.wav')
	alarmlist = [[20,35],[20,45],[21,1]]

	def checkForAlarm(self):
		currenttime = [dt.datetime.now().hour, dt.datetime.now().minute]
		if(currenttime in self.alarmlist):
			if(self.sound):
				self.sound.play()		

	def build(self):
		while(True):
			self.checkForAlarm()
			time.sleep(30)
		return Label(text = self.getTime())

if __name__ == "main":
	
	MyApp().run()

#MyApp().run()
