from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder

from src.cards.text import TextCard


Builder.load_string("""

<SettingsScreen>:
    BoxLayout:
        orientation: "vertical"

        MDToolbar:
            title: "Настройки"

        ScrollView:
            MDList:
                OneLineListItem:
                    text: "Dark theme"
                    MDSwitch:
                        pos_hint: {'center_x': .9, 'center_y': .5}
                        on_active: app.change_theme(*args)

                OneLineListItem:
                    text: "Сбросить прогресс"

                OneLineListItem:
                    text: "Удалить все тексты"
                    on_release:
                        app.store.clear()
                    md_color:

""", filename="textslistscreen.kv")


class SettingsScreen(Screen):
	pass