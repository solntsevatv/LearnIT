from kivy.uix.screenmanager import Screen
from kivy.storage.jsonstore import JsonStore
from kivy.lang.builder import Builder

from typing import Iterable, List, Optional
from kivymd.uix.label import MDLabel

from src.basetext import BaseText
from src.cards.phrase import PhraseCard


Builder.load_string("""

<BackToManualButton@MDFloatingActionButton>:
    icon: "backburger"
    theme_text_color: "Secondary"
    md_bg_color: app.theme_cls.primary_color
    pos_hint: {"x": self.width / 2 / (self.parent.width + 1e-6), "y": self.height / 2 / (self.parent.height + 1e-6) }
    width: self.height
    on_release:
        app.open_manual()
        

<NavlayoutHelpScreen>:
    id: navlayout_help
    
    AnchorLayout:
        Image:
            width: self.parent.width
            height: self.parent.width / self.image_ratio
            source: "res/1.jpg"
   

    BackToManualButton:
    
""", filename="navlayout_help.kv")


class NavlayoutHelpScreen(Screen):
    pass
