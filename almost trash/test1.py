from kivy.app import App
from kivy.config import Config
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.properties import ObjectProperty

import time

Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '480')


class V3Widget(BoxLayout):
    clock_label = ObjectProperty()

    def __init__(self, **kwargs):
        super(V3Widget, self).__init__(**kwargs)
        Clock.schedule_interval(self.clock_label.update, 1)


class ClockLabel(Label):
    def update(self, *args):
        self.text = time.strftime('%I:%M:%S %p')


class V3App(App):
    def build(self):
        return V3Widget()


if __name__ == "__main__":
    V3App().run()
