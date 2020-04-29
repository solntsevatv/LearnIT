from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition 
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.backdrop import *
from kivy.metrics import dp 

Window.size = (360, 720)

class Colours:
    Screen.b_ground_color = (1.0, 0.62, 0.0, 0.5)
    name_of_app_color = (1.0, 0.62, 0.0, 0.3)
    menu_color = (1.0, 0.62, 0.0, 0.4)

class LearningScreen(Screen, Colours):
    pass

class ListoftextsScreen(Screen, Colours):
    pass

class SettingsScreen(Screen, Colours):
    pass

class AddingTextScreen(Screen, Colours):
    pass

class TestApp(MDApp):
    
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_hue = "100"
        sm = ScreenManager(transition = WipeTransition())
        sm.add_widget(LearningScreen(name='Learning'))
        sm.add_widget(ListoftextsScreen(name = 'Listoftexts'))
        sm.add_widget(SettingsScreen(name='Settings'))
        sm.add_widget(AddingTextScreen(name='AddText'))
        return sm

if __name__ == '__main__':
    TestApp().run()