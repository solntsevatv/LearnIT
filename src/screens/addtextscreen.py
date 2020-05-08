from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder

from src.cards.text import TextCard


Builder.load_string("""

<SaveTextButton@MDIconButton>:
    user_font_size: "45sp"
    icon: "check"
    pos_hint: {"right": 1 - 20 / self.parent.width, "center_y": 0.5}
    on_release:
        app.save_text()
        app.confirm_text_input()


<AddTextScreen@Screen>:
    BoxLayout:
        orientation: "vertical"

        MDToolbar:
            title: "Learn it!"
            #save text
            SaveTextButton:
                

        MDTextField:
            hint_text: "Название"
            mode: "rectangle"
            size_hint: 1 - 40 / self.parent.width, None
            pos_hint: {"center_x": 0.5}
            icon_right_color: app.theme_cls.primary_color

        MDTextField:
            hint_text: "Текст"
            mode: "rectangle"
            multiline: True
            size_hint: 1 - 40 / self.parent.width, 1 - 120 / self.parent.height
            pos_hint: {"center_x": 0.5}
            icon_right_color: app.theme_cls.primary_color

""", filename="addtextscreen.kv")


class AddTextScreen(Screen):
	pass