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
            text: "Название текста"

        MDLabel:
            text: "Автор"
    

""", filename="text.py")


class TextCard(MDCard):
	pass