import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button 
from kivy.uix.widget import Widget
from kivy.core.audio import SoundLoader
from kivy.uix.popup import Popup
class MyGrid(GridLayout):
	
	def __init__(self, **kwargs):
		super(MyGrid, self).__init__(**kwargs)
		self.cols = 1
############################################################		
		self.instance = GridLayout(cols= 2)
		"""self.instance.cols = 2		
		self.instance.add_widget(Label(text="name"))
		self.name = TextInput(multiline=False)
		self.instance.add_widget(self.name)

		self.instance.add_widget(Label(text="lastname"))
		self.lastname = TextInput(multiline=False)
		self.instance.add_widget(self.lastname)

		self.instance.add_widget(Label(text="email"))
		self.email = TextInput(multiline=False)
		self.instance.add_widget(self.email)
##############################################################
		self.add_widget(self.instance)
		self.button = Button(text="submit")
		self.add_widget(self.button)
		self.button.bind(on_press = self.press)"""
		self.popup = Popup(title='Set Alarm',content=Label(text="piss off",size=(400,400),auto_dusmiss = False)
		self.popup.open()


class YourApp(App):
	def build(self):
		return MyGrid()

if __name__ == "__main__":
	YourApp().run()

"""
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button 

class MyGrid(GridLayout):
	def __init__(self, **kwargs):
		super(MyGrid, self).__init__(**kwargs)
		self.cols = 1
		self.instance = GridLayout()
		self.instance.cols = 2

		self.instance.add_widget(Label(text="name: "))
		self.name = TextInput(multiline=False)
		self.instance.add_widget(self.name)

		self.instance.add_widget(Label(text="lastname :"))
		self.lastname = TextInput(multiline=False)
		self.instance.add_widget(self.lastname)

		self.instance.add_widget(Label(text="email :"))
		self.email = TextInput(multiline=False)
		self.instance.add_widget(self.email)

		self.add_widget(self.instance)
		self.button = Button(text="submit" ,font_size = 40)
		self.add_widget(self.button)
		self.button.bind(on_press = self.press)

	def press(self,instance):
		name = self.name.text
		lastname = self.lastname.text
		email=self.email.text
		self.name.text = "ok"
		self.lastname.text="ok"
		self.email.text="ok"

class MyApp(App):
	def build(self):
		return MyGrid()

if __name__ == "__main__":
	MyApp().run()
"""