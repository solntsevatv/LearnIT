class BaseText:
	def __init__(self, **kwargs):
		self.title = kwargs["title"]
		self.author = kwargs["author"]
		self.units = kwargs["units"]

	@property
	def text(self):
		return "\n".join(self.units)
	