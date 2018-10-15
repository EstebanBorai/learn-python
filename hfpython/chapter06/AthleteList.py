from code_magnets01 import sanitize

class AthleteList(list):
	def __init__(self, name, birthdate=None, times=[]):
		list.__init__([])
		self.name = name
		self.birthdate = birthdate
		self.extend(times)

	def top3(self):
		return (sorted(set([sanitize(t) for t in self]))[0:3])

test = AthleteList('Esteban Borai')
test.append('2-11')
print(test.top3())
# ['2.11']
# Add times with not uniform data to test
# sanitize function
test.extend(['1:12', '4-22', '3.33'])
print(test.top3())
# ['1.12', '2.11', '3.33']
