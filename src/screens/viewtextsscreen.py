from typing import Iterable, List, Optional

from kivy.metrics import dp
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder

from kivymd.uix.label import MDLabel

from src.basetext import BaseText
from src.cards.phrase import PhraseCard


Builder.load_string("""

<BackToListButton@MDFloatingActionButton>:
    icon: "backburger"
    theme_text_color: "Secondary"
    md_bg_color: app.theme_cls.primary_color
    pos_hint: {"x": self.width / 2 / (self.parent.width + 1e-6), "y": self.height / 2 / (self.parent.height + 1e-6) }
    on_release:
        app.open_textslist()

<LearnTextButton@MDFloatingActionButton>:
    icon: "brain"
    theme_text_color: "Secondary"
    md_bg_color: app.theme_cls.primary_color
    pos_hint: {"center_x": .5, "y": self.height / 2 / (self.parent.height + 1e-6) }
    on_release:
        base_text = self.parent.parent.parent.base_text
        app.open_learntext(base_text)

<EditTextButton@MDFloatingActionButton>:
    icon: "file-edit"
    theme_text_color: "Secondary"
    md_bg_color: app.theme_cls.primary_color
    pos_hint: {"right": 1 - self.width / 2 / (self.parent.width + 1e-6), "y": self.width / 2 / (self.parent.height + 1e-6) }
    on_release:
        app.open_edittext(self.parent.parent.parent.base_text)

<ViewTextsScreen@Screen>:
    BoxLayout:
        orientation: "vertical"

        MDToolbar:
            id: toolbar
            title: "Название текста"
        
        FloatLayout:
            ScrollView:
                MDGridLayout:
                    id: phrases_layout
                    cols: 1
                    adaptive_height: True
                    padding: "10dp", "20dp"
                    spacing: "20dp", "20dp"

                    # PhraseCard:

            BackToListButton:
            LearnTextButton:
            EditTextButton:

""", filename="viewtextsscreen.kv")


class ViewTextsScreen(Screen):
    base_text: Optional[BaseText] = None
    phrases_list: List[PhraseCard] = []

    def open_text(self, base_text: BaseText) -> None:
        self.base_text = base_text
        self.ids.toolbar.title = base_text.title
        self.update_phrases()
    
    def update_phrases(self) -> None:
        self.clear_phrases()
        for i in range(len(self.base_text.units)):
            phrase_card = PhraseCard(self.base_text, i)
            self.phrases_list.append(phrase_card)
            self.ids.phrases_layout.add_widget(phrase_card)
        # add one for margin
        self.ids.phrases_layout.add_widget(BoxLayout(size_hint_y=None, height=dp(120)))

    def clear_phrases(self) -> None:
        self.phrases_list.clear()
        self.ids.phrases_layout.clear_widgets()
