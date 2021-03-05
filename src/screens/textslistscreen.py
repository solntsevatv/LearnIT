from kivy.metrics import dp
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder

from src.cards.text import TextCard
from src.basetext import BaseText


Builder.load_string("""

<AddTextButton@MDFloatingActionButton>:
    icon: "plus"
    theme_text_color: "Secondary"
    md_bg_color: app.theme_cls.primary_color
    pos_hint: {"right": 1 - self.width / 2 / (self.parent.width + 1e-6), "y": self.height / 2 / (self.parent.height + 1e-6) }
    on_release:
        app.open_addtext()

<TextsListScreen@Screen>:
    BoxLayout:
        orientation: "vertical"

        MDToolbar:
            title: "Learn it!"

        FloatLayout:
            ScrollView:
                MDGridLayout:
                    id: texts_layout
                    cols: 1
                    adaptive_height: True
                    padding: "10dp", "20dp"
                    spacing: "20pd", "20dp"

                    # TextCard:

            AddTextButton:

""", filename="textslistscreen.kv")


class TextsListScreen(Screen):
    """Главный экран со списком всех карточек (текстов)."""

    cards_list: list

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cards_list = []

    def clear_texts(self) -> None:
        """
        Очищает список карточек, удаляя их из списка.

        При этом карточки остаются в базе.
        """

        self.ids.texts_layout.clear_widgets()
        self.cards_list.clear()

    def add_text(self, base_text: BaseText) -> None:
        """
        Добавляет новую карточку в список и привязывает
        к ней переданный базовый текст.

        Новая карточка тут же появляется на экране.
        """

        text_card = TextCard(self)
        text_card.assign_base_text(base_text)
        self.ids.texts_layout.add_widget(text_card)
        self.cards_list.append(text_card)

    def refresh_texts(self, texts_data_list: dict) -> None:
        """
        Обновляет список текстов, загружая их из базы.
        
        Если текстов в базе нет - никакого приглашения к
        созданию новых текстов показано не будет.
        """

        self.clear_texts()
        for id, text_data in texts_data_list.items():
            base_text = BaseText(id=id, **text_data)
            self.add_text(base_text)
        self.ids.texts_layout.add_widget(BoxLayout(size_hint_y=None, height=dp(120)))

    def remove_card(self, card: TextCard) -> None:
        """
        Удаляет карточку из списка.

        Этот метод вызывается из самой карточки, и не должен
        по возможности вызываться откуда-либо еще.

        Если переданной карточки в списке нет, поведение
        не определено.
        """

        self.cards_list.remove(card)
        self.ids.texts_layout.remove_widget(card)
