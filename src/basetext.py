class BaseText:
	id = None

	def __init__(self, *, id=None, title="", author="", units=[""]):
		self.title = title
		self.author = author
		self.units = units
		if id is None:
			self.generate_id()
		else:
			self.id = id

	@property
	def text(self):
		"""Возвращает оригинальный текст, составленный из юнитов."""
		return "\n".join(self.units)

	def to_dict(self):
		return dict(title=self.title, author=self.author, units=self.units)

	def generate_id(self):
		"""Генерирует уникальный идентификатор для данного текста.

		Идентификатор представляет собой строковое представление числа,
		сгенерированного на основе заголовка текста и его автора.
		"""

		self.id = str(hash(self.title + self.author))