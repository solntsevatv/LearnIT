from kivymd.app import MDApp
from kivy.lang.builder import Builder

from cool_widget.cool_widget import CoolWidget


class MultiFileApp(MDApp):
	def build(self):
		return CoolWidget()


MultiFileApp().run()