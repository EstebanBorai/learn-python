from code_magnets01 import sanitize

class Athlete:
	def __init__(self, name, date_of_birth, times):
		self.name = name
		self.date_of_birth = date_of_birth
		self.times = times

	def top3(self):
		return (sorted(set(sanitize([sanitize(t) for t in self.times])))[0:3])
	