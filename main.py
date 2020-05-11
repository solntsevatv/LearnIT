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

from src.cards.text import TextCard
from src.basetext import BaseText

Window.size = (360, 720)


main_kv = """

NavigationLayout:
    ScreenManager:
        id: screen_manager

        # TextsListScreen:
        #     name: "textslist"
        # AddTextScreen:
        #     name: "addtext"
        # SettingsScreen:
        #     name: "settings"

    NavLayout:

"""


class Colours:
    bg_color = (1.0, 0.62, 0.0, 0.5)
    app_name_color = (1.0, 0.62, 0.0, 0.3)
    menu_color = (1.0, 0.62, 0.0, 0.4)


class MainApp(MDApp):
    store = JsonStore("data.json")

    def __init__(self, **kwargs):
        self.theme_cls.primary_palette = "DeepOrange"
        super().__init__(**kwargs)

    def change_theme(self, checkbox, value):
        if value:
            self.theme_cls.theme_style = "Dark"
        else:
            self.theme_cls.theme_style = "Light"

    def build_screens(self):
        screen_manager = self.root.ids.screen_manager

        self.textslistscreen = TextsListScreen(name="textslist")
        screen_manager.add_widget(self.textslistscreen)
        
        self.addtextscreen = AddTextScreen(name="addtext")
        screen_manager.add_widget(self.addtextscreen)

        self.settingsscreen = SettingsScreen(name="settings")
        screen_manager.add_widget(self.settingsscreen)

    def build(self):
        self.root = Builder.load_string(main_kv, filename="main.kv")
        self.build_screens()
        self.load_all_texts_from_storage()

    def open_textslist(self):
        self.root.ids.screen_manager.current = "textslist"

    def open_addtext(self):
        self.root.ids.screen_manager.current = "addtext"
        self.addtextscreen.add_new_text()

    def confirm_text_input(self):
        self.root.ids.screen_manager.current = "textslist"

    def open_settings(self):
        self.root.ids.screen_manager.current = "settings"

    def load_all_texts_from_storage(self):
        self.textslistscreen.refresh_texts(self.store["texts"])
    
    def save_text(self, base_text):
        # добавили в data.json текст
        texts = self.store["texts"]
        texts[str(base_text.id)] = base_text.to_dict()
        self.store["texts"] = texts

        # обновили список снова
        self.load_all_texts_from_storage()

        # base_text
        # base_text = BaseText(text_dict)
        # self.textslistscreen.add_text(base_text)

    # редактирование происходит следующим образом: если автор и название текста те же,
    # то старая карточка удаляется, а новая остается, если меняются автор и название, то
    # появляется новая карточка. Думаю, это нужно будет исправить, но пока так :)
    def edit_card(self, card):
        self.root.ids.screen_manager.current = "addtext"
        self.addtextscreen.edit_base_text(card.base_text)
        # self.addtextscreen.clear_text_fields()
        # self.addtextscreen.ids.name.insert_text(title)
        # self.addtextscreen.ids.author.insert_text(author)
        # self.addtextscreen.ids.text_input.insert_text(self.store[title + ' ' + author]["units"][0])


app = MainApp()
app.run()
