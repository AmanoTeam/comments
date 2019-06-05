class CustomDict(dict):
	def __getattr__(self, key):
		return self.get(key)