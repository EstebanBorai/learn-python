class Athlete:
	def __init__(self, a_name, a_dob=None, a_times=[]):
		self.name = a_name
		self.dob = a_dob
		self.times = a_times

sarah = Athlete('Sarah Sweeney', '2002-6-17', ['2:58', '2:58', '1:56'])
james = Athlete('James')

print(type(sarah))
# <class '__main__.Athlete'>
print(type(james))
# <class '__main__.Athlete'>

print(sarah)
# <__main__.Athlete object at 0x10e4c6dd8>
print(james)
# <__main__.Athlete object at 0x10e4c6e48>

print(sarah.name)
# Sarah Sweeney
print(james.name)
# James

print(sarah.dob)
# 2002-6-17
print(james.dob)
# None

print(sarah.times)
# ['2:58', '2:58', '1:56']
print(james.times)
# []
