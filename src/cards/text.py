from kivymd.uix.card import MDCard
from kivy.lang.builder import Builder


Builder.load_string("""

<TextCard>:
    size_hint: 1, None
    height: "180dp"
    elevation: 1

    padding: 20, 0

    on_release:
        app.open_addtext()

    BoxLayout:
        orientation: "vertical"

        MDLabel:
            id: title
            text: "Название текста"

        MDLabel:
            id: author
            text: "Автор"
    

""", filename="text.py")


class TextCard(MDCard):
    base_text = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def assign_base_text(self, base_text):
        self.base_text = base_text
        self.ids.title.text = str(self.base_text.title)
        self.ids.author.text = str(self.base_text.author)
