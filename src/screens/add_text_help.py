from kivy.uix.screenmanager import Screen
from kivy.storage.jsonstore import JsonStore
from kivy.lang.builder import Builder

from typing import Iterable, List, Optional
from kivymd.uix.label import MDLabel

from src.basetext import BaseText
from src.cards.phrase import PhraseCard


Builder.load_string("""

<AddTextHelpScreen>:
    id: add_text_help
    orientation: "vertical"

    AnchorLayout:
        Image:
            width: self.parent.width
            height: self.parent.width / self.image_ratio
            source: "res/3.jpg"

    BackToManualButton:

""", filename="add_text_help.kv")


class AddTextHelpScreen(Screen):
    pass
