from typing import List

from kivy.logger import Logger
from kivy.storage.jsonstore import JsonStore
from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder

from kivymd.uix.label import MDLabel

from src.basetext import BaseText

from src.SpeechRecognizion import Record, Speech_to_Text
from src.check import check_text

Builder.load_string("""

<BackButton@MDFloatingActionButton>:
    icon: "backburger"
    theme_text_color: "Secondary"
    md_bg_color: app.theme_cls.primary_color
    pos_hint: {"x": self.width / 2 / (self.parent.width + 1e-6), "y": self.height / 2 / (self.parent.height + 1e-6) }
    on_release:
        base_text = self.parent.parent.parent.base_text
        # phrase_index = self.parent.parent.parent.phrase_index
        app.open_learntext(base_text)

<SpeakingButton@MDFloatingActionButton>:
    icon: "microphone"
    theme_text_color: "Secondary"
    md_bg_color: app.theme_cls.primary_color
    pos_hint: {"center_x": 0.5, "y": self.height / 2 / (self.parent.height + 1e-6) }
    on_release:
        self.parent.parent.parent.repeat_next()

<BrowseResultsButton@MDFloatingActionButton>:
    icon: "eye-check"
    theme_text_color: "Secondary"
    md_bg_color: app.theme_cls.primary_color
    pos_hint: {"right": 1 - self.width / 2 / (self.parent.width + 1e-6), "y": self.height / 2 / (self.parent.height + 1e-6) + 5 }
    on_release:
        base_text = self.parent.parent.parent.base_text
        phrase_index = self.parent.parent.parent.phrase_index
        recognized_phrase = self.parent.parent.parent.recognized_phrase
        app.open_result(base_text, phrase_index, recognized_phrase)

<SpeakingScreen@Screen>:
    BoxLayout:
        orientation: "vertical"

        MDToolbar:
            id: toolbar
            title: "Название текста"
        
        FloatLayout:
            BoxLayout:
                orientation: "vertical"
                
                MDLabel:
                    id: counter
                    theme_text_color: "Secondary"
                    text: "Повторите фрагмент еще N раз."
                    size_hint_y: None
                    height: 3 * self.texture_size[1]
                    padding: dp(20), 0
                
                MDSeparator:
                    height: "1dp"

                MDSpinner:
                    id: spinner
                    size_hint: None, 1
                    size: dp(110), dp(110)
                    pos_hint: {"center_x": 0.5, "center_y": .99}
                    active: False

                BoxLayout:
            
            BackButton:

            SpeakingButton:
                id: speak_btn

            BrowseResultsButton:
                id: result_btn

""", filename="speakingscreen.kv")


class SpeakingScreen(Screen):
    is_recording = False
    recognized_phrase = None

    def learn_phrase(self, base_text: BaseText, phrase_index: int, repeat_amount: int) -> None:
        self.base_text = base_text
        self.phrase_index = phrase_index
        self.initial_repeat_amount = repeat_amount
        self.repeat_amount = repeat_amount
        self.ids.toolbar.title = base_text.title
        self.stop_record_ui()

        btn = self.ids.result_btn
        btn.pos_hint = {
            "right": 1 - btn.width / 2 / (btn.parent.width + 1e-6),
            "y": btn.height / 2 / (btn.parent.height + 1e-6) + 5
        }
        btn = self.ids.speak_btn
        btn.pos_hint = {
            "center_x": 0.5,
            "y": btn.height / 2 / (btn.parent.height + 1e-6)
        }
        self.ids.counter.text = "Повторите фрагмент {} раз(а).".format(self.repeat_amount)

    def repeat_next(self) -> None:
        self.begin_record_ui()
        Logger.info("speaking screen: Record started!")
        Record()
        recognized_text = Speech_to_Text()
        self.stop_record_ui()
        Logger.info("speaking screen: Record stopped!")
        Logger.info("speaking screen: text is \"{}\"".format(recognized_text))
        phrase_data = check_text(recognized_text, self.base_text.units[self.phrase_index])
        Logger.info("speaking screen: checking with \"{}\"".format(self.base_text.units[self.phrase_index]))
        self.repeat_amount -= 1
        if self.repeat_amount > 0:
            btn = self.ids.result_btn
            btn.pos_hint = {
                "right": 1 - btn.width / 2 / (btn.parent.width + 1e-6),
                "y": btn.height / 2 / (btn.parent.height + 1e-6) + 5
            }
            btn = self.ids.speak_btn
            btn.pos_hint = {
                "center_x": 0.5,
                "y": btn.height / 2 / (btn.parent.height + 1e-6)
            }
            self.ids.counter.text = "Повторите фрагмент еще {} раз(а).".format(self.repeat_amount)
        else:
            # use only last one
            self.save_recognized_phrase(phrase_data)

            btn = self.ids.result_btn
            btn.pos_hint = {
                "right": 1 - btn.width / 2 / (btn.parent.width + 1e-6),
                "y": btn.height / 2 / (btn.parent.height + 1e-6)
            }
            btn = self.ids.speak_btn
            btn.pos_hint = {
                "center_x": 0.5,
                "y": btn.height / (btn.parent.height + 1e-6) + 5
            }
            self.ids.counter.text = "Вы повторили фрагмент {} раз(а)!".format(self.initial_repeat_amount)
    
    def save_recognized_phrase(self, phrase_data: tuple) -> None:
        self.recognized_phrase = phrase_data
        if not phrase_data[0]:
            return
        
        Logger.info("speaking screen: phrase saved!")
        store = JsonStore("data.json")
        progress = store["progress"]
        phrases = progress[self.base_text.id]["phrases"]
        phrases.append(dict(per_error=phrase_data[3], per_miss_words=phrase_data[4]))
        progress[self.base_text.id]["phrases"] = phrases
        store["progress"] = progress

    def begin_record_ui(self) -> None:
        self.ids.spinner.active = True
        self.ids.speak_btn.disabled = True
    
    def stop_record_ui(self) -> None:
        self.ids.spinner.active = False
        self.ids.speak_btn.disabled = False
