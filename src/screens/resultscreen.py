from typing import List

from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder
from kivy.storage.jsonstore import JsonStore

from kivymd.uix.label import MDLabel

from src.basetext import BaseText


Builder.load_string("""

<CheckButton@MDFloatingActionButton>:
    icon: "check"
    theme_text_color: "Secondary"
    md_bg_color: app.theme_cls.primary_color
    pos_hint: {"center_x": .5, "y": self.height / 2 / (self.parent.height + 1e-6) }
    on_release:
        base_text = self.parent.parent.parent.base_text
        result = self.parent.parent.parent.result
        app.exit_result_screen(base_text, result)

<ResultScreen@Screen>:
    BoxLayout:
        orientation: "vertical"

        MDToolbar:
            id: toolbar
            title: "Название текста"
        
        FloatLayout:
            BoxLayout:
                orientation: "vertical"
                
                MDLabel:
                    id: result_percent
                    theme_text_color: "Secondary"
                    text: "Результат: N%"
                    size_hint_y: None
                    height: 3 * self.texture_size[1]
                    padding: "20dp", 0
                
                MDSeparator:
                    height: "1dp"

                MDLabel:
                    id: result_index
                    theme_text_color: "Secondary"
                    text: "Фраза NN"
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
                
                MDSeparator:
                    height: "1dp"

                MDLabel:
                    id: mistake_percent
                    theme_text_color: "Secondary"
                    text: "Процент пропусков:"
                    size_hint_y: None
                    height: 3 * self.texture_size[1]
                    padding: "20dp", 0
                
                MDSeparator:
                    height: "1dp"
                    
                MDLabel:
                    id: mismatch_percent
                    theme_text_color: "Secondary"
                    text: "Процент несовпадений:"
                    size_hint_y: None
                    height: 3 * self.texture_size[1]
                    padding: "20dp", 0
                
                MDSeparator:
                    height: "1dp"

                BoxLayout:
            
            CheckButton:

""", filename="resultsscreen.kv")


class ResultScreen(Screen):
    def show_results(self, base_text: BaseText, phrase_index: int, recognized_phrase: tuple) -> None:
        self.base_text = base_text
        self.phrase_index = phrase_index
        self.ids.toolbar.title = base_text.title
        self.ids.phrase.text = base_text.units[phrase_index]
        self.result = recognized_phrase[0]
        
        self.ids.result_index.text = "Фраза №" + str(1 + phrase_index)
        self.ids.result_percent.text = "Результат: {}".format("хорошо!" if self.result else "плохо")
        self.ids.mistake_percent.text = "Процент пропусков: {}%".format(recognized_phrase[4])
        self.ids.mismatch_percent.text = "Процент несовпадений: {}%".format(recognized_phrase[3])
