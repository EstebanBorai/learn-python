from os import chdir
from code_magnets01 import sanitize

chdir('/Users/esteban/Repos/learn-python/hfpython/chapter05')

def get_normalize(file_name):
	with open(file_name) as file:
		data = file.readline()
	return data.strip().split(',')

james = get_normalize('james.txt')
julie = get_normalize('julie.txt')
mikey = get_normalize('mikey.txt')
sarah = get_normalize('sarah.txt')

def show_bests_times(athlete):
	return sorted(set([sanitize(time) for time in athlete]))[0:3]

print(show_bests_times(james))
print(show_bests_times(julie))
print(show_bests_times(mikey))
print(show_bests_times(sarah))
