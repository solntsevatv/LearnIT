from typing import Optional, List
from itertools import accumulate

from kivy.storage.jsonstore import JsonStore

class BaseText(object):
    """
    Базовый текст.

    Содержит в себе информацию о самом тексте, авторе, названии.
    Также хранит другую дополнительную информацию.

    Текст хранится в виде списка юнитов - атомарных единиц текста.
    """

    def __init__(self, *, id: Optional[int] = None,
            title: str = "", author: str = "", units: List[str] = [""]):
        """
        Инициализирует базовый текст.

        Если id не будет передан, то он сгенерируется автоматически.
        Использование предполагает распаковку сериализованной версии
        базового текста:

            BaseText(id=id, **text_data)
        """

        self.title = title
        self.author = author
        self.units = units
        if id is None:
            self.generate_id()
        else:
            self.id = id

    @property
    def text(self) -> str:
        """Возвращает оригинальный текст, составленный из юнитов."""
        return "\n\n".join(self.units)

    def to_dict(self) -> dict:
        """
        Переводит объект базового текста в питоноский словарь.

        Полезно для дальнейшей сериализации и хранения.
        """

        return dict(title=self.title, author=self.author, units=self.units)

    def generate_id(self) -> None:
        """
        Генерирует уникальный идентификатор для данного текста.

        Идентификатор представляет собой строковое представление числа,
        сгенерированного на основе заголовка текста и его автора.
        """

        self.id = str(hash(self.title + self.author))
