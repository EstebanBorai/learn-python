from Athlete import Athlete
from os import chdir

chdir('/Users/esteban/Repos/learn-python/chapter06')

def get_coach_data(filename):
	try:
		with open(filename) as f:
			data = f.readline()
			data = data.strip().split(',')
			return Athlete(data.pop(0), data.pop(0), data)
	except IOError as ioerr:
		print('File Error! ' + str(ioerr))
		return None

sarah = get_coach_data('sarah2.txt')
james = get_coach_data('james2.txt') 
julie = get_coach_data('julie2.txt')
mikey = get_coach_data('mikey2.txt')

print(sarah.top3())
print(james.top3())
print(julie.top3())
print(mikey.top3())
