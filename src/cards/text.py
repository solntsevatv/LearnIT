from kivymd.uix.card import MDCard
from kivy.lang.builder import Builder
from kivy.storage.jsonstore import JsonStore


Builder.load_string("""

<DeleteTextCard@MDIconButton>:
    size_hint: None, None
    user_font_size: "25sp"
    icon: "close"
    pos_hint: {"center_x": 0.9, "center_y": 0.78}
    on_release:
        self.parent.delete_card()

<TextCard>:
    size_hint: 1, None
    height: "180dp"
    elevation: 1

    padding: 20, 0

    on_release:
        self.edit_card()

    BoxLayout:
        orientation: "vertical"

        MDLabel:
            id: title
            text: "Название текста"

        MDLabel:
            id: author
            text: "Автор"

    DeleteTextCard:
    

""", filename="text.py")


class TextCard(MDCard):
    textslistscreen = None
    base_text = None

    def __init__(self, textslistscreen, **kwargs):
        self.textslistscreen = textslistscreen
        super().__init__(**kwargs)

    def assign_base_text(self, base_text):
        self.base_text = base_text
        self.ids.title.text = str(self.base_text.title)
        self.ids.author.text = str(self.base_text.author)

    def delete_card(self):
        self.textslistscreen.remove_card(self)
        store = JsonStore("data.json")
        texts = store["texts"]
        del texts[self.base_text.id]
        store["texts"] = texts

    def edit_card(self):
        import sys
        sys.modules["__main__"].app.edit_card(self)
