from kivy.uix.screenmanager import Screen
from kivymd.uix.list import OneLineListItem
from kivy.storage.jsonstore import JsonStore
from kivy.lang.builder import Builder

from typing import Iterable, List, Optional
from kivymd.uix.label import MDLabel

from src.basetext import BaseText
from src.cards.phrase import PhraseCard


Builder.load_string("""

<TeachHelpScreen>:
    id: teach_help

    BoxLayout:
        orientation: "vertical"
        
        ScrollView:
            BoxLayout:
                orientation: "vertical"
                
                MDList:
                    OneLineListItem:
                        text: "Начало обучения"

                Image:
                    source: "res/4-1.jpg"
            
                MDList:
                    OneLineListItem:
                        text: "Шаг 1"

                Image:
                    source: "res/4-2.jpg"
                
                MDList:
                    OneLineListItem:
                        text: "Шаг 2" 

                Image:
                    source: "res/4-3.jpg"
    
    BackToManualButton:

""", filename="teach_help.kv")


class TeachHelpScreen(Screen):
    pass
