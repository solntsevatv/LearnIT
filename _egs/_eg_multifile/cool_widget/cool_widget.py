from kivy.uix.button import Button
from kivy.lang.builder import Builder


Builder.load_file("cool_widget/cool_widget.kv")

class CoolWidget(Button):
	text = "cool widget!"
