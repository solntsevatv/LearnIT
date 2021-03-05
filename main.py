from typing import List

from kivy.core.window import Window
from kivy.storage.jsonstore import JsonStore
from kivymd.app import MDApp
from kivymd.theming import ThemeManager
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang.builder import Builder

from src.screens.textslistscreen import TextsListScreen
from src.screens.settingsscreen import SettingsScreen
from src.screens.addtextscreen import AddTextScreen
from src.screens.viewtextsscreen import ViewTextsScreen
from src.screens.statisticsscreen import StatisticsScreen
from src.screens.learntextscreen import LearnTextScreen
from src.screens.speakingscreen import SpeakingScreen
from src.screens.resultscreen import ResultScreen

from src.screens.manualscreen import ManualScreen
from src.screens.navlayout_help import NavlayoutHelpScreen
from src.screens.main_help import MainHelpScreen
from src.screens.add_text_help import AddTextHelpScreen
from src.screens.teach_help import TeachHelpScreen

from src.navlayout import NavLayout

from src.cards.text import TextCard
from src.basetext import BaseText

Window.size = (360, 720)


main_kv = """

NavigationLayout:
    ScreenManager:
        id: screen_manager

    NavLayout:

"""


class MainApp(MDApp):
    def __init__(self, **kwargs):
        data = JsonStore("data.json")
        settings = data["settings"]
        self.theme_cls.primary_palette = settings["prim_pallete"]
        self.theme_cls.accent_palette = settings["acc_palette"]
        self.theme_cls.theme_style = settings["theme_style"]
        super().__init__(**kwargs)

    def build_screens(self) -> None:
        screen_manager = self.root.ids.screen_manager

        self.textslistscreen = TextsListScreen(name="textslist")
        screen_manager.add_widget(self.textslistscreen)
        
        self.addtextscreen = AddTextScreen(name="addtext")
        screen_manager.add_widget(self.addtextscreen)

        self.settingsscreen = SettingsScreen(name="settings")
        screen_manager.add_widget(self.settingsscreen)

        self.viewtextsscreen = ViewTextsScreen(name="viewtexts")
        screen_manager.add_widget(self.viewtextsscreen)

        self.statisticsscreen = StatisticsScreen(name="statistics")
        screen_manager.add_widget(self.statisticsscreen)

        self.learntextscreen = LearnTextScreen(name="learntext")
        screen_manager.add_widget(self.learntextscreen)

        self.speakingscreen = SpeakingScreen(name="speaking")
        screen_manager.add_widget(self.speakingscreen)

        self.resultscreen = ResultScreen(name="result")
        screen_manager.add_widget(self.resultscreen)

        self.manualscreen = ManualScreen(name="manual")
        screen_manager.add_widget(self.manualscreen)

        self.navlayout_help = NavlayoutHelpScreen(name="navlayout_help")
        screen_manager.add_widget(self.navlayout_help)

        self.main_help = MainHelpScreen(name="main_help")
        screen_manager.add_widget(self.main_help)

        self.add_text_help = AddTextHelpScreen(name="add_text_help")
        screen_manager.add_widget(self.add_text_help)

        self.teach_help = TeachHelpScreen(name="teach_help")
        screen_manager.add_widget(self.teach_help)


    def build(self) -> None:
        self.root = Builder.load_string(main_kv, filename="main.kv")
        self.build_screens()
        self.load_all_texts_from_storage(JsonStore("data.json"))

    def open_textslist(self) -> None:
        self.root.ids.screen_manager.current = "textslist"

    def open_addtext(self) -> None:
        self.root.ids.screen_manager.current = "addtext"
        self.addtextscreen.add_new_text()

    def confirm_text_input(self, next_screen: str) -> None:
        self.load_all_texts_from_storage(JsonStore("data.json"))
        self.root.ids.screen_manager.current = next_screen

    def open_settings(self) -> None:
        self.root.ids.screen_manager.current = "settings"

    def open_viewtexts(self, base_text: BaseText) -> None:
        """Открывает экран просмотра текста для базового текста."""
        self.root.ids.screen_manager.current = "viewtexts"
        self.viewtextsscreen.open_text(base_text)
    
    def open_edittext(self, base_text: BaseText) -> None:
        self.root.ids.screen_manager.current = "addtext"
        self.addtextscreen.edit_base_text(base_text, "viewtexts")

    def open_statistics(self) -> None:
        """
        Открывает экран статистики.
        
        Статистика загружается из базы и рассчитывается
        непосредственно на экране статистики.
        """

        self.root.ids.screen_manager.current = "statistics"
        self.statisticsscreen.load_statistics()
    
    def open_manual(self) -> None:
        """Открывает экран cо справкой."""
        self.root.ids.screen_manager.current = "manual"
    
    def open_navlayout_help(self) -> None:
        """Открывает справку по боковому меню."""
        self.root.ids.screen_manager.current = "navlayout_help"
    
    def open_main_help(self) -> None:
        """Открывает справку по главному экрану."""
        self.root.ids.screen_manager.current = "main_help"
    
    def open_add_text_help(self) -> None:
        """Открывает справку по добавлению/изменению текстов."""
        self.root.ids.screen_manager.current = "add_text_help"
    
    def open_teach_help(self) -> None:
        """Открывает справку по обучению."""
        self.root.ids.screen_manager.current = "teach_help"
    
    def open_learntext(self, base_text: BaseText) -> None:
        phrase_index = len(JsonStore("data.json")["progress"][base_text.id]["phrases"])
        if phrase_index >= len(JsonStore("data.json")["texts"][base_text.id]["units"]):
            # начать с начала
            phrase_index = 0
            JsonStore("data.json")["progress"][base_text.id]["phrases"] = []
            JsonStore("data.json")["progress"][base_text.id]["percent"] = 0
        
        self.root.ids.screen_manager.current = "learntext"
        self.learntextscreen.learn_phrase(base_text, phrase_index)

    def open_speaking(self, base_text: BaseText, phrase_index: int = 0) -> None:
        """
        Открывает экран для воспроизведения фразы пользователем.

        Использует количество повторений указанное в базе.
        """

        self.root.ids.screen_manager.current = "speaking"
        repeat_amount = JsonStore("data.json")["settings"]["repeat_amount"]
        self.speakingscreen.learn_phrase(base_text, phrase_index, repeat_amount)

    def open_result(self, base_text: BaseText, phrase_index: int, recognized_phrase: tuple) -> None:
        """Переходит на экран с результатом анализа записи."""
        self.root.ids.screen_manager.current = "result"
        self.resultscreen.show_results(base_text, phrase_index, recognized_phrase)

    def load_all_texts_from_storage(self, store: JsonStore) -> None:
        """Загружает тексты из базы инициализируя список карточек."""
        self.textslistscreen.refresh_texts(store["texts"])
    
    def save_text(self, base_text: BaseText) -> None:
        """
        Сохраняет переданный базовый текст в базе.

        Сбрасывает весь прогресс, если он был в базе.
        При этом обновляет весь список карточек на главном экране.
        Новый текст добавляется в список в виде карточки.
        """

        # добавили в data.json текст
        store = JsonStore("data.json")
        texts = store["texts"]
        texts[base_text.id] = base_text.to_dict()
        store["texts"] = texts

        # сбрасываем прогресс по этому тексту
        progress = store["progress"]
        progress[base_text.id] = {
            "phrases": [],
            "percent": 0
        }
        store["progress"] = progress

        # обновили список снова
        self.load_all_texts_from_storage(store)
    
    def delete_all_cards(self) -> None:
        """
        Удаляет все тексты из базы.

        Осторожно, необратимо!
        """

        store = JsonStore("data.json")
        texts = store["texts"]
        texts.clear()
        store["texts"] = texts

    def edit_card(self, card: TextCard) -> None:
        """Открывает окно редактирования карточки."""
        self.root.ids.screen_manager.current = "addtext"
        self.addtextscreen.edit_base_text(card.base_text, "textslist")
    
    def exit_result_screen(self, base_text: BaseText, result: bool) -> None:
        """
        Выходит из экрана с результатом обработки.

        Если стих содержит ещё не изученные фразы, то переходит к экрану
        заучивания следующей фразы. Иначе - к списку текстов.
        """

        if result:
            phrase_amount = len(JsonStore("data.json")["progress"][base_text.id]["phrases"])
            units_amount = len(JsonStore("data.json")["texts"][base_text.id]["units"])
            if phrase_amount < units_amount:
                app.open_learntext(base_text)
            else:
                app.open_textslist()
        else:
            app.open_learntext(base_text)


if __name__ == "__main__":
    app = MainApp()
    app.run()
