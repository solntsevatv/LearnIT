from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder

from kivymd.uix.label import MDLabel

from src.basetext import BaseText


Builder.load_string("""

<SpeakButton@MDFloatingActionButton>:
    icon: "brain"
    theme_text_color: "Secondary"
    md_bg_color: app.theme_cls.primary_color
    pos_hint: { "center_x": 0.5, "y": self.height / 2 / (self.parent.height + 1e-6) }
    on_release:
        base_text = self.parent.parent.parent.base_text
        phrase_index = self.parent.parent.parent.phrase_index
        app.open_speaking(base_text, phrase_index)

<CheckFullTextButton@MDFloatingActionButton>:
    icon: "text-subject"
    theme_text_color: "Secondary"
    md_bg_color: app.theme_cls.primary_color
    pos_hint: { "x": self.width / 2 / (self.parent.width + 1e-6), "y": self.height / 2 / (self.parent.height + 1e-6) }
    on_release:
        base_text = self.parent.parent.parent.base_text
        app.open_viewtexts(base_text)

<LearnTextScreen@Screen>:
    BoxLayout:
        orientation: "vertical"

        MDToolbar:
            id: toolbar
            title: "Название текста"
        
        FloatLayout:
            BoxLayout:
                orientation: "vertical"
                
                MDLabel:
                    theme_text_color: "Secondary"
                    text: "Запомните фрагмент:"
                    size_hint_y: None
                    height: 3 * self.texture_size[1]
                    padding: "20dp", 0
                
                MDSeparator:
                    height: "1dp"

                MDLabel:
                    id: phrase
                    padding: "20dp", "60dp"
                    size_hint_y: None
                    height: self.texture_size[1]
                
                BoxLayout:
        
            SpeakButton:

            CheckFullTextButton:

""", filename="learntextscreen.kv")


class LearnTextScreen(Screen):
    def learn_phrase(self, base_text: BaseText, phrase_index: int) -> None:
        self.base_text = base_text
        self.phrase_index = phrase_index
        self.ids.toolbar.title = base_text.title
        self.ids.phrase.text = base_text.units[phrase_index]
