from kivy.core.window import Window
from kivy.metrics import dp
from kivy.uix.floatlayout import FloatLayout
from kivymd.app import MDApp
from kivymd.theming import ThemeManager
from kivymd.uix.tab import MDTabsBase


Window.size = (360, 720)


class Colours:
    bg_color = (1.0, 0.62, 0.0, 0.5)
    app_name_color = (1.0, 0.62, 0.0, 0.3)
    menu_color = (1.0, 0.62, 0.0, 0.4)


class LearningTab(FloatLayout, MDTabsBase):
    pass


class TextsListTab(FloatLayout, MDTabsBase):
    pass


class SettingsTab(FloatLayout, MDTabsBase):
    pass


class AddingTextTab(FloatLayout, MDTabsBase):
    pass


class TestApp(MDApp):    
    def __init__(self, **kwargs):
        self.theme_cls = ThemeManager()
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_hue = "500"
        super().__init__(**kwargs)

TestApp().run()