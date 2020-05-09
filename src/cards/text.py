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
        app.textslistscreen.ids.texts_layout.remove_widget(self.parent)

<TextCard>:
    size_hint: 1, None
    height: "180dp"
    elevation: 1

    padding: 20, 0

    on_release:
        app.edit_text(title.text, author.text)

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
    base_text = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def assign_base_text(self, base_text):
        self.base_text = base_text
        self.ids.title.text = str(self.base_text.title)
        self.ids.author.text = str(self.base_text.author)

    def delete_card(self):
        store = JsonStore("data.json")
        store.delete(self.ids.title.text + ' ' + self.ids.author.text)
