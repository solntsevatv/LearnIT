from kivy.metrics import dp
from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder
from kivymd.uix.picker import MDThemePicker
from kivy.storage.jsonstore import JsonStore

from src.cards.text import TextCard


Builder.load_string("""

<SaveSettingsButton@MDIconButton>:
    user_font_size: "45sp"
    icon: "check"
    pos_hint: {"right": 1 - dp(20) / (self.parent.width + 1e-6), "center_y": 0.5}
    on_release:
        self.parent.parent.parent.save_settings(app.theme_cls.primary_palette,\
        app.theme_cls.accent_palette, app.theme_cls.theme_style)
        app.open_textslist()

<Check@MDCheckbox>:
    group: 'group'
    size_hint: None, None
    user_font_size: "25sp"

<SettingsScreen@Screen>:
    BoxLayout:
        orientation: "vertical"

        MDToolbar:
            title: "Настройки"
            SaveSettingsButton:

        ScrollView:
            MDList:
                OneLineListItem:
                    text: "Изменение темы"
                    on_press:
                        app.settingsscreen.show_theme_picker()
                
                
                OneLineListItem:
                    text: "Количество повторений: " + str(int(self.parent.parent.parent.parent.ids.slider.value))
                
                OneLineListItem:
                    MDSlider:
                        id: slider
                        pos_hint: {'center_x': .5, 'center_y': .5}
                        min: 1
                        max: 10
                        value: 5

                OneLineListItem:
                    text: "Режим индикации"
                OneLineListItem:
                    text: "    цветовой"
                    Check:
                        active: True
                        pos_hint: {'center_x': .9, 'center_y': .5}
                OneLineListItem:
                    text: "    звуковой"
                    Check:
                        pos_hint: {'center_x': .9, 'center_y': .5}

                OneLineListItem:
                    text: "Сбросить прогресс"
                    on_release:
                        app.statisticsscreen.delete_statistics()

                OneLineListItem:
                    text: "Удалить все тексты"
                    on_release:
                        app.delete_all_cards()
                        app.textslistscreen.ids.texts_layout.clear_widgets()

""", filename="settings.kv")


class SettingsScreen(Screen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = JsonStore("data.json")
        self.settings = self.data["settings"]
        self.ids.slider.value = self.settings["repeat_amount"]

    def show_theme_picker(self):
        theme_dialog = MDThemePicker()
        theme_dialog.open()

    def save_settings(self, prim_palette: str, acc_palette: str, style: str):
        self.settings["prim_pallete"] = prim_palette
        self.settings["acc_palette"] = acc_palette
        self.settings["theme_style"] = style
        self.settings["repeat_amount"] = int(self.ids.slider.value)
        self.data["settings"] = self.settings
