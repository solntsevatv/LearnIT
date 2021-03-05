from typing import Optional

from kivy.uix.screenmanager import Screen
from src.screens.textslistscreen import TextsListScreen
from kivy.lang.builder import Builder

from src.cards.text import TextCard
from src.basetext import BaseText

Builder.load_string("""

<SaveTextButton@MDIconButton>:
    user_font_size: "45sp"
    icon: "check"
    pos_hint: {"right": 1 - dp(20) / (self.parent.width + 1e-6), "center_y": 0.5}
    on_release:
        self.parent.parent.parent.save_text()

<AddTextScreen@Screen>:
    BoxLayout:
        orientation: "vertical"

        MDToolbar:
            title: "Learn it!"
            SaveTextButton:
                

        MDTextField:
            id: name
            hint_text: "Название"
            mode: "rectangle"
            size_hint: 1 - dp(40) / (self.parent.width + 1e-6), None
            pos_hint: {"center_x": 0.5}
            icon_right_color: app.theme_cls.primary_color

        MDTextField:
            id: author
            hint_text: "Автор"
            mode: "rectangle"
            size_hint: 1 - dp(40) / (self.parent.width + 1e-6), None
            pos_hint: {"center_x": 0.5}
            icon_right_color: app.theme_cls.primary_color

        MDTextField:
            id: text_input
            hint_text: "Текст"
            mode: "rectangle"
            multiline: True
            size_hint: 1 - dp(40) / (self.parent.width + 1e-6), 1 - dp(120) / (self.parent.height + 1e-6)
            pos_hint: {"center_x": 0.5}
            icon_right_color: app.theme_cls.primary_color

""", filename="addtextscreen.kv")


class AddTextScreen(Screen):
    base_text: Optional[BaseText] = None
    next_screen = "textslist"

    def clear_text_fields(self) -> None:
        self.ids.name.text = ""
        self.ids.author.text = ""
        self.ids.text_input.text = ""

    def update_text_fields(self) -> None:
        self.ids.name.text = self.base_text.title
        self.ids.author.text = self.base_text.author
        self.ids.text_input.text = self.base_text.text

    def add_new_text(self) -> None:
        # сброс текста, чтобы не отредактировать прошлый
        self.base_text = None
        self.clear_text_fields()

    # next_screen добавлен как индикатор того, куда нужно отправить
    # пользователя дальше - на главный экран или на экран просмотра текста
    def edit_base_text(self, base_text: BaseText, next_screen: str) -> None:
        self.base_text = base_text
        self.next_screen = next_screen
        self.update_text_fields()

    def save_text(self):
        import sys
        app = sys.modules["__main__"].app
        
        title = self.ids.name.text
        author = self.ids.author.text
        text = self.ids.text_input.text

        base_text = self.base_text

        if base_text is not None:
            # меняем существующий текст
            base_text = self.base_text
            base_text.title = title
            base_text.author = author
            base_text.units = list(filter(lambda s: len(s.strip()) != 0, text.split("\n\n")))
        else:
            # добавляем новый
            base_text = BaseText(title=title, author=author, units=text.split("\n\n"))


        app.save_text(base_text)
        app.confirm_text_input(self.next_screen)
