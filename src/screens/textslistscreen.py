from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder

from src.cards.text import TextCard


Builder.load_string("""

<AddTextButton@MDFloatingActionButton>:
    icon: "plus"
    theme_text_color: "Secondary"
    md_bg_color: app.theme_cls.primary_color
    pos_hint: {"right": (self.parent.width - 30) / self.parent.width, "y": 30 / self.parent.height}
    width: self.height
    on_release:
        self.screen_manager.current = "addingtext"

<TextsListScreen@Screen>:
    name: "main"

    BoxLayout:
        orientation: "vertical"

        MDToolbar:
            title: "Learn it!"

        FloatLayout:
            ScrollView:
                MDGridLayout:
                    cols: 1
                    adaptive_height: True
                    padding: 10, 20
                    spacing: 20, 20

                    TextCard:
                    TextCard:
                    TextCard:

            AddTextButton:
                screen_manager: root.manager

""", filename="textslistscreen.kv")


class TextsListScreen(Screen):
	pass