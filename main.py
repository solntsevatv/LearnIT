from kivy.core.window import Window
from kivy.storage.jsonstore import JsonStore
from kivymd.app import MDApp
from kivymd.theming import ThemeManager
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang.builder import Builder

from src.screens.textslistscreen import TextsListScreen
from src.screens.settingsscreen import SettingsScreen
from src.screens.addtextscreen import AddTextScreen

from src.navlayout import NavLayout

Window.size = (360, 720)


main_kv = """

NavigationLayout:
    ScreenManager:
        id: screen_manager

        TextsListScreen:
            name: "textslist"
        AddTextScreen:
            name: "addtext"
        SettingsScreen:
            name: "settings"

    NavLayout:

"""


class Colours:
    bg_color = (1.0, 0.62, 0.0, 0.5)
    app_name_color = (1.0, 0.62, 0.0, 0.3)
    menu_color = (1.0, 0.62, 0.0, 0.4)


class MainApp(MDApp):
    store = JsonStore("texts.json")

    def __init__(self, **kwargs):
        self.theme_cls.primary_palette = "DeepOrange"
        super().__init__(**kwargs)

    def change_theme(self, checkbox, value):
        if value:
            self.theme_cls.theme_style = "Dark"
        else:
            self.theme_cls.theme_style = "Light"

    def build(self):
        self.root = Builder.load_string(main_kv, filename="main.kv")

    def open_textslist(self):
        self.root.ids.screen_manager.current = "textslist"

    def open_addtext(self):
        self.root.ids.screen_manager.current = "addtext"

    def confirm_text_input(self):
        self.root.ids.screen_manager.current = "textslist"

    def open_settings(self):
        self.root.ids.screen_manager.current = "settings"


MainApp().run()