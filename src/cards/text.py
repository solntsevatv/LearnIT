from kivy.metrics import dp
from kivymd.uix.card import MDCard
from kivy.lang.builder import Builder
from kivy.storage.jsonstore import JsonStore


Builder.load_string("""

<EditTextCard@MDIconButton>:
    size_hint: None, None
    user_font_size: "23sp"
    icon: "file-document-edit-outline"
    pos_hint: {"center_x": 0.85, "center_y": 0.78}
    on_release:
        self.parent.edit_card()

<DeleteTextCard@MDIconButton>:
    size_hint: None, None
    user_font_size: "23sp"
    icon: "close"
    pos_hint: {"center_x": 0.9, "center_y": 0.78}
    on_release:
        self.parent.delete_card()

<TextCard>:
    size_hint: 1, None
    height: "140dp"
    elevation: 1

    padding: "20dp", 0

    on_release:
        app.open_viewtexts(self.base_text)

    BoxLayout:
        orientation: "vertical"

        MDLabel:
            id: author
            text: "Автор"
            size_hint_y: None
            height: dp(40) + self.texture_size[1]
            theme_text_color: "Secondary"
        
        MDSeparator:
            height: "1dp"

        MDLabel:
            id: title
            text: "Название текста"
            size_hint_y: None
            height: dp(60) + self.texture_size[1]

    EditTextCard:
    DeleteTextCard:

""", filename="text.kv")


class TextCard(MDCard):
    """
    Класс для описания карточки с текстом на главном экране - в списке текстов.

    Показывает пользователю базовую информацию о тексте включая
    автора, название текста, статус (выучено/невыучено).
    
    При клике по карточке происходит переход на экран заучивания текста.
    """

    textslistscreen = None
    base_text = None

    def __init__(self, textslistscreen, **kwargs):
        """
        Для инициализации требуется ссылка на родительский экран.

        При инициализации у карточки нет какого-либо конкретного
        привязанного текста. Тем не менее она будет тут же добавлена
        на главный экран.
        """

        self.textslistscreen = textslistscreen
        super().__init__(**kwargs)

    def assign_base_text(self, base_text):
        """
        Привязывает переданный текст к карточке.

        Информация на карточке обновляется автоматически.
        """

        self.base_text = base_text
        self.ids.title.text = str(self.base_text.title)
        self.ids.author.text = str(self.base_text.author)

    def delete_card(self):
        """
        Удаляет карточку из списка.

        Также удаляется текст из базы текстов (осторожно!). При
        попытке удаления карточки повторно поведение не определено.
        """

        self.textslistscreen.remove_card(self)
        store = JsonStore("data.json")
        texts = store["texts"]
        del texts[self.base_text.id]
        store["texts"] = texts

    def edit_card(self):
        """
        Открывает экран редактирования текста, привязанного
        к карточке.

        При попытке редактировать карточку с непривязанным
        текстом поведение не определено.
        """

        import sys
        sys.modules["__main__"].app.edit_card(self)
