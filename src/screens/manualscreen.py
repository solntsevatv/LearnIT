from kivy.uix.screenmanager import Screen
from kivy.storage.jsonstore import JsonStore
from kivy.lang.builder import Builder

from typing import Iterable, List, Optional
from kivymd.uix.label import MDLabel

from src.basetext import BaseText
from src.cards.phrase import PhraseCard


Builder.load_string("""

<ManualScreen>:
    id: help
    
    BoxLayout:
        orientation: "vertical"
        MDToolbar:
            title: "Краткая справка по Learnit"
        
        ScrollView:
            MDList:
                OneLineListItem:
                    text: "Боковое меню"
                    on_release:
                        app.open_navlayout_help()

                OneLineListItem:
                    text: "Главный экран"
                    on_release:
                        app.open_main_help()

                OneLineListItem:
                    text: "Редактировaние и добавление текста " 
                    on_release:
                        app.open_add_text_help() 

                OneLineListItem:
                    text: "Обучение "
                    on_release:
                        app.open_teach_help() 

""", filename="manualscreen.kv")


class ManualScreen(Screen):
    pass
