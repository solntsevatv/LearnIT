from kivy.uix.screenmanager import Screen
from kivy.storage.jsonstore import JsonStore
from kivy.lang.builder import Builder

from typing import Iterable, List, Optional
from kivymd.uix.label import MDLabel

from src.basetext import BaseText
from src.cards.phrase import PhraseCard



Builder.load_string("""

<MainHelpScreen>:
    orientation: "vertical"
    
    AnchorLayout:
        Image:
            width: self.parent.width
            height: self.parent.width / self.image_ratio
            source: "res/2.jpg"
    
    BackToManualButton:

""", filename="main_help.kv")


class MainHelpScreen(Screen):
    pass
