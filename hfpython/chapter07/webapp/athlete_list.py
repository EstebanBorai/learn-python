from sanitize import sanitize

class AtheleteList(list):
	def __init__(self, name, date_of_birth=None, times=[]):
		list.__init__([])
		self.name = name
		self.date_of_birth = date_of_birth
		self.extend(times)

	def top3(self):
		return sorted(set([sanitize(t) for t in self]))
