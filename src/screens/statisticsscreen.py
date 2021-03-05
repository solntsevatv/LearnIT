from kivy.uix.screenmanager import Screen
from kivy.storage.jsonstore import JsonStore
from kivy.lang.builder import Builder


Builder.load_string("""
<StatisticsScreen>:
    BoxLayout:
        orientation: "vertical"

        MDToolbar:
            title: "Статистика"
        
        ScrollView:
            MDList:
                OneLineListItem:
                    id: texts_total
                    text: "Текстов всего:"
                
                OneLineListItem:
                    id: texts_learned
                    text: "Текстов выучено:"

""", filename="statisticsscreen.kv")


class StatisticsScreen(Screen):
    def load_statistics(self):
        """Загружает статистику из базы и отображает её на экране."""
        store = JsonStore("data.json")
        texts_total = len(store["texts"].keys())
        texts_learned = sum(map(lambda p: int(p["percent"] == 100), store["progress"].values()))
        self.ids.texts_total.text = "Текстов всего: {}".format(texts_total)
        self.ids.texts_learned.text = "Текстов выучено: {}".format(texts_learned)

    def delete_statistics(self):
        """
        Удаляет статистику из базы.

        Осторожно, необратимо!
        """

        store = JsonStore("data.json")
        texts_total = len(store["texts"].keys())
        texts_learned = store["progress"]
        for p in texts_learned:
            texts_learned[p] = dict(percent=0, phrases=[])
        store["progress"] = texts_learned
        self.ids.texts_total.text = "Текстов всего: {}".format(texts_total)
        self.ids.texts_learned.text = "Текстов выучено: 0"
