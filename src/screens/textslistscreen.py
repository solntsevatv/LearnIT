from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder

from src.cards.text import TextCard
from src.basetext import BaseText



Builder.load_string("""

<AddTextButton@MDFloatingActionButton>:
    icon: "plus"
    theme_text_color: "Secondary"
    md_bg_color: app.theme_cls.primary_color
    pos_hint: {"right": (self.parent.width - 30) / self.parent.width, "y": 30 / self.parent.height}
    width: self.height
    on_release:
        app.open_addtext()

<TextsListScreen@Screen>:
    BoxLayout:
        orientation: "vertical"

        MDToolbar:
            title: "Learn it!"

        FloatLayout:
            ScrollView:
                MDGridLayout:
                    id: texts_layout
                    cols: 1
                    adaptive_height: True
                    padding: 10, 20
                    spacing: 20, 20

                    # TextCard:

            AddTextButton:

""", filename="textslist.kv")


class TextsListScreen(Screen):
    cards_list = []

    def clear_texts(self):
        self.ids.texts_layout.clear_widgets()
        self.cards_list.clear()

    def add_text(self, base_text):
        text_card = TextCard(self)
        text_card.assign_base_text(base_text)
        self.ids.texts_layout.add_widget(text_card)
        self.cards_list.append(text_card)

    def refresh_texts(self, texts_data_list):
        self.clear_texts()
        for id, text_data in texts_data_list.items():
            base_text = BaseText(id=id, **text_data)
            self.add_text(base_text)

    def remove_card(self, card):
        self.cards_list.remove(card)
        self.ids.texts_layout.remove_widget(card)