from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.theming import ThemeManager
from kivy.uix.screenmanager import Screen, ScreenManager

Window.size = (360, 720)


class Colours:
    bg_color = (1.0, 0.62, 0.0, 0.5)
    app_name_color = (1.0, 0.62, 0.0, 0.3)
    menu_color = (1.0, 0.62, 0.0, 0.4)


class TestApp(MDApp):    
    def __init__(self, **kwargs):
        self.theme_cls = ThemeManager()
        self.theme_cls.primary_palette = "DeepOrange"
        self.theme_cls.theme_style = "Dark"
        super().__init__(**kwargs)

TestApp().run()