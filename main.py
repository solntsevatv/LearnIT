from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.theming import ThemeManager
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.list import OneLineListItem, IRightBodyTouch
from kivymd.uix.selectioncontrol import MDSwitch

Window.size = (360, 720)


class Colours:
    bg_color = (1.0, 0.62, 0.0, 0.5)
    app_name_color = (1.0, 0.62, 0.0, 0.3)
    menu_color = (1.0, 0.62, 0.0, 0.4)


class TestApp(MDApp):
    def change_theme(self, checkbox, value):
        if value:
            self.theme_cls.theme_style = "Dark"
        else:
            self.theme_cls.theme_style = "Light"

    def __init__(self, **kwargs):
        self.theme_cls = ThemeManager()
        self.theme_cls.primary_palette = "DeepOrange"
        self.theme_cls.theme_style = "Light"
        super().__init__(**kwargs)

TestApp().run()