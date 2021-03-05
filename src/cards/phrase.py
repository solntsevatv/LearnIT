from kivy.metrics import dp
from kivymd.uix.card import MDCard
from kivy.lang.builder import Builder

from src.basetext import BaseText


Builder.load_string("""

<PhraseCard@MDCard>:
    size_hint: 1, None
    elevation: 1
    padding: "20dp", 0

    BoxLayout:
        orientation: "vertical"

        MDLabel:
            id: phrase
            text: "Текст фразы"

""", filename="phrase.kv")


class PhraseCard(MDCard):
    base_text: BaseText
    index: int

    def __init__(self, base_text: BaseText, index: int):
        super().__init__()
        self.base_text = base_text
        self.index = index
        self.ids.phrase.text = base_text.units[index]
        self.height = dp(20) * (2 + base_text.units[index].count("\n"))
